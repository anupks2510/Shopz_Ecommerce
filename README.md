# Shopz Ecommerce - Django Shopping Platform  

![Python](https://img.shields.io/badge/Python-3.11-blue)  
![Django](https://img.shields.io/badge/Django-4.x-green)  
![Status](https://img.shields.io/badge/Status-Development%20(Sandbox)-orange)  
![PayPal](https://img.shields.io/badge/PayPal-Sandbox%20Mode-yellow)

A full-featured e-commerce website built with Django, featuring user authentication, product catalog, cart system, and PayPal payment gateway.

## Current Status
| Feature                  | Status           | Notes                          |
|--------------------------|------------------|--------------------------------|
| Local Development Server | Running          | `python manage.py runserver`   |
| PayPal Payments          | Sandbox Mode     | Testing with fake cards        |
| Order Management         | Functional       | Admin + User panel             |
| Live Deployment          | Coming Soon      | Production PayPal & Hosting    |

> **Important**: PayPal integration is currently in **Sandbox (Test) Mode**.  
> Real transactions are disabled until we go live.

## Features
- User registration & login  
- Product browsing & search  
- Add to cart & checkout  
- PayPal payment gateway (Sandbox)  
- Order history & tracking  
- Responsive design  

## PayPal Sandbox Testing
You can test payments using these official PayPal sandbox cards:

| Card Type       | Card Number          | Expiry | CVV |
|-----------------|----------------------|--------|-----|
| Visa            | 4032039288772636     | Any future date | 123 |
| MasterCard      | 5105105105105100     | Any future date | 123 |
| American Express| 371449635398431      | Any future date | 1234 |

## Setup (Local Development)

```bash
git clone https://github.com/anupks2510/Shopz_Ecommerce.git
cd Shopz_Ecommerce
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
