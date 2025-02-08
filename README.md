# ALX Travel App

A Django-based travel listing platform that allows users to browse listings and make bookings. This project uses Django REST Framework to provide API endpoints for managing listings and bookings. It also integrates Swagger for API documentation.

## Project Setup

### Prerequisites

- Python 3.x
- MySQL Database
- Django 3.x
- Django REST Framework
- drf-yasg for Swagger Documentation
- Celery and RabbitMQ (for future background tasks)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/alx_travel_app.git
    cd alx_travel_app
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    Make sure you have MySQL running and configured in the `settings.py` file.

5. Create a `.env` file in the root directory with the following environment variables:

    ```
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=3306
    ```

6. Run migrations to set up the database schema:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

### API Documentation

The API documentation is automatically generated using Swagger and can be accessed at:


### API Endpoints

- **GET /api/listings/** - Retrieve all listings.
- **POST /api/listings/** - Create a new listing.
- **GET /api/bookings/** - Retrieve all bookings.
- **POST /api/bookings/** - Create a new booking.

### Running Tests

To run tests, use the following command:

```bash
python manage.py test

