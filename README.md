# Job Application Web App with Python Django

A Django web application to manage job applications. This project includes a form where users can submit their job application details, which are then stored in the database. 

## Features

- User registration and login
- Job application submission
- Admin panel for managing applications

## Requirements

- Python 3.7 or higher
- Django 3.2 or higher
- sqlite (or another supported database)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Hasan082/Job-Application-Web-App-with-Python-Django.git
cd Job-Application-Web-App-with-Python-Django
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Environment Variables

Create a `.env` file in the root of your project and add the following environment variables:

```ini
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your web browser and go to `http://127.0.0.1:8000` to see the application in action.

## Usage

- Visit the home page to see the job application form.
- Submit the form to send your job application.
- Admins can log in to the admin panel to manage applications.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.
```

### .env File Instructions

Create a `.env` file in the root directory of your project (where `manage.py` is located) and add the following configurations:

```ini
# Django settings
SECRET_KEY=your_secret_key
DEBUG=True  # Set to False in production

# Database settings
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port

# Email settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
```

Replace the placeholder values with your actual configuration settings.

### Loading the .env File in Django

Ensure you have the `python-dotenv` package installed. If not, install it using:

```bash
pip install python-dotenv
```

In your `settings.py` file, add the following code at the top to load the environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'False') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

This setup ensures that your sensitive information remains secure and configurable via environment variables.