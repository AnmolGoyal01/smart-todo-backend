# 🧠 Smart Todo Backend

This is the backend for the **Smart Todo List** application built using Django and Django REST Framework. It supports CRUD operations on tasks, along with time-based auto-bucketing into `Ongoing`, `Success`, and `Failure` based on deadlines.

---

## 🚀 Features

- Create, update, delete, and list tasks
- Status auto-update based on deadline
- API to update expired tasks
- PostgreSQL database using Docker
- RESTful APIs for frontend integration

---

## 🛠️ Technologies

- Python 3.9
- Django 4.2
- Django REST Framework
- PostgreSQL (via Docker)
- psycopg2-binary

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/anmolgoyal01/smart-todo-backend.git
cd smart-todo-backend
```

### 2. Create Virtual Environment
```bash
uv venv .venv
source .venv/bin/activate
```
### 3. Install Dependencies
```bash
uv pip install -r smart_todo_backend/requirements.txt
```
### 4. Start PostgreSQL with Docker
```bash
docker-compose -f smart_todo_backend/docker-compose.yml up -d
```
Ensure PostgreSQL is up and running on port `5432`.
### 5. Configure Environment
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'smarttodo',
        'USER': 'anmol',
        'PASSWORD': 'secret123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
### 6. Apply Migrations
```bash
cd smart_todo_backend
python manage.py migrate
```
### 6. Run the Server
```bash
python manage.py runserver
```
## 📡 API Endpoints

### 🔹 GET /api/tasks/
Returns a list of all tasks.

```bash
GET http://localhost:8000/api/tasks/
```

### 🔹 POST /api/tasks/
Create a new task.

```bash
POST http://localhost:8000/api/tasks/
Content-Type: application/json

{
  "title": "Finish Assignment",
  "description": "Complete the Django backend task",
  "deadline": "2025-06-26T18:30",
  "status" : "ongoing"
}
```
### 🔹 GET /api/tasks/`<id>`/
Get a specific task by ID.
```bash
GET http://localhost:8000/api/tasks/1/
```
### 🔹 PUT /api/tasks/`<id>`/
Update a task by ID.
```bash
PUT http://localhost:8000/api/tasks/1/
Content-Type: application/json

{
  "title": "Finish Assignment",
  "description": "Updated description",
  "deadline": "2025-06-27T15:00",
  "status": "success"
}
```
### 🔹 DELETE /api/tasks/`<id>`/
Delete a task by ID.

```bash
DELETE http://localhost:8000/api/tasks/1/
```
### 🔹 GET /api/tasks/update-status/
Auto-update tasks with expired deadlines (for status `ongoing` → `failure`).

```bash
GET http://localhost:8000/api/tasks/update-status/
```




## 🔗 Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://anmolgoyal.me/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anmol-goyal-358804235/)
[![twitter](https://img.shields.io/badge/github-010101?style=for-the-badge&logo=github&logoColor=white)](https://anmolgoyal.me/_next/static/media/github-icon.04fa7de0.svg)
