from fastapi import FastAPI
 
from app.core.config import settings
from app.core.logging import configure_logging
from app.core.lifespan import lifespan
from app.core.setup import initialize_app

import logging

configure_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title = settings.app_name,
    version = settings.app_version,
    lifespan = lifespan,
    debug = settings.debug,
    docs_url = "/docs",
    redoc_url = "/redoc"
)

initialize_app(app)

logger.info(f"{settings.app_name} application initialized")
