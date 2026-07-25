from fastapi import FastAPI

from app.api.register_routes import register_routes
from app.exceptions.handlers import register_exception_handlers
from app.middleware.register_middlewares import register_middlewares

def initialize_app(app: FastAPI) -> None:
    
    register_middlewares(app)
    register_exception_handlers(app)
    register_routes(app)