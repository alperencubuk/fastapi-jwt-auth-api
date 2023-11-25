from math import ceil

from sqlalchemy import asc, desc, func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from source.app.users.enums import Order, Sort
from source.app.users.models import User
from source.app.users.schemas import (
    UserCreate,
    UserPage,
    UserRequest,
    UserUpdate,
    UserUpdateRequest,
)


async def create_user(user: UserRequest, db: AsyncSession) -> User | None:
    try:
        user = User(**UserCreate(**user.model_dump()).model_dump())
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    except IntegrityError:
        return None


async def update_user(
    user: User,
    request: UserUpdateRequest,
    db: AsyncSession,
) -> User | None:
    try:
        fields_to_update = UserUpdate(**request.model_dump()).model_dump().items()
        for key, value in fields_to_update:
            if value is not None:
                setattr(user, key, value)
        await db.commit()
        await db.refresh(user)
        return user
    except IntegrityError:
        return None


async def delete_user(user: User, db: AsyncSession) -> None:
    await db.delete(user)
    await db.commit()
    return None


async def list_users(
    page: int, size: int, sort: Sort, order: Order, db: AsyncSession
) -> UserPage:
    order = asc(sort) if order == Order.ASC else desc(sort)

    users = await db.scalars(
        select(User).order_by(order).offset((page - 1) * size).limit(size)
    )
    total = await db.scalar(select(func.count(User.id)))

    return UserPage(
        users=users,
        page=page,
        size=size,
        total=total,
        pages=(ceil(total / size)),
    )
