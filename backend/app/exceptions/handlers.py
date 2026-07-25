import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.base import AppException

logger = logging.getLogger(__name__)

async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
    
    logger.warning(exc.message,
                   extra = {
                       "request_id": request.scope.get("request_id"),
                       "error_code": exc.error_code,
                       "path": request.url.path
                   })
    
    return JSONResponse(status_code = exc.status_code,
                        content = {
                            "error": {
                                "code": exc.error_code,
                                "message": exc.message
                            }
                        })

async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    
    logger.exception("Unhandles Exception",
                     extra = {
                         "request_id": request.scope.get("request_id"),
                         "path": request.url.path
                     })
    
    return JSONResponse(status_code = 500,
                        content = {
                            "error": {
                                "code": "INTERNAL_SERVER_ERROR",
                                "message": "An unexpected error occurred"
                            }
                        })

def register_exception_handlers(app: FastAPI) -> None:
    
    app.add_exception_handler(AppException, app_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)