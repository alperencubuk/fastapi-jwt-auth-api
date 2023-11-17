from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, model_validator

from source.app.auth.utils import get_password_hash
from source.app.users.enums import Order, Roles, Sort
from source.core.schemas import PageSchema, PaginationSchema, ResponseSchema


class UserRequest(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None


class UserCreate(UserRequest):
    active: bool = True
    role: Roles = Roles.USER
    password_timestamp: float = Field(default_factory=datetime.utcnow().timestamp)

    @model_validator(mode="after")
    def validator(cls, values: "UserCreate") -> "UserCreate":
        values.password = get_password_hash(values.password)
        return values


class UserResponse(ResponseSchema):
    username: str
    email: EmailStr
    first_name: str | None
    last_name: str | None
    active: bool
    role: Roles
    create_date: datetime
    update_date: datetime


class UserUpdateRequest(BaseModel):
    username: str | None = None
    password: str | None = None
    email: EmailStr | None = None
    first_name: str | None = None
    last_name: str | None = None


class UserUpdateRequestAdmin(UserUpdateRequest):
    active: bool | None = None
    role: Roles | None = None


class UserUpdate(UserUpdateRequestAdmin):
    password_timestamp: float | None = None

    @model_validator(mode="after")
    def validator(cls, values: "UserUpdate") -> "UserUpdate":
        if password := values.password:
            values.password = get_password_hash(password)
            values.password_timestamp = datetime.utcnow().timestamp()
        return values


class UserPage(PageSchema):
    users: list[UserResponse]


class UserPagination(PaginationSchema):
    sort: Sort = Sort.ID
    order: Order = Order.ASC


class UserId(BaseModel):
    user_id: int


class Username(BaseModel):
    username: str
