# FastAPI JWT Auth API

### Summary:

FastAPI, Postgres, Sqlalchemy, Pydantic v2, Docker
API example with JWT Authentication.

### Requirements:

```
docker
```

### Run:

```
cp config/.env.example config/.env
docker compose up --build
```

### Docs:

```
OpenAPI: http://localhost:8000/docs
Postman: postman_collection.json in the project root.
```

### Endpoints:

```http request
POST   /auth/token                       # token get
POST   /auth/refresh                     # token refresh

POST   /users                            # user create
GET    /users                            # user get
PATCH  /users                            # user update
DELETE /users                            # user delete

GET    /users/admin                      # user list (admin)

GET    /                                 # health check
```

### Example Requests/Responses:

#### Request:
```http request
POST /auth/token

Body:
{
    "username": "user",
    "password": "123456"
}
```

#### Response:
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJwYXNzd29yZF90aW1lc3RhbXAiOjE3MDAyMjc0MTguNTYxMjExLCJleHAiOjE3MDAyMjk3OTAsInRva2VuX3R5cGUiOiJhY2Nlc3MifQ.dQPryffcPZ0Yj2niYp72CukEzbRz-M7_j6WgieiXWHA",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJwYXNzd29yZF90aW1lc3RhbXAiOjE3MDAyMjc0MTguNTYxMjExLCJleHAiOjE3MDI4MTk5OTAsInRva2VuX3R5cGUiOiJyZWZyZXNoIn0.5Dxog4Tl02rOe5ksf4xsU1u8waISGsZTvOGZx1fwltI",
    "token_type": "bearer"
}
```

#### Request:
```http request
GET /users
Headers:
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJwYXNzd29yZF90aW1lc3RhbXAiOjE3MDAyMjc0MTguNTYxMjExLCJleHAiOjE3MDAyMjk3OTAsInRva2VuX3R5cGUiOiJhY2Nlc3MifQ.dQPryffcPZ0Yj2niYp72CukEzbRz-M7_j6WgieiXWHA
```

#### Response:
```json
{
    "id": 1,
    "username": "user",
    "email": "user@test.com",
    "first_name": "fname",
    "last_name": "lname",
    "active": true,
    "role": "user",
    "create_date": "2023-11-17T13:23:45.737500",
    "update_date": "2023-11-17T13:23:45.737500"
}
```

#### Request:
```http request
POST /auth/refresh

{
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJwYXNzd29yZF90aW1lc3RhbXAiOjE3MDAyMjc0MTguNTYxMjExLCJleHAiOjE3MDI4MTk5OTAsInRva2VuX3R5cGUiOiJyZWZyZXNoIn0.5Dxog4Tl02rOe5ksf4xsU1u8waISGsZTvOGZx1fwltI"
}
```

#### Response:
```json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJwYXNzd29yZF90aW1lc3RhbXAiOjE3MDAyMjc0MTguNTYxMjExLCJleHAiOjE3MDAyMzAwOTIsInRva2VuX3R5cGUiOiJhY2Nlc3MifQ.EU2XcjLGw6imlCl3rLYs9pqu0t7q5qYRW4kxrP6yF0c",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJwYXNzd29yZF90aW1lc3RhbXAiOjE3MDAyMjc0MTguNTYxMjExLCJleHAiOjE3MDI4MjAyOTIsInRva2VuX3R5cGUiOiJyZWZyZXNoIn0.hWzB5PKfRbK-g419Gwqi3ulwGkReRcRK796XEIpUXAI",
    "token_type": "bearer"
}
```

### Database Tables:

```json
{
  "Base (Abstract)": {
    "id": "int",
    "create_date": "datetime",
    "update_date": "datetime"
  },
  "User": {
    "username": "str",
    "password": "str",
    "email": "str",
    "first_name": "str",
    "last_name": "str",
    "active": "bool",
    "role": "enum(str)",
    "password_timestamp": "float"
  }
}
```

### Migration:

```
docker exec api alembic revision --autogenerate -m "description"
docker exec api alembic upgrade head
```
