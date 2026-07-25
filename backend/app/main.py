from fastapi import FastAPI

from app.api.router import api_router 
from app.core.config import settings
from app.core.logging import configure_logging

import logging

configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
    debug = settings.debug
)

logger.info("Polaris Terminal application initialized")

app.include_router(api_router)