# Coffee Shop Web Application

## Overview
A full-stack Django web application for an online coffee shop. It features product browsing, user authentication, and order management, backed by a PostgreSQL database running in Docker.

## Features
- **User Authentication**: Secure registration, login, and logout functionalities using a custom user model.
- **Product Catalog**: Browse various coffee products with details including images, prices, descriptions, and categories (Hot Coffee, Cold Coffee, Bakery, etc.).
- **Order Management**: Users can place orders for products and view their order history/status.
- **REST API**: built-in API support for retrieving product data via Django REST Framework.
- **Responsive Interface**: User-friendly design.
- **Database**: Robust PostgreSQL integration for data persistence.

## Tech Stack
- **Backend Framework**: Django 6.0+
- **Database**: PostgreSQL 15 (Dockerized)
- **API**: Django REST Framework
- **Language**: Python 3.13
- **Containerization**: Docker

## Prerequisites
- Python 3.13 or higher
- Docker Desktop or Engine
- `pip` (Python package manager)

## Installation Guide

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd coffeeShop
```

### 2. Set Up Virtual Environment
Create and activate a virtual environment (recommended name: `coffee`).

```bash
# Create
python -m venv coffee

# Activate (Linux/MacOS)
source coffee/bin/activate

# Activate (Windows)
# coffee\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory of the project.
**Note**: The database configuration below utilizes port `5433` to avoid conflicts with default local Postgres installations.

```env
DEBUG=True
SECRET_KEY=django-insecure-)#jv7)!%!#zq(qc7dy6(x%u%g%xdk&%fg@_@+=7@cl!d!j652g
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://coffee_user:Happy_Coffee_Shop.1945@localhost:5433/coffee_shop_db
```

### 5. Database Setup (Docker)
Run the following command to start the PostgreSQL container:

```bash
docker run --name coffe_shop_db -e POSTGRES_PASSWORD=Happy_Coffee_Shop.1945 -p 5433:5432 -d postgres:15
```

Initialize the database user and permissions:
```bash
# Enter the container's Postgres shell
docker exec -it coffe_shop_db psql -U postgres

# Run the following SQL commands:
CREATE USER coffee_user WITH PASSWORD 'Happy_Coffee_Shop.1945';
CREATE DATABASE coffee_shop_db OWNER coffee_user;
GRANT ALL PRIVILEGES ON DATABASE coffee_shop_db TO coffee_user;
ALTER USER coffee_user CREATEDB; -- Required to run Django tests
\q
```

### 6. Apply Migrations & Load Data
Apply the Django migrations to create the creating database schema:
```bash
python manage.py migrate
```

Load the initial backup data (in this specific order to respect foreign keys):
```bash
python manage.py loaddata backup_users.json
python manage.py loaddata backup_products.json
python manage.py loaddata backup_orders.json
```

## Running the Application
Start the development server:
```bash
python manage.py runserver
```
Open your browser and navigate to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Running Tests
This project includes unit tests for products, orders, and user authentication.

Run all tests:
```bash
python manage.py test
```

Run specific app tests:
```bash
python manage.py test users
python manage.py test products
python manage.py test orders
```

## Project Structure
- **`CoffeeWebShop/`**: Main project configuration (settings, URLs, WSGI).
- **`users/`**: Custom user model, authentication views (Login/Register/Logout).
- **`products/`**: Product models, views, and API endpoints.
- **`orders/`**: Order processing, creating orders, and viewing order history.
- **`templates/`**: HTML templates for the application.
- **`manage.py`**: Django CLI utility.

## License
MIT
