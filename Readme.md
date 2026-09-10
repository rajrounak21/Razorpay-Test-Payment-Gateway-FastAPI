# Razorpay FastAPI Payment Gateway

[![GitHub](https://img.shields.io/badge/GitHub-Razorpay--FastAPI-181717?style=for-the-badge\&logo=github)](https://github.com/rajrounak21/razorpay-fastapi-payment-demo)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat\&logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)
[![Razorpay](https://img.shields.io/badge/Razorpay-Test%20Mode-0C2451?style=flat\&logo=razorpay\&logoColor=white)](https://razorpay.com/docs/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat\&logo=python\&logoColor=white)](https://www.python.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat\&logo=html5\&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat\&logo=css3\&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat\&logo=javascript\&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](./LICENSE)

A clean and minimal **Razorpay Test Mode payment integration** built with **Python, FastAPI, HTML, CSS, and JavaScript**.

This project demonstrates the complete payment flow — from creating a Razorpay order to opening the Razorpay Checkout and verifying the payment signature on the backend.

---

## Features

* Razorpay Test Mode integration
* FastAPI backend
* Backend payment signature verification
* Simple single-product checkout
* Razorpay Checkout integration
* Frontend-to-backend payment flow
* Modern responsive UI
* Payment loading states
* Payment success page
* Payment failure/cancel handling
* Environment-based API credentials
* Clean and simple project structure

---

## Application Flow

```text
                    ┌───────────────────┐
                    │    Product Page   │
                    │       ₹200        │
                    └─────────┬─────────┘
                              │
                           Buy Now
                              │
                              ▼
                    ┌───────────────────┐
                    │  FastAPI Backend  │
                    │   Create Order    │
                    └─────────┬─────────┘
                              │
                         Razorpay
                         Order ID
                              │
                              ▼
                    ┌───────────────────┐
                    │   Payment Page    │
                    │ Razorpay Checkout │
                    └─────────┬─────────┘
                              │
                           Payment
                              │
                              ▼
                    ┌───────────────────┐
                    │ Razorpay Checkout │
                    └─────────┬─────────┘
                              │
                    Payment Response
                              │
                              ▼
                    ┌───────────────────┐
                    │  FastAPI Backend  │
                    │ Verify Signature  │
                    └─────────┬─────────┘
                              │
                       ┌──────┴──────┐
                       ▼             ▼
                    Success        Failed
```

---

## Payment Lifecycle

### 1. Create Order

When the user clicks **Buy Now**, the frontend sends the product amount and currency to:

```http
POST /create-order
```

The FastAPI backend creates an order through Razorpay.

```text
Frontend
   ↓
POST /create-order
   ↓
FastAPI
   ↓
Razorpay API
   ↓
Razorpay Order ID
```

---

### 2. Open Checkout

The generated Razorpay Order ID is passed to the payment page.

```text
/payment?order_id=order_xxxxx
```

The frontend reads the order ID from the URL and opens Razorpay Checkout.

---

### 3. Complete Payment

Razorpay Checkout handles the payment interface.

The user can complete the test transaction using Razorpay's Test Mode payment details.

---

### 4. Verify Payment

After checkout, Razorpay returns:

```text
razorpay_order_id
razorpay_payment_id
razorpay_signature
```

The frontend sends these values to:

```http
POST /verify-payment
```

The FastAPI backend verifies the Razorpay signature using the Razorpay SDK.

```text
Razorpay Checkout
        ↓
Payment Response
        ↓
Frontend JavaScript
        ↓
FastAPI /verify-payment
        ↓
Signature Verification
        ↓
Valid / Invalid
```

Only after successful verification is the payment treated as successful.

---

## Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Backend programming             |
| FastAPI       | API and web server              |
| Razorpay      | Payment gateway                 |
| HTML5         | Frontend structure              |
| CSS3          | UI and responsive styling       |
| JavaScript    | Checkout and API communication  |
| Jinja2        | HTML template rendering         |
| python-dotenv | Environment variable management |

### Documentation

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Razorpay Documentation](https://razorpay.com/docs/)
* [Razorpay Payment Gateway](https://razorpay.com/payment-gateway/)
* [Python Documentation](https://docs.python.org/3/)

---

## Project Structure

```text
razorpay-fastapi-payment-demo/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── payment.html
│   ├── success.html
│   └── failed.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── payment.js
```

---

## API Endpoints

| Method | Endpoint          | Description                              |
| ------ | ----------------- | ---------------------------------------- |
| `GET`  | `/`               | Displays the product page                |
| `POST` | `/create-order`   | Creates a Razorpay order                 |
| `GET`  | `/payment`        | Displays the checkout page               |
| `POST` | `/verify-payment` | Verifies the payment signature           |
| `GET`  | `/success`        | Displays successful payment result       |
| `GET`  | `/failed`         | Displays failed/cancelled payment result |

---

## Getting Started

### Prerequisites

Make sure you have:

* Python 3.x
* Razorpay Test Mode account
* Razorpay Test API credentials
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/rajrounak21/razorpay-fastapi-payment-demo.git
cd razorpay-fastapi-payment-demo
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
RAZORPAY_KEY_ID=your_test_key_id
RAZORPAY_KEY_SECRET=your_test_secret
```

Use your **Razorpay Test Mode** credentials.

How to Get Credentials Must read **RAZORPAY_TEST_KEYS.md** file

### 5. Start the Application

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Open the URL in your browser and click **Buy Now** to start the payment flow.

---

## Razorpay Test Mode

This project uses **Razorpay Test Mode**, so no real money is charged.

Test Mode allows you to understand and test the complete payment process without making actual transactions.

Use the test payment details provided in the official Razorpay documentation:

[Razorpay Test Payment Details](https://razorpay.com/docs/payments/payments/test-card-upi-details/)

---

## Security

The project separates the Razorpay credentials into two parts.

### Key ID

The Razorpay **Key ID** is required by Razorpay Checkout and can be exposed to the frontend.

### Key Secret

The Razorpay **Key Secret** must remain on the backend.

```text
.env
 │
 ├── RAZORPAY_KEY_ID
 │
 └── RAZORPAY_KEY_SECRET
          │
          └── Backend only
```

The secret should never be placed inside:

* HTML
* JavaScript
* GitHub
* Public API responses
* Frontend source code

---

## What I Learned

This project was built to understand the fundamentals of payment gateway integration.

### Backend

* Creating Razorpay orders
* Working with FastAPI API routes
* Loading credentials using environment variables
* Converting rupees to paise
* Verifying Razorpay payment signatures
* Handling payment errors

### Frontend

* Calling FastAPI APIs using `fetch()`
* Reading query parameters using `URLSearchParams`
* Opening Razorpay Checkout
* Handling successful and failed payments
* Managing loading states
* Redirecting users after payment verification

### Integration

The project demonstrates how a frontend and backend communicate with a third-party payment gateway:

```text
Frontend
   ↕
FastAPI Backend
   ↕
Razorpay
```

---

## Why FastAPI?

FastAPI makes it straightforward to create lightweight backend APIs while providing:

* High performance
* Automatic API documentation
* Type validation with Pydantic
* Simple route definitions
* Easy integration with external APIs and SDKs

This makes it a good choice for small payment demos as well as larger Python applications.

---

## Production Considerations

This project intentionally keeps the implementation simple for learning purposes.

The product amount is sent from the frontend to the backend when creating the Razorpay order.

For a real production application, the backend should **never blindly trust the price sent by the frontend**.

A production implementation should follow a flow such as:

```text
Product ID
    ↓
Frontend
    ↓
Backend
    ↓
Database
    ↓
Fetch Actual Product Price
    ↓
Create Razorpay Order
    ↓
Razorpay Checkout
```

This prevents a user from modifying the price through browser developer tools.

A production application would also typically require additional handling for:

* Order persistence
* Payment status tracking
* Webhooks
* Idempotency
* Refunds
* Database transactions
* Authentication
* Logging and monitoring
* Production Razorpay credentials

These are intentionally outside the scope of this learning project.

---

## Project Goal

The goal of this project is to understand the **core Razorpay payment integration**, not to build a complete e-commerce platform.

The complete concept can be summarized as:

```text
Create Order
     ↓
Open Checkout
     ↓
Complete Payment
     ↓
Receive Payment Details
     ↓
Verify Signature
     ↓
Show Result
```

---

## Project Preview

### Product Page

A simple premium-style product page where the user can start the payment process.

### Checkout

Razorpay Checkout handles the actual payment interface.

### Payment Result

The application displays a dedicated success or failure page after verification.

---

## Important Note

This repository is intended for **educational and testing purposes** and uses Razorpay Test Mode.

Before processing real payments, additional production-level security, validation, database handling, webhook processing, and error handling should be implemented.

---

## Author

### Rounak Raj

**AI & ML Developer | Python | FastAPI | AI/ML**

Portfolio: [rounakraj.online](https://portfolio.rounakraj.online/)

GitHub: [rajrounak21](https://github.com/rajrounak21)

---

## ⭐ Support

If this project helped you understand Razorpay payment integration with FastAPI, consider giving the repository a ⭐.
---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).
