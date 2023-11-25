from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from source.app.auth.schemas import Credentials, Refresh, Token
from source.app.auth.services import (
    authenticate_refresh_token,
    authenticate_user,
    generate_token,
)
from source.core.database import get_db
from source.core.exceptions import unauthorized
from source.core.schemas import ExceptionSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post(
    "/token",
    response_model=Token,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema}},
)
async def token(credentials: Credentials, db: AsyncSession = Depends(get_db)) -> dict:
    if user := await authenticate_user(
        username=credentials.username,
        password=credentials.password,
        db=db,
    ):
        return await generate_token(
            user_id=user.id, password_timestamp=user.password_timestamp
        )
    return unauthorized("Incorrect username or password")


@auth_router.post(
    "/refresh",
    response_model=Token,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema}},
)
async def refresh(request: Refresh, db: AsyncSession = Depends(get_db)) -> dict:
    if new_token := await authenticate_refresh_token(
        token=request.refresh_token, db=db
    ):
        return new_token
    return unauthorized("Invalid or expired token")
