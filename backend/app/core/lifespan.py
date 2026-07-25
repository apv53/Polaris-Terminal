from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    
    #Application startup and shutdown lifecycle
    
    #Startup
    logger.info("Starting backend ...")
    
    yield
    
    #Shutdown
    logger.info("Shutting down backend ...")