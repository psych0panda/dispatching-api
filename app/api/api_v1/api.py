from fastapi import APIRouter

from app.api.api_v1.endpoints import heat_meter_reading, users, auth

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(heat_meter_reading.router, prefix="/heat_meter_reading", tags=["heat-meter-reading"])
api_router.include_router(users.router, prefix="/users", tags=["users"])

