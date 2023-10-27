from fastapi import APIRouter

from source.app.auth.views import auth_router
from source.app.users.views import users_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(users_router)
