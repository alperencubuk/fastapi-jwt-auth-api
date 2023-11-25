from fastapi import HTTPException, status


def bad_request(detail: str) -> HTTPException:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=detail,
    )


def unauthorized(detail: str) -> HTTPException:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )


def forbidden(detail: str) -> HTTPException:
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=detail,
    )


def not_found(detail: str) -> HTTPException:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail,
    )


def conflict(detail: str) -> HTTPException:
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=detail,
    )
