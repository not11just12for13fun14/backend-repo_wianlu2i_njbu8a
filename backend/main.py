from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Microplastic Hub API", version="1.0.0")

frontend_url = os.getenv("FRONTEND_URL", "*")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url] if frontend_url != "*" else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Microplastic Hub API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/test")
def test():
    return {"ok": True, "note": "Database not used for this static site."}
