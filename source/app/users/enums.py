from enum import Enum


class Roles(str, Enum):
    ADMIN = "admin"
    USER = "user"


class Sort(str, Enum):
    ID = "id"
    USERNAME = "username"
    CREATE_DATE = "create_date"
    UPDATE_DATE = "update_date"


class Order(str, Enum):
    ASC = "asc"
    DESC = "desc"
