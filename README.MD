## Local development

```
docker-compose build
docker-compose up
```

## End points

### register

```
http://127.0.0.1:8000/register
payload=
    {
 "username":"shamil",
 "password":"shamil"
}

```

### login

```
http://127.0.0.1:8000/login
payload=
    {
 "username":"shamil",
 "password":"shamil"
}

```

### api key

```
http://127.0.0.1:8002/generate_api_key
payload=
    {
}

headers=Authorization= Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzJkNWNlYzgtNzQ0Ni00YmQ2LWFlOGItODk4NTc0YWVhY2NjIiwiZXhwIjoxNzA3MTQyODYxfQ.Y9cIFacws12zYz7wbqCkv3v_57wDgNMc4tTr28Yw_gg

```

### api key

this endpoint requires username and password which is from the .env
username=shamil
password=shamil

```
http://127.0.0.1:8001/logs

```
