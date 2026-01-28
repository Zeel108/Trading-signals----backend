from fastapi import APIRouter, Depends
from app.auth.dependency import get_current_user
from core.redis_client import redis_client
from app.signals.zerodha_mock import fetch_zerodha_signals
import json

router = APIRouter()

@router.get("/")
def get_signals(user=Depends(get_current_user)):
    cache_key = "zerodha_signals"

    cached = redis_client.get(cache_key)
    if cached:
        signals = json.loads(cached)
    else:
        signals = fetch_zerodha_signals()
        redis_client.setex(cache_key, 300, json.dumps(signals))  # 5 min TTL

    if not user.is_paid:
        return signals[:1]   # free user sees only 1 signal

    return signals
