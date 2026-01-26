from fastapi import FastAPI
from core.config import Base, engine
from app.auth.router import router as auth_router
from app.billing.router import router as billing_router
from app.signals.router import router as signals_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Trading signals SaaS")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(signals_router, prefix="/signals", tags=["Signals"])
app.include_router(billing_router, prefix="/billing", tags=["Billing"])


@app.get("/")
def hello():
    return {"message":"appi running"}