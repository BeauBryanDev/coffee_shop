# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django 6.0.1 e-commerce application for a coffee shop (CoffeeWebShop). The project uses SQLite as the database and includes a Products app for managing coffee products.

## Development Environment

**Virtual Environment**: The project uses a Python virtual environment located in the `coffee/` directory.

- Activate: `source coffee/bin/activate`
- Deactivate: `deactivate`

**Dependencies**:
- Production: `requirements.txt` (includes Django 6.0.1, Pillow 12.1.0, ipython, and other tools)
- Development: `requirement-dev.txt` (currently mirrors production)

Install dependencies:
```bash
pip install -r requirements.txt
```

## Common Commands

**Development Server**:
```bash
python manage.py runserver
```

**Database Operations**:
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# View migration status
python manage.py showmigrations

# View SQL for a migration
python manage.py sqlmigrate <app_name> <migration_number>

# Open database shell
python manage.py dbshell
```

**Admin Interface**:
```bash
# Create superuser for /admin access
python manage.py createsuperuser
```

**Testing and Validation**:
```bash
# Run tests
python manage.py test

# Check for configuration errors
python manage.py check

# Interactive Python shell with Django context
python manage.py shell
```

**Data Management**:
```bash
# Export data
python manage.py dumpdata > data.json

# Import data
python manage.py loaddata data.json
```

**Static Files** (when configured):
```bash
python manage.py collectstatic
```

## Architecture

**Project Structure**:
- `CoffeeWebShop/` - Main project configuration (settings, URLs, WSGI)
- `products/` - Django app handling product management
- `coffee/` - Python virtual environment (should not be modified directly)
- `db.sqlite3` - SQLite database file
- `manage.py` - Django management script

**URL Routing**:
- Root URL configuration: `CoffeeWebShop/urls.py`
- Currently only includes admin interface at `/admin/`
- App-specific URLs should be included using `include()` pattern

**Products App**:
- **Model**: `Product` model (products/models.py) with fields:
  - name, description, price, stock, available
  - product_image (ImageField - requires Pillow)
  - slug (auto-generated, unique identifier)
  - category, created_at, updated_at

- **Views** (products/views.py):
  - `home` - TemplateView for homepage
  - `ProductListView` - Paginated product listing (10 per page, ordered by -created_at)
  - `ProductDetailView` - Individual product details
  - Note: There are typos in imports ("dijango", "dijanfo", "dinago" instead of "django")

- **Templates**: Located in `products/templates/products/`
  - base.html, home.html, product_list.html, produdct_detail.html
  - Note: Templates currently empty, typo in filename "produdct_detail.html"

- **Admin**: Not yet configured (admin.py is empty)

**Settings Configuration** (CoffeeWebShop/settings.py):
- `DEBUG = True` - Development mode enabled
- `ALLOWED_HOSTS = []` - Needs configuration for production
- `DATABASES` - SQLite backend at `BASE_DIR / 'db.sqlite3'`
- `STATIC_URL = 'static/'` - Static files not fully configured
- `INSTALLED_APPS` includes 'products' app
- `TEMPLATES` configured with APP_DIRS=True for app-level template discovery

## Known Issues

1. **Import Typos in products/views.py**: Multiple Django imports have typos:
   - `dijango` should be `django` (lines 2-4)
   - `dijanfo` should be `django` (line 5)
   - `dinago` should be `django` (line 6)

2. **Template Typo**: `produdct_detail.html` should be `product_detail.html`

3. **Products App Not Registered in Admin**: The Product model is not registered in admin.py

4. **Templates Are Empty**: All template files are currently empty placeholders

5. **No URL Routes for Products**: Products app URLs not included in main urls.py

6. **Media Files Configuration**: MEDIA_URL and MEDIA_ROOT not configured for product images

## Database

The project uses SQLite with a database file at the root: `db.sqlite3`. The database file is tracked in git (not in .gitignore).

Initial migrations have been created for the products app.

## Notes File

`notes.txt` contains Django command reference in Spanish, including various management commands for migrations, internationalization, and database operations.
