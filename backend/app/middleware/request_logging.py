import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request: Request, call_next):
        
        start_time = time.perf_counter()
        response = await call_next(request)
        duration = (time.perf_counter() - start_time) * 1000
        
        logger.info("HTTP Request", 
                    extra = {
                        "request_id": request.scope.get("request_id"),
                        "method": request.method,
                        "path": request.url.path,
                        "status_code": response.status_code,
                        "duration_ms": round(duration, 2),
                        "client": request.client.host if request.client else None
                    })
        
        return response