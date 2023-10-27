from typing import Annotated

from fastapi import Depends

from source.app.auth.services import auth, auth_admin
from source.app.users.models import User

CurrentUser = Annotated[User, Depends(auth)]
Admin = Annotated[User, Depends(auth_admin)]
