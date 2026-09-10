import os
import uuid

import razorpay
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


load_dotenv()

app = FastAPI(title="Razorpay Test Store")

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


# Razorpay client
razorpay_client = razorpay.Client(
    auth=(
        os.getenv("RAZORPAY_KEY_ID"),
        os.getenv("RAZORPAY_KEY_SECRET")
    )
)


# Data received from frontend
class CreateOrderRequest(BaseModel):
    amount: float
    currency: str


# Payment verification model
class PaymentVerification(BaseModel):
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str


# -------------------------
# WEB PAGES
# -------------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@app.get("/payment", response_class=HTMLResponse)
def payment(request: Request):
    return templates.TemplateResponse(
        "payment.html",
        {
            "request": request,
            "key_id": os.getenv("RAZORPAY_KEY_ID")
        }
    )


@app.get("/success", response_class=HTMLResponse)
def success(request: Request):
    return templates.TemplateResponse(
        "success.html",
        {
            "request": request
        }
    )


@app.get("/failed", response_class=HTMLResponse)
def failed(request: Request):
    return templates.TemplateResponse(
        "failed.html",
        {
            "request": request
        }
    )


# -------------------------
# CREATE RAZORPAY ORDER
# -------------------------

@app.post("/create-order")
def create_order(order_data:CreateOrderRequest):

    # Razorpay expects amount in paise
    amount_paise = int(order_data.amount * 100)

    razorpay_order_data = {
        "amount": amount_paise,
        "currency": order_data.currency,
        "receipt": f"receipt_{uuid.uuid4().hex[:10]}"
    }

    try:
        razorpay_order = razorpay_client.order.create(razorpay_order_data)

        return {
            "order_id": razorpay_order["id"],
            "amount": amount_paise,
            "currency": order_data.currency,
            "key_id": os.getenv("RAZORPAY_KEY_ID")
        }

    except Exception as e:
        print("Error creating razorpay order:", e)

        raise HTTPException(
            status_code=500,
            detail="Unable to create Razorpay order"
        )


# -------------------------
# VERIFY PAYMENT
# -------------------------

@app.post("/verify-payment")
def verify_payment(payment_data: PaymentVerification):

    try:

        razorpay_client.utility.verify_payment_signature(
            {
                "razorpay_order_id": payment_data.razorpay_order_id,
                "razorpay_payment_id": payment_data.razorpay_payment_id,
                "razorpay_signature": payment_data.razorpay_signature
            }
        )

        return {
            "status": "success",
            "message": "Payment verified successfully",
            "payment_id": payment_data.razorpay_payment_id,
            "order_id": payment_data.razorpay_order_id
        }

    except Exception as e:

        print("Payment verification error:", e)

        raise HTTPException(
            status_code=400,
            detail="Payment verification failed"
        )