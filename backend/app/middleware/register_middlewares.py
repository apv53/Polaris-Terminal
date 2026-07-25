from fastapi import FastAPI

from app.middleware.request_id import RequestIDMiddleware
from app.middleware.request_logging import RequestLoggingMiddleware

def register_middlewares(app: FastAPI) -> None:
    
    app.add_middleware(RequestIDMiddleware)
    app.add_middleware(RequestLoggingMiddleware)