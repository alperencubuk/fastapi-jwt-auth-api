from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from source.app.auth.auth import Admin, CurrentUser
from source.app.users.models import User
from source.app.users.schemas import (
    UserPage,
    UserPagination,
    UserRequest,
    UserResponse,
    UserUpdateRequest,
)
from source.app.users.services import create_user, delete_user, list_users, update_user
from source.core.database import get_db
from source.core.schemas import ExceptionSchema

users_router = APIRouter(prefix="/users")


@users_router.post(
    "/",
    response_model=UserResponse,
    responses={
        status.HTTP_409_CONFLICT: {"model": ExceptionSchema},
    },
    status_code=status.HTTP_201_CREATED,
    tags=["users"],
)
async def user_create(user: UserRequest, db: AsyncSession = Depends(get_db)) -> User:
    if created_user := await create_user(user=user, db=db):
        return created_user
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"User '{user.username}' already exists",
    )


@users_router.get(
    "/",
    response_model=UserResponse,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema}},
    tags=["users"],
)
async def user_get(user: CurrentUser) -> User:
    return user


@users_router.patch(
    "/",
    response_model=UserResponse,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema},
        status.HTTP_409_CONFLICT: {"model": ExceptionSchema},
    },
    tags=["users"],
)
async def user_update(
    user: CurrentUser,
    request: UserUpdateRequest,
    db: AsyncSession = Depends(get_db),
) -> User:
    if updated_user := await update_user(user=user, request=request, db=db):
        return updated_user
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"User '{request.username}' already exists",
    )


@users_router.delete(
    "/",
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema}},
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["users"],
)
async def user_delete(user: CurrentUser, db: AsyncSession = Depends(get_db)) -> None:
    await delete_user(user=user, db=db)
    return None


@users_router.get(
    "/admin",
    response_model=UserPage,
    responses={status.HTTP_401_UNAUTHORIZED: {"model": ExceptionSchema}},
    tags=["admin"],
)
async def users_list(
    user: Admin,
    pagination: UserPagination = Depends(),
    db: AsyncSession = Depends(get_db),
) -> UserPage:
    return await list_users(
        page=pagination.page,
        size=pagination.size,
        sort=pagination.sort,
        order=pagination.order,
        db=db,
    )
