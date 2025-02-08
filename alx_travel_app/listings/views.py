from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    serializer_class = ListingSerializer
import os
import requests
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
from .tasks import send_payment_confirmation_email  # Celery task

CHAPA_SECRET_KEY = os.getenv("CHAPA_SECRET_KEY")
CHAPA_BASE_URL = "https://api.chapa.co/v1/transaction"

@csrf_exempt
def initiate_payment(request):
    if request.method == "POST":
        data = request.POST
        booking_reference = data.get("booking_reference")
        amount = data.get("amount")

        if not booking_reference or not amount:
            return JsonResponse({"error": "Missing required fields"}, status=400)

        headers = {
            "Authorization": f"Bearer {CHAPA_SECRET_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "amount": amount,
            "currency": "ETB",
            "email": "user@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "tx_ref": booking_reference,
            "callback_url": "http://127.0.0.1:8000/api/verify-payment/",
            "return_url": "http://127.0.0.1:8000/payment-success/",
            "customization[title]": "Booking Payment"
        }

        response = requests.post(f"{CHAPA_BASE_URL}/initialize", json=payload, headers=headers)
        res_data = response.json()

        if response.status_code == 200:
            transaction_id = res_data["data"]["tx_ref"]
            Payment.objects.create(
                booking_reference=booking_reference,
                transaction_id=transaction_id,
                amount=amount,
                status="Pending"
            )
            return JsonResponse({"payment_url": res_data["data"]["checkout_url"]})

        return JsonResponse({"error": res_data.get("message", "Payment initiation failed")}, status=400)


@csrf_exempt
def verify_payment(request):
    if request.method == "GET":
        transaction_id = request.GET.get("transaction_id")

        if not transaction_id:
            return JsonResponse({"error": "Transaction ID is required"}, status=400)

        headers = {"Authorization": f"Bearer {CHAPA_SECRET_KEY}"}
        response = requests.get(f"{CHAPA_BASE_URL}/verify/{transaction_id}", headers=headers)
        res_data = response.json()

        if response.status_code == 200 and res_data["data"]["status"] == "success":
            payment = get_object_or_404(Payment, transaction_id=transaction_id)
            payment.status = "Completed"
            payment.save()

            # Send email using Celery
            send_payment_confirmation_email.delay(payment.booking_reference)

            return JsonResponse({"message": "Payment successful", "status": "Completed"})

        return JsonResponse({"error": "Payment verification failed"}, status=400)

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
views.py[+] [dos] (07:09 08/02/2025)                                                                                                                                                    12,1 Bot
-- INSERT --

