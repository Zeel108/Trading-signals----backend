from fastapi import APIRouter

router = APIRouter()

@router.get("/test1")
def test_signals():
    return {"signals":"ok"}