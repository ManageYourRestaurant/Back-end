from fastapi import APIRouter
from api.handler.map.restorant import restorant_router


map_router = APIRouter()

map_router.include_router(router=restorant_router, prefix="/restorant")
