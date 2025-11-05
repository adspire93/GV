"""
GammaVantage Main Application

FastAPI-based application for WhatsApp F&O trading assistant.

Entry point for the application.
Initializes all services and starts the server.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import logging

from app.core.config import settings
from app.api import whatsapp_webhook, chartink_webhook, payment_webhook, health

# Configure logging
logging.basicConfig(
    level=logging.INFO if not settings.DEBUG else logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="GammaVantage",
    description="WhatsApp-based F&O Trading Assistant",
    version="1.0.0"
)


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup."""
    logger.info("Starting GammaVantage application...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    # TODO: Initialize database connections
    # TODO: Initialize cache connections
    # TODO: Initialize WebSocket connections for real-time data


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    logger.info("Shutting down GammaVantage application...")
    # TODO: Close database connections
    # TODO: Close cache connections
    # TODO: Close WebSocket connections


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "app": "GammaVantage",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    # TODO: Implement actual health check
    return {"status": "healthy"}


@app.post("/webhook/whatsapp")
async def whatsapp_webhook_handler(request: Request):
    """WhatsApp webhook endpoint."""
    # TODO: Implement WhatsApp webhook handling
    return {"status": "received"}


@app.get("/webhook/whatsapp")
async def whatsapp_webhook_verify(request: Request):
    """WhatsApp webhook verification."""
    # TODO: Implement webhook verification
    return {"status": "verified"}


@app.post("/webhook/chartink")
async def chartink_webhook_handler(request: Request):
    """Chartink screener webhook endpoint."""
    # TODO: Implement Chartink webhook handling
    return {"status": "received"}


@app.post("/webhook/payment")
async def payment_webhook_handler(request: Request):
    """Payment gateway webhook endpoint."""
    # TODO: Implement payment webhook handling
    return {"status": "received"}


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler."""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )


if __name__ == "__main__":
    """Run the application."""
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info"
    )
