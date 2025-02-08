# **ALX Travel App - Milestone 4: Payment Integration with Chapa API**

## **Overview**
This project is a Django-based web application designed to handle bookings for a travel app, integrating the Chapa API for secure payment processing. It allows users to make bookings and process payments via the Chapa API, with a payment workflow that includes initiation, verification, and confirmation.

---

## **Features**
- Integration of the **Chapa API** for payment processing
- Ability to create bookings and initiate payments
- Verification of payment status
- Background email notifications using **Celery**
- Secure handling of payment data via environment variables
- Payment status tracking in the database

---

## **Technologies Used**
- **Django** - Web framework
- **Celery** - Asynchronous task queue
- **Redis** - Message broker for Celery
- **Chapa API** - Payment gateway for transactions
- **Python** - Backend language
- **PostgreSQL** (or your choice of database) - Database for storing application data

---

## **Setup Instructions**

### **1. Clone the Repository**

```sh
git clone https://github.com/yourusername/alx_travel_app_0x02.git
cd alx_travel_app_0x02/alx_travel_app
```

### **2. Install Dependencies**

Make sure you're using a virtual environment. If you don’t have one set up, you can create one:

```sh
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows (Git Bash)
```

Then, install the necessary dependencies:

```sh
pip install -r requirements.txt
```

### **3. Set Up Environment Variables**

Create a `.env` file in the root of the project and add your Chapa API credentials:

```sh
CHAPA_SECRET_KEY=your_chapa_secret_key
```

You can obtain the API keys by creating an account on the [Chapa Developer Portal](https://developer.chapa.co/).

### **4. Migrate Database**

Ensure your database is set up and migrate any pending changes:

```sh
python manage.py migrate
```

### **5. Start Redis Server**

Redis is required for Celery to function. If you're using WSL, you can start the Redis server using:

```sh
redis-server
```

Alternatively, use your operating system’s native method to start Redis.

### **6. Run Celery Worker**

In a new terminal window (preferably in WSL or your preferred terminal), run the Celery worker:

```sh
celery -A alx_travel_app worker --loglevel=info
```

This will start processing background tasks, such as sending email notifications.

### **7. Run the Django Development Server**

Now you can run the development server:

```sh
python manage.py runserver
```

You should be able to access the app at `http://127.0.0.1:8000/` in your browser.

---

## **How It Works**

1. **Payment Integration**:
   - Users can make bookings through the app.
   - Once a booking is created, the system initiates the payment process via the Chapa API.
   - The payment status is verified after the user completes the payment, and the database is updated accordingly (e.g., `Pending`, `Completed`, `Failed`).

2. **Email Notifications**:
   - On successful payment, a confirmation email is sent to the user using Celery as the background task queue.
   - You can view the emails and monitor their status from the Django admin panel or logs.

---

## **Testing the Integration**

1. **Chapa Sandbox**:  
   - Use the **Chapa sandbox environment** for testing payment initiation and verification.
   - Ensure the transaction IDs are recorded and payments are correctly verified.

2. **Logs**:  
   - Logs for the Celery worker will be printed in the terminal where you started the worker. You can monitor task completion, errors, and email status here.

---

## **Troubleshooting**

1. **Redis not found**:
   - Make sure Redis is installed and running. You can use WSL to ensure it's working if you’re on Windows.

2. **Celery Worker Issues**:
   - Ensure Celery is correctly installed and configured. You might need to use the correct Django app name in place of `alx_travel_app` when running the Celery worker.
   - Use `celery -A your_project_name worker --loglevel=info`.

3. **Chapa Payment Failures**:
   - Check your Chapa credentials and ensure they are correctly set in the `.env` file.
   - Use the Chapa sandbox environment to test transactions without real money being involved.

---

