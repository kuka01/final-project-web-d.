# PhoneHub

PhoneHub is a full-stack e-commerce web application for browsing and purchasing mobile phones. Built with Django Templates for the front-end and Django REST Framework for the back-end API.

## Project Description

Users can browse phones by brand and category, view detailed product pages with reviews, register/login, add phones to favorites, and leave product reviews. The project demonstrates full CRUD operations, token-based authentication, REST API integration with CORS support, and real-time JavaScript search functionality.

## Team Members

- **Person 1** - Tusipov Adil
- **Person 2** - Sabyrzhan Ansar
- **Person 3** - Tashbolat Kuanysh

## Tech Stack

- **Backend:** Django 6.0, Django REST Framework
- **Frontend:** Django Templates, HTML/CSS/JavaScript
- **Database:** SQLite (development)
- **API Testing:** Postman
- **Authentication:** Token-based (DRF TokenAuthentication)

## Features

- User authentication (register, login, logout)
- Browse phones by brand/category with live search
- Product detail pages with reviews and ratings
- Add and manage product reviews (authenticated users only)
- Favorites system with localStorage persistence
- Full CRUD operations for products (moderators only)
- REST API endpoints (9 FBV + 5 CBV) with token authentication
- CORS configuration for external API clients
- Admin panel with custom filters
- Responsive dark AMOLED theme

## Setup Instructions

```bash
git clone https://github.com/kuka01/final-project-web-d.git
cd final-project-web-d
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo  # Load demo data
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

## Default Demo User

- **Username:** demo
- **Password:** demo12345