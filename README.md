# FactoryApp

FactoryApp is a Django-based platform for managing day-to-day factory activity. Workers and managers share a single interface for improvement suggestions, inspections and asset tracking.

## Features

### Role-based accounts
* Custom `CustomUser` model with **worker** and **manager** roles, plus optional profile images.
* Manager registration requires a secret key.

### Improvement suggestions
* Workers submit suggestions and vote "yes" or "no" on other proposals.
* Managers update the status of each suggestion to *in process*, *approved* or *rejected*.

### Inspection scheduler
* Managers create inspections with due dates and track how many days remain.
* Completed inspections are archived for later review.

### Factory registry
* Simple CRUD pages for departments and machines owned by each department.

## Technology stack
* Python 3.12
* Django 5.2
* SQLite database (development)
* Bootstrap-powered HTML templates

## Getting started
1. Clone the repository
   ```bash
   git clone https://github.com/YOUR_USERNAME/factory-app.git
   cd factory-app
   ```
2. Create a virtual environment and install dependencies
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Apply database migrations
   ```bash
   python manage.py migrate
   ```
4. Run the development server
   ```bash
   python manage.py runserver
   ```

## Environment variables
Define the following settings in a `.env` file or the environment before running the project:

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Set to `True` to enable debug mode (development only) |
| `MANAGER_SECRET_KEY` | Required when registering a manager account |

## Running tests
```bash
python manage.py test
```

## Project structure
```
accounts/      – custom user model and authentication forms
suggestions/   – suggestion submission and voting logic
inspections/   – scheduling and tracking of inspections
common/        – departments, machines and shared views
config/        – Django project configuration
```

## License
This repository is provided for educational purposes and is not intended for production use.
