# Sample Flask Auth

A simple REST API built with Flask to demonstrate user authentication and basic user management operations.

The project uses session-based authentication with Flask-Login, data persistence with Flask-SQLAlchemy, and a MySQL database.

## Features

* User registration
* Login with username and password
* Logout
* Retrieve a user by ID
* Update a user password
* Delete a user
* Protected routes
* Prevention of self-deletion
* Password hashing with bcrypt

## Technologies

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* MySQL
* PyMySQL
* bcrypt

## Project Structure

```text
sample-flask-auth-/
├── models/
│   └── user.py
├── app.py
├── database.py
├── requirements.txt
└── README.md
```

## User Model

The application uses the following user model:

| Field      | Type    | Description                                 |
| ---------- | ------- | ------------------------------------------- |
| `id`       | Integer | Unique user identifier                      |
| `username` | String  | Unique username                             |
| `password` | String  | User password                               |
| `email`    | String  | Unique email address                        |
| `role`     | String  | User role, with `user` as the default value |

## Requirements

Before running the project, make sure you have installed:

* Python 3
* pip
* MySQL or MariaDB
* Git

## Installation

Clone the repository:

```bash
git clone https://github.com/saulobdsena/sample-flask-auth-.git
```

Enter the project directory:

```bash
cd sample-flask-auth-
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Linux or macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Install bcrypt:

```bash
pip install bcrypt
```

> The `bcrypt` package is used to generate and verify password hashes.

## Database Configuration

Create a MySQL database:

```sql
CREATE DATABASE `flask-crud`;
```

The current database connection is configured in `app.py`:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://admin:admin123@127.0.0.1:3306/flask-crud"
)
```

The connection URL follows this format:

```text
mysql+pymysql://USERNAME:PASSWORD@HOST:PORT/DATABASE
```

Update the username, password, host, port, and database name according to your MySQL installation.

For better security, environment variables should be used:

```python
import os

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://admin:admin123@127.0.0.1:3306/flask-crud"
)

app.config["SECRET_KEY"] = os.getenv(
    "SECRET_KEY",
    "development-secret-key"
)
```

## Creating the Database Tables

After configuring the database, open a terminal in the project directory and run:

```bash
python
```

Then execute:

```python
from app import app
from database import db

with app.app_context():
    db.create_all()

exit()
```

This command creates the table associated with the `User` model.

## Running the Application

Run:

```bash
python app.py
```

By default, the API will be available at:

```text
http://127.0.0.1:5000
```

To verify that the application is running:

```http
GET /
```

Response:

```text
Hello
```

## API Endpoints

### Register a User

```http
POST /user
```

Request body:

```json
{
  "username": "saulo",
  "password": "my-password",
  "email": "saulo@example.com"
}
```

Expected response:

```json
{
  "message": "Successful"
}
```

cURL example:

```bash
curl -X POST http://127.0.0.1:5000/user \
  -H "Content-Type: application/json" \
  -d '{
    "username": "saulo",
    "password": "my-password",
    "email": "saulo@example.com"
  }'
```

### Login

```http
POST /login
```

Request body:

```json
{
  "username": "saulo",
  "password": "my-password"
}
```

Expected response:

```json
{
  "message": "Authentication successful"
}
```

cURL example:

```bash
curl -X POST http://127.0.0.1:5000/login \
  -H "Content-Type: application/json" \
  -c cookies.txt \
  -d '{
    "username": "saulo",
    "password": "my-password"
  }'
```

The `-c cookies.txt` option stores the session cookie required to access protected routes.

### Get a User

```http
GET /user/<id>
```

This route requires authentication.

Example:

```bash
curl http://127.0.0.1:5000/user/1 \
  -b cookies.txt
```

Response:

```json
{
  "username": "saulo"
}
```

If the user does not exist:

```json
{
  "message": "User not found"
}
```

### Update a User

```http
PUT /user/<id>
```

This route requires authentication.

Request body:

```json
{
  "password": "new-password"
}
```

Example:

```bash
curl -X PUT http://127.0.0.1:5000/user/1 \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{
    "password": "new-password"
  }'
```

Expected response:

```json
{
  "message": "User 1 updated!"
}
```

### Delete a User

```http
DELETE /user/<id>
```

This route requires authentication.

Example:

```bash
curl -X DELETE http://127.0.0.1:5000/user/2 \
  -b cookies.txt
```

Expected response:

```json
{
  "message": "User 2 deleted!"
}
```

An authenticated user cannot delete their own account through this endpoint:

```json
{
  "message": "You cannot delete your own user"
}
```

### Logout

```http
GET /logout
```

This route requires authentication.

Example:

```bash
curl http://127.0.0.1:5000/logout \
  -b cookies.txt
```

Response:

```json
{
  "message": "Logout successful"
}
```

## HTTP Status Codes

| Status Code | Meaning                               |
| ----------- | ------------------------------------- |
| `200`       | Request completed successfully        |
| `400`       | Invalid data or incorrect credentials |
| `401`       | Authentication required               |
| `403`       | Operation not allowed                 |
| `404`       | User not found                        |


## License

This project may be used for educational purposes and for learning Flask, authentication, and REST API development.
