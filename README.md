FastAPI Calculator App (Module 12)

This project implements a secure FastAPI backend with full CRUD operations for users and calculations.
It includes integration tests, CI/CD with GitHub Actions, and Docker deployment.
Features
User Endpoints

Register user — POST /users/register
Login user — POST /users/login
Secure password hashing (SHA256 → bcrypt)
Duplicate username handling
Calculation Endpoints (BREAD)
Browse (GET /calculations)
Read (GET /calculations/{id})
Edit (PUT /calculations/{id})
Add (POST /calculations)
Delete (DELETE /calculations/{id})

Additional Features
Auto-discovered routers
SQLAlchemy models + SQLite locally / PostgreSQL in CI/Docker
Integration tests using pytest + FastAPI TestClient
GitHub Actions CI
Docker-compatible service

Setup Instructions (Local)
1. Clone the repository
git clone
cd HW12

2. Create a virtual environment
python -m venv .venv

Activate it:

.\.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

Run the Application Locally

Start FastAPI:

uvicorn app.main:app --reload


Visit:

 http://localhost:8000/docs

 http://localhost:8000/redoc

Manual Testing via OpenAPI Docs

Open http://localhost:8000/docs

Test Users

POST /users/register
Provide:

{
  "username": "john",
  "email": "john@example.com",
  "password": "1234"
}
POST /users/login

{
  "username": "john",
  "password": "1234"
}

Test Calculations

POST /calculations

{
  "expression": "2+2",
  "result": 4
}


GET /calculations

GET /calculations/{id}

PUT /calculations/{id}

DELETE /calculations/{id}

2. Run all tests:
pytest -q

What tests include:

 Register user
 Login user
 Create calculation
 Retrieve calculation
 Update calculation
 Delete calculation

All database access uses a separate test DB via dependency override.

GitHub Actions CI/CD

Run integration tests

If tests pass then build & push Docker image to Docker Hub

To enable:

Add two GitHub Secrets:

DOCKER_USER
DOCKER_PASS


Push to main branch.

Docker Instructions
Run using Docker Compose (local)
docker-compose up --build


API will run at:

http://localhost:8000

Using PostgreSQL container for storage.

