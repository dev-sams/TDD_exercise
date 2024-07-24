# tdd_exercise

## Technologies
- Python 3.6
- Django 2.3


## Running Locally

### First Time Setup
1. Clone the repo cd into directory
2. Create virtual environment: `python -m venv venv`
3. Run: `source venv/bin/activate`
4. Run requirements: `pip install -r requirements.txt`
5. Create an admin user for logging into the Django admin interface: `python manage.py createsuperuser`


### Running the App

1. Make sure you are already in your virtual environment: `source venv/bin/activate`
2. Run the app: `python manage.py runserver`
3. View the project at http://localhost:8000 and the admin interface at http://localhost:8000/admin


### Running the Test Case
1. Run `python manage.py test` to run the test cases