from fastapi import HTTPException, status
from core.redis_client import redis_client
from time import time

RATE_LIMIT = 20      # requests
WINDOW = 60          # seconds

def rate_limit(user_id: int, route: str):
    key = f"rate:{user_id}:{route}"
    current = redis_client.get(key)

    if current and int(current) >= RATE_LIMIT:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests, slow down"
        )

    if not current:
        redis_client.setex(key, WINDOW, 1)
    else:
        redis_client.incr(key)
