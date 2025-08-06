# 🏭 FactoryApp

FactoryApp is a Django-based platform for managing day-to-day factory activity. Workers and managers share a single interface for improvement suggestions, inspections, and asset tracking.

---

## ✅ Features

### 🔐 Role-based user accounts
- Custom `CustomUser` model provides distinct **worker** and **manager** roles, with optional profile images.
- Manager registration is gated by a secret key (`S0FTUNI-SECRET`) for added security.

### 💡 Improvement suggestion workflow
- Workers submit suggestions and vote “yes” or “no” on others.
- Managers update each suggestion’s status to *in process*, *approved*, or *rejected*.
- Suggestions cannot be edited after publishing, but can be deleted.

### 🛡️ Inspection scheduler
- Managers create inspection tasks with due dates.
- Tracks how many days remain until each inspection is due.
- Uses color indicators:
  - 🟢 Enough time
  - 🟠 Near deadline
  - 🔴 Overdue
- Completed inspections are archived for review.

### 🏭 Factory registry
- Two separate models: `Department` and `Machine`.
- Managers use simple CRUD interfaces to maintain a list of departments and assign machines to each one.
- Enables basic asset tracking and reflects the actual structure of factory floors.

---

## 🧰 Technology stack

### Core technologies
- Python 3.12
- Django 5.2
- SQLite (for development)
- Bootstrap-powered HTML templates
-- `python-dotenv` for automatic loading of environment variables from a `.env` file

### Python dependencies
- Django 5.2.4
- asgiref
- sqlparse
- tzdata

All dependencies are listed in `requirements.txt`.

---

## ⚙️ Getting started

1. **Clone the repository**
   git clone https://github.com/stanchev-dev/factory-app.git
   cd factory-app

## Getting started
1. Clone the repository
   
   git clone https://github.com/stanchev-dev/factory-app.git
   cd factory-app
   
2. Create a virtual environment and install dependencies
   
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   
 3. Create a .env file with the following:
  SECRET_KEY=your-secret-key
  DEBUG=True
  DATABASE_NAME=db.sqlite3

4. Apply database migrations
   
   python manage.py migrate
   
5. Run the development server
   
   python manage.py runserver
   

## 🎓 Project Purpose
FactoryApp was developed as an educational final project to demonstrate advanced Django concepts in a real-world scenario. The application simulates an internal factory management system, showcasing role-based authentication, user-driven suggestions, inspection scheduling, and asset tracking. It serves as a full-stack example of how Django can be used to build secure, modular, and scalable internal tools for organizations.

## 📬 Contact
Questions or feedback? Open a GitHub Issue or get in touch through the repository:
🔗 https://github.com/stanchev-dev/factory-app

## License
This repository is provided for educational purposes and is not intended for production use.

