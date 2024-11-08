from fastapi import APIRouter

from api.router.user_router import user_api_router
from api.router.map_router import map_router
api_router = APIRouter()

api_router.include_router(router=user_api_router, prefix="/auth", tags=["auth"])
api_router.include_router(router=map_router, prefix="/map" tags=["map"])