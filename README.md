# 🚀 FastAPI + React Task Manager

A full-stack web application built using **FastAPI (backend)** and **React (frontend)** that supports user authentication, role-based access control, and CRUD operations on tasks using a production-ready PostgreSQL database.

---

## 📌 Features

### 🔹 Backend (FastAPI)

- User registration and login
- Password hashing using bcrypt
- JWT-based authentication
- Role-based access control (Admin vs User)
- Protected APIs
- CRUD APIs for Tasks
- Admin-only delete functionality
- API versioning (`/api/v1`)
- Swagger API documentation
- Modular clean architecture (service layer)
- CORS enabled
- Environment-based configuration

---

### 🔹 Frontend (React)

- User registration and login UI
- JWT token persistence using localStorage
- Protected dashboard
- Task list display
- Create and delete tasks
- Logout functionality
- Error and success message handling
- Real-time API integration

---

## 🛠 Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Passlib (bcrypt)
- Python-Jose (JWT)
- Pydantic
- pydantic-settings
- Uvicorn

### Frontend
- React
- Fetch API
- JavaScript
- HTML5 / CSS3

---

## ⚙️ Setup Instructions

---

### 1️⃣ Backend Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

## 📘 API Documentation

Swagger documentation is available at:

http://127.0.0.1:8000/docs

---

## 🔐 Environment Configuration

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/taskmanager
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

⚠️ The `.env` file is excluded from version control.

---

## 🗄 Database Setup

This project uses **PostgreSQL** for production-ready data persistence.

Create the database:

```sql
CREATE DATABASE taskmanager;
```

Tables are automatically created on server startup.

---

## 📈 Scalability & Production Enhancements

This application is structured to scale with:

- Redis for caching and JWT blacklisting
- Docker containerization
- Nginx reverse proxy & load balancing
- Microservices separation (Auth Service, Task Service)
- Background workers (Celery or FastAPI background tasks)
- Rate limiting and request throttling
- Database migrations using Alembic
- CI/CD pipeline integration

