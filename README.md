# FastAPI + React Task Manager

A full-stack web application built using FastAPI (backend) and React (frontend) that supports user authentication, role-based access control, and CRUD operations on tasks.

---

## 🚀 Features

### Backend (FastAPI)
- User registration and login
- Password hashing using bcrypt
- JWT-based authentication
- Role-based access (admin vs user)
- Protected APIs
- CRUD APIs for Tasks
- Admin-only delete functionality
- API versioning (`/api/v1`)
- Swagger API documentation
- SQLite database
- CORS enabled

### Frontend (React)
- User registration and login UI
- JWT token persistence using localStorage
- Task list UI
- Create, update, and delete tasks
- Logout functionality
- Error handling
- Real-time API integration

---

## 🛠 Tech Stack

**Backend:**
- FastAPI
- SQLAlchemy
- SQLite
- Passlib (bcrypt)
- Python-Jose (JWT)

**Frontend:**
- React
- Fetch API

---

## ⚙️ Setup Instructions

### 1️⃣ Backend Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn python-jose passlib[bcrypt] sqlalchemy email-validator
uvicorn main:app --reload


Scalability Notes
This application is designed to scale with the following enhancements:

- Replace SQLite with PostgreSQL or MySQL for production
- Add Redis for caching frequent queries and JWT blacklisting
- Dockerize the backend and frontend for containerized deployment
- Use Nginx as a reverse proxy and load balancer
- Split services into microservices Auth Service, Task Service
- Add background workers using Celery or FastAPI background tasks
- Implement rate limiting and request throttling
- Use environment variables for secrets and configuration
