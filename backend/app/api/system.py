from fastapi import APIRouter, Depends

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.api.deps import get_db
from app.schemas.system import HealthResponse, ReadinessResponse, LivenessResponse

import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags = ["System"])

@router.get("/")
async def root():
    
    logger.info("Root endpoint accessed")
    
    return{
        "name" : settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_environment,
        "status": "working"
    }

@router.get("/live", response_model = LivenessResponse)
async def live():    
    return {"status": "alive"}

@router.get("/ready", response_model = ReadinessResponse)
async def ready(db: AsyncSession = Depends(get_db)):
    
    await db.execute(text("SELECT 1"))
    
    return {"status": "ready", "database": "connected"}

@router.get("/health", response_model = HealthResponse)
async def health():
    
    return{
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_environment,
        "status": "healthy"
    }