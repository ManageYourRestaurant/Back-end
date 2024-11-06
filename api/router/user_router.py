from fastapi import APIRouter

from service.user_manager import auth_backend, fastapi_users
from schema.user_schema import UserCreate, UserRead, UserUpdate

user_api_router = APIRouter()
user_api_router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt")
user_api_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/register")
user_api_router.include_router(fastapi_users.get_reset_password_router(), prefix="/change_password")
user_api_router.include_router(fastapi_users.get_verify_router(UserRead), prefix="/verify")
user_api_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users")
