from sqlalchemy import exists, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from source.app.users.enums import Roles
from source.app.users.models import User
from source.app.users.schemas import UserCreate
from source.core.database import SessionLocal
from source.core.settings import settings


async def create_admin(db: AsyncSession = SessionLocal()):
    admin_user = User(
        **UserCreate(
            username=settings.ADMIN_USERNAME,
            password=settings.ADMIN_PASSWORD,
            email=settings.ADMIN_EMAIL,
            role=Roles.ADMIN,
        ).model_dump()
    )
    try:
        if not await db.scalar(select(exists().where(User.role == Roles.ADMIN))):
            db.add(admin_user)
            await db.commit()
            await db.refresh(admin_user)
    except IntegrityError:
        pass
    finally:
        await db.close()
