# FastAPI JWT Auth API

---
### Summary:

```
FastAPI, Postgres, Sqlalchemy, Pydantic v2, Docker
API example with JWT Authentication.
```

### Requirements:

```
docker
```

### Run:

```
cp config/.env.example config/.env
docker compose up --build -d
```

### Migration:

```
docker compose exec api alembic revision --autogenerate -m "description"
docker compose exec api alembic upgrade head
```

### Docs:

```
localhost:8000/docs
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

### Database Tables:

```json
{
  "Base (Abstract)": {
    "id": "int",
    "create_date": "datetime",
    "update_date": "datetime"
  },
  "User": {
    "username":  "str",
    "password":  "str",
    "email":  "str",
    "first_name":  "str",
    "last_name": "str",
    "active":  "bool",
    "role":  "enum(str)",
    "password_timestamp": "float"
  }
}
```

---
