from uuid import uuid4

from fastapi import Request
from starlette.types import ASGIApp

class RequestIDMiddleware:
    
    #Unique ID assigner middleware for incoming requests, returned in response header
    
    def __init__(self, app: ASGIApp):
        self.app = app
    
    async def __call__(self, scope, receive, send):
        
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        
        request_id = str(uuid4())
        scope["request_id"] = request_id
        
        async def send_wrapper(message):
            
            if message["type"] == "http.response.start":
                
                headers = list(message.get("headers", []))
                headers.append(
                    (b"x-request-id", request_id.encode("utf-8"))
                )
                
                message["headers"] = headers
            
            await send(message)
        
        await self.app(scope, receive, send_wrapper)