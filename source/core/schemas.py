from typing import Any

from fastapi import HTTPException, status
from pydantic import BaseModel, Field, ValidationError
from pydantic.config import ConfigDict


class ResponseSchema(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)


class PageSchema(BaseModel):
    page: int
    size: int
    total: int
    pages: int


class PaginationSchema(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=50, ge=1)

    def __init__(self, **data: Any) -> None:
        try:
            super(PaginationSchema, self).__init__(**data)
        except ValidationError as error:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=error.errors(),
            )


class ExceptionSchema(BaseModel):
    detail: str


class HealthSchema(BaseModel):
    api: bool
    database: bool
