const params = new URLSearchParams(window.location.search);

const orderId = params.get("order_id");

const payButton = document.getElementById("pay-button");


function showError(message) {

    alert(message);

    payButton.disabled = false;

    payButton.querySelector("span:first-child").textContent =
        `Pay ₹${PRODUCT_PRICE}`;

}


/*
 * Open Razorpay Checkout
 */
function payNow() {

    if (!orderId) {

        showError("Payment order was not found.");

        return;
    }


    payButton.disabled = true;

    payButton.querySelector("span:first-child").textContent =
        "Opening checkout...";


    const options = {

        key: RAZORPAY_KEY,

        amount: PRODUCT_PRICE * 100,

        currency: "INR",

        name: "PayFlow",

        description: PRODUCT_NAME,

        order_id: orderId,


        handler: async function (response) {

            payButton.querySelector("span:first-child").textContent =
                "Verifying payment...";


            try {

                const verificationResponse = await fetch(
                    "/verify-payment",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type": "application/json"
                        },

                        body: JSON.stringify({

                            razorpay_order_id:
                                response.razorpay_order_id,

                            razorpay_payment_id:
                                response.razorpay_payment_id,

                            razorpay_signature:
                                response.razorpay_signature

                        })
                    }
                );


                const result =
                    await verificationResponse.json();


                if (verificationResponse.ok &&
                    result.status === "success") {

                    window.location.href = "/success";

                } else {

                    window.location.href = "/failed";

                }


            } catch (error) {

                console.error(
                    "Verification error:",
                    error
                );

                window.location.href = "/failed";

            }

        },


        modal: {

            ondismiss: function () {

                payButton.disabled = false;

                payButton.querySelector(
                    "span:first-child"
                ).textContent =
                    `Pay ₹${PRODUCT_PRICE}`;

            }

        }

    };


    const razorpay = new Razorpay(options);


    razorpay.on(
        "payment.failed",
        function (response) {

            console.error(
                "Payment failed:",
                response.error
            );

            window.location.href = "/failed";

        }
    );


    razorpay.open();

}