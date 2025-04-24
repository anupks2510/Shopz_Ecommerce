from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# DeepSeek API Key – FOR TESTING ONLY. Use env vars for production.
DEEPSEEK_API_KEY = "api-key-here"  # Replace with your actual API key
# Note: In production, use environment variables or a secure vault to store sensitive information like API keys.

# Expanded Predefined Responses Dictionary
predefined_responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you with Shopz?",
    "how are you?": "I'm just a bot, but I'm doing great! How about you?",
    "what is shopz?": "Shopz is an AI-powered e-commerce platform offering personalized recommendations and secure global payments.",
    "who developed shopz?": "Shopz was developed by Piyush Pradeep Panda, Saif Moin Inamdar, Hashir Akhtar Khan, Zaid Irphan Shaikh, and supervised by Dnyaneshwari Akshay Sabale.",
    "how do i convince my teacher to give me good marks?": "Sir/Ma'am, AI is the future, and this project is proof that I am ready to be a part of it. With cutting-edge technology, industry-standard API integrations, and robust security measures, this chatbot is more than just a project—it's an **innovation**. I humbly request you to acknowledge the effort behind this masterpiece! 🙏",
    "tell me a joke": "Why did the shopper bring a ladder? Because the prices were going through the roof!",
    "what is e-commerce fraud?": "E-commerce fraud includes scams like identity theft, chargeback fraud, and fake returns.",
    "how can i secure my online transactions?": "Use strong passwords, enable two-factor authentication, and shop from trusted websites.",
    "what is dropshipping?": "Dropshipping is a business model where retailers sell products without holding inventory, relying on third-party suppliers.",
    "how do smart mirrors work in fashion stores?": "Smart mirrors use AR to let you try on clothes virtually!",
    "what is an ai-powered recommendation engine?": "It’s an algorithm that suggests products based on your shopping behavior and preferences.",
    "how do i file a return request?": "Go to 'My Orders,' select the item, and click 'Request Return.'",
    "what if my order arrives damaged?": "Contact support immediately and upload pictures to process a refund or replacement.",
    "do you offer free shipping?": "Yes! We offer free shipping on orders above ₹500.",
    "how can i track my order?": "Go to 'My Orders' in your account and enter your order ID to track.",
    "how long does delivery take?": "Standard delivery takes 3-5 business days. Express delivery is available in select cities.",
    "do you have seasonal discounts?": "Yes, we run seasonal sales like Diwali, Christmas, and New Year discounts!",
    "can i change my delivery address?": "Yes, you can update your delivery address under 'My Account' before checkout.",
    "how do I contact the seller directly?": "You can message sellers through the 'Contact Seller' button on the product page.",
    "is my payment information safe?": "Yes! We use encryption and PayPal's secure API for all transactions.",
    "do you have gift wrapping options?": "Yes, we offer gift wrapping for selected items at checkout.",
    "how do i make my teacher laugh?": "Sir/Ma'am, yeh chatbot itna intelligent hai ki agar isse 'Biryani kahan milegi?' poochhein toh ye aapko sabse best restaurant recommend karega! 😃",
    "how do i start an e-commerce business?": "Choose a niche, set up a website, find suppliers, and market your products.",
    "what is influencer marketing?": "Influencer marketing uses social media personalities to promote products to their audience.",
    "how does affiliate marketing work?": "Affiliates earn a commission by promoting products and driving sales through unique referral links.",
    "what is the best cashback offer?": "Cashback offers vary by payment method – check credit card and wallet deals for extra savings!",
    "when is the next big sale?": "Sales happen during festivals, holidays, and special promotions – stay tuned!",
    "how do i find the best discounts?": "Use price comparison websites, coupon codes, and follow brands for flash sales!",
    "can ai predict my shopping habits?": "Yes! AI analyzes your browsing history to suggest items you might like.",
    "what is buy now, pay later (bnpl)?": "BNPL allows you to split payments into smaller installments with no or low interest.",
}

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").strip().lower()

            # Check predefined responses
            response = predefined_responses.get(user_message)
            if response:
                return JsonResponse({"response": response})

            # If not predefined, query DeepSeek
            deepseek_response = get_deepseek_response(user_message)
            return JsonResponse({"response": deepseek_response})

        except json.JSONDecodeError:
            return JsonResponse({"response": "Invalid request format."}, status=400)

    return JsonResponse({"error": "Invalid request method."}, status=400)


def get_deepseek_response(query):
    """
    Calls DeepSeek API to get response for the given query.
    """
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": query}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            completion = response.json()
            return completion.get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
        else:
            return f"DeepSeek API error: {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}"
