from fastapi import APIRouter

from app.core.config import settings

import logging

logger = logging.getLogger(__name__)

router = APIRouter(tags = ["System"])

@router.get("/")
async def root():
    
    logger.info("Root endpoint accessed")
    
    return{
        "Name" : settings.app_name,
        "Version": settings.app_version,
        "Environment": settings.app_environment,
        "Status": "Working"
    }