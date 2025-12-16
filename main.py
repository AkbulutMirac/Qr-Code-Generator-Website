from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import router as qr_code_router

app = FastAPI(title="QR Code Generator Service")


# Enable CORS for all origins (you can restrict this in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include API router
app.include_router(qr_code_router, prefix="/api")


app.mount("/", StaticFiles(directory="static", html=True), name="static")