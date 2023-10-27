from sqlalchemy import Boolean, Column, Float, String

from source.core.models import Model


class User(Model):
    __tablename__ = "User"

    username = Column(name="username", type_=String, unique=True, index=True)
    password = Column(name="password", type_=String)
    email = Column(name="email", type_=String)
    first_name = Column(name="first_name", type_=String, nullable=True)
    last_name = Column(name="last_name", type_=String, nullable=True)
    active = Column(name="active", type_=Boolean)
    role = Column(name="role", type_=String)
    password_timestamp = Column(name="password_timestamp", type_=Float)
