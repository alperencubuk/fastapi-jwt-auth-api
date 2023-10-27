from pydantic import BaseModel, Field
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
    size: int = Field(default=50, ge=0)


class ExceptionSchema(BaseModel):
    detail: str


class HealthSchema(BaseModel):
    api: bool
    database: bool
