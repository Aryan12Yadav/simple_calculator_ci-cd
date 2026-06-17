# Simple Calculator CI/CD

## Project Overview

Simple Calculator CI/CD is a full-stack web application developed as a college-level project to demonstrate modern software development practices. The application provides basic arithmetic operations through a user-friendly React interface and stores calculation history using PostgreSQL.

The project follows a layered backend architecture using FastAPI, SQLAlchemy, PostgreSQL, Redis caching, Docker, GitHub Actions, Render, and Vercel.

The main objective of this project is to understand how frontend, backend, database, caching, containerization, deployment, and CI/CD pipelines work together in a real-world application.

---

## Features

* Addition
* Subtraction
* Multiplication
* Division
* Calculation history storage
* PostgreSQL database integration
* Redis caching support
* REST API architecture
* React frontend
* FastAPI backend
* Docker support
* GitHub Actions CI pipeline
* Render backend deployment
* Vercel frontend deployment

---

## Technology Stack

### Frontend

* React.js
* Axios
* Vite

### Backend

* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn

### Database

* PostgreSQL

### Cache

* Redis

### DevOps

* Docker
* GitHub Actions
* Render
* Vercel

---

## Project Architecture

Frontend (React)

↓

FastAPI REST API

↓

Service Layer

↓

SQLAlchemy ORM

↓

PostgreSQL

↓

Redis Cache

---

## Folder Structure

calculator_project/

backend/

app/

api/

services/

models/

schemas/

database/

cache/

main.py

requirements.txt

Dockerfile

frontend/

src/

components/

services/

App.jsx

main.jsx

package.json

vite.config.js

.github/

workflows/

ci-cd.yml

---

## API Endpoints

### Calculate

POST

/calculator/calculate

Parameters:

* num1
* num2
* operation

Supported Operations:

* add
* subtract
* multiply
* divide

---

### Get History

GET

/calculator/history

Returns all previous calculations stored in the database.

---

## Database Schema

Table Name: calculations

Columns:

* id
* operation
* num1
* num2
* result

---

## Local Setup

### Clone Repository

git clone <repository-url>

cd calculator_project

---

### Backend Setup

cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

---

### Environment Variables

Create a .env file

DATABASE_URL=your_postgresql_url

REDIS_HOST=localhost

REDIS_PORT=6379

REDIS_DB=0

---

### Run Backend

uvicorn app.main:app --reload

Backend URL:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs

---

### Frontend Setup

cd frontend

npm install

npm run dev

Frontend URL:

http://localhost:5173

---

## Docker Setup

Build Image

docker build -t calculator-api .

Run Container

docker run -p 8000:8000 calculator-api

---

## CI/CD Pipeline

GitHub Actions is used for Continuous Integration.

Pipeline Steps:

1. Checkout repository
2. Setup Python environment
3. Install backend dependencies
4. Setup Node.js environment
5. Install frontend dependencies
6. Build React application

Workflow file:

.github/workflows/ci-cd.yml

---

## Deployment

### Backend Deployment

Platform: Render

Deployment Type: Web Service

Environment Variables:

* DATABASE_URL
* REDIS_HOST
* REDIS_PORT
* REDIS_DB

---

### Frontend Deployment

Platform: Vercel

Environment Variable:

VITE_API_URL=<backend-url>

---

## Object-Oriented Design

The backend follows Object-Oriented Programming principles.

### Encapsulation

Business logic is encapsulated inside the CalculatorService class.

### Abstraction

API routes interact with service methods instead of directly handling database operations.

### Modularity

Each layer has a dedicated responsibility:

* API Layer
* Service Layer
* Model Layer
* Schema Layer
* Database Layer
* Cache Layer

This improves maintainability and readability.

---

## Learning Outcomes

Through this project, I learned:

* REST API development using FastAPI
* Database management with PostgreSQL
* ORM concepts using SQLAlchemy
* Redis caching fundamentals
* React frontend development
* Docker containerization
* CI/CD implementation using GitHub Actions
* Cloud deployment using Render and Vercel
* Environment variable management
* Layered software architecture

---

## Future Improvements

* User Authentication
* JWT Security
* Docker Compose
* Unit Testing
* Integration Testing
* API Rate Limiting
* Logging and Monitoring
* Kubernetes Deployment
* Advanced Caching Strategies

---

## Author

Aryan Yadav

B.Tech (Computer Science and Engineering - Artificial Intelligence)

Chhatrapati Shahu Ji Maharaj University

---

## License

This project is developed for educational and learning purposes.
