from fastapi import APIRouter, Depends
from core.redis_client import redis_client
from app.auth.dependency import get_current_user
import json
from app.signals.zerodha_mock import generate_zerodha_signals

router = APIRouter(
    prefix="/signals",
    tags=["signals"]
)

@router.get("/")
def get_signals(user=Depends(get_current_user)):
    """
    Returns Zerodha-like stock signals.
    - Free users: see only 1 stock
    - Paid users: see all 30 stocks
    - Cached in Redis for 5 minutes
    """
    cache_key = "zerodha_signals"
    cached = redis_client.get(cache_key)

    if cached:
        signals = json.loads(cached)
    else:
        signals = generate_zerodha_signals()
        redis_client.setex(cache_key, 300, json.dumps(signals))  # cache for 5 min

    # Free users see only 1 stock
    if not user.is_paid:
        return signals[:1]

    return signals
