from pydantic import BaseModel

class HealthResponse(BaseModel):
    service: str
    version: str
    environment: str
    status: str

class ReadinessResponse(BaseModel):
    status: str
    database: str

class LivenessResponse(BaseModel):
    status: str