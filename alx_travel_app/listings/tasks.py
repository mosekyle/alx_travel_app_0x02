from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_payment_confirmation_email(booking_reference):
    subject = "Payment Confirmation"
    message = f"Your payment for booking {booking_reference} has been successfully processed."
    recipient_email = "user@example.com"

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [recipient_email],
        fail_silently=False,
    )

