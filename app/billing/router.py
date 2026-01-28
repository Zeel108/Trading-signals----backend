import os
import stripe
from fastapi import APIRouter, Depends, Request, HTTPException
from dotenv import load_dotenv
from app.auth.dependency import get_current_user
from core.config import SessionLocal
from app.models import User
from core.redis_client import redis_client
from sqlalchemy.orm import Session
import json

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
FRONTEND_URL = os.getenv("FRONTEND_URL")

router = APIRouter()

@router.post("/create-checkout")
def create_checkout(current_user: User = Depends(get_current_user)):
    print("USER ID:", current_user.id)
    print("EMAIL:", current_user.email)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[{
            "price_data": {
                "currency": "inr",
                "product_data": {"name": "Trading Signals Plan"},
                "unit_amount": 49900,
            },
            "quantity": 1,
        }],
        success_url=f"{FRONTEND_URL}success",
        cancel_url=f"{FRONTEND_URL}cancel",
        metadata={
            "user_id": str(current_user.id),
            "email": current_user.email      }
    )

    return {"checkout_url": session.url}


@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

    try:
        # Only construct event if you have a real Stripe signature
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except Exception as e:
        # For manual Postman testing, you can skip signature verification
        event = json.loads(payload)
        print("No valid signature, using raw payload for testing")

    print("WEBHOOK HIT!")
    print("EVENT TYPE:", event.get("type"))

    # Handle only checkout.session.completed
    if event.get("type") == "checkout.session.completed":
        session = event["data"]["object"]
        print("WEBHOOK METADATA:", session.get("metadata"))

        user_id = session.get("metadata", {}).get("user_id")
        if user_id:
            db = SessionLocal()
            user = db.query(User).filter(User.id == int(user_id)).first()
            if user:
                user.is_paid = True
                db.commit()
            db.close()

    return {"status": "success"}
