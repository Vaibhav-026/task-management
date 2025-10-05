# Task Management API

A fully functional **Task Management System** built with **Django Rest Framework (DRF)**.  
This API allows users to register, authenticate, and manage their daily tasks efficiently with features like filtering, ordering, and pagination.

---

## Features

- User registration & authentication (JWT)
- Create, update, delete tasks
- Filter tasks by status, priority, or date
- Pagination and ordering support
- tasks linked to the logged-in user
- Token-based authentication using `djangorestframework-simplejwt`

---

## Tech Stack

- **Backend:** Django, Django Rest Framework (DRF)
- **Authentication:** JWT (JSON Web Token)
- **Database:** SQLite (default, easily replaceable with PostgreSQL/MySQL)
- **Language:** Python 3.x

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally:

### 1️⃣ Clone the repository
```bash
git clone git@github.com:Vaibhav-026/task-management.git
cd task-management

2️⃣ Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate      # for Linux/Mac
venv\Scripts\activate         # for Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Create a superuser (optional)

python manage.py createsuperuser

6️⃣ Start the development server
python manage.py runserver

The API will now be available at:http://127.0.0.1:8000/

🔑 Authentication (JWT)

This project uses JWT authentication provided by SimpleJWT.

Method	        Endpoint	                Description
POST	          /api/register/	          Register new user
POST	         /api/token/	              Obtain JWT access & refresh token
POST	        /api/token/refresh/	        Refresh access token


🧾 Task Endpoints

Method	      Endpoint	              Description
GET	          /api/tasks/	            List all tasks (for logged-in user)
POST	        /api/tasks/	            Create a new task
GET	          /api/tasks/<id>/	      Retrieve a specific task
PUT	          /api/tasks/<id>/	      Update a task
DELETE	      /api/tasks/<id>/	      Delete a task

1-Register API curl
    curl --location 'http://127.0.0.1:8000/api/users/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Test",
    "last_name": "Admin",
    "username": "testusernonadminnew",
    "email": "test@user.com",
    "password": "TestAdmin123",
    "confirm_password": "TestAdmin123",
    "is_admin": false
}'

Response-{
    "first_name": "Test",
    "last_name": "Admin",
    "username": "testusernonadminnew",
    "email": "test@user.com",
    "is_admin": false
}

2- Login API Curl
  curl --location 'http://127.0.0.1:8000/api/users/login/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "testusernonadmin",
    "password": "TestAdmin123"
}'
Response-{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1OTcyMTQ1MCwiaWF0IjoxNzU5NjM1MDUwLCJqdGkiOiJiYzI1ZTA1NjUyYjM0YmE1OWQ1ZThjNWYwMzllNGM5ZSIsInVzZXJfaWQiOiI1In0.fLCzvYAwuICfCCAVK7OvvQXMAE2YJ7ytnZRE4-bk8AE",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU5NjM4NjUwLCJpYXQiOjE3NTk2MzUwNTAsImp0aSI6IjI1MzA2NTkxOTQ3MjRkYjJhNGMyOWE0NzI3N2FmZGQ2IiwidXNlcl9pZCI6IjUifQ.DXCDm9Pvka9XKjrpWEXu8o8TcPoSnqpbHq53BUh4MsA"
}


3-Add Task Viewset
curl --location 'http://127.0.0.1:8000/api/task/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU5NjM4NjUwLCJpYXQiOjE3NTk2MzUwNTAsImp0aSI6IjI1MzA2NTkxOTQ3MjRkYjJhNGMyOWE0NzI3N2FmZGQ2IiwidXNlcl9pZCI6IjUifQ.DXCDm9Pvka9XKjrpWEXu8o8TcPoSnqpbHq53BUh4MsA' \
--header 'Content-Type: application/json' \
--data '{
"title": "Hello welcom to Youtube",
"description": "Youtube is owned by Google"
}'
Response-{{
    "id": 8,
    "title": "Hello welcom to Youtube",
    "description": "Youtube is owned by Google",
    "completed": false,
    "created_at": "2025-10-05T03:41:21.655219Z",
    "updated_at": "2025-10-05T03:41:21.655263Z"
}

4-List Task View
curl --location 'http://127.0.0.1:8000/api/task/'
Response-{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 7,
            "title": "Hello welcom to Tiktok",
            "description": "Tiktik is owned by Bytedance",
            "completed": true,
            "created_at": "2025-10-03T15:12:07.796055Z",
            "updated_at": "2025-10-03T14:43:48.096439Z"
        },
        {
            "id": 6,
            "title": "Hello welcom to Youtube",
            "description": "Youtube is owned by Google",
            "completed": false,
            "created_at": "2025-10-03T14:27:43.102036Z",
            "updated_at": "2025-10-03T14:27:43.102072Z"
        },
        {
            "id": 5,
            "title": "Hello welcom to facebook",
            "description": "Facebook is owned by Meta",
            "completed": false,
            "created_at": "2025-10-03T14:09:11.991348Z",
            "updated_at": "2025-10-03T14:09:11.991366Z"
        },
        {
            "id": 4,
            "title": "ttile 4",
            "description": "This description 4",
            "completed": false,
            "created_at": "2025-10-03T14:08:51.185232Z",
            "updated_at": "2025-10-03T14:08:51.185251Z"
        },
        {
            "id": 2,
            "title": "This is second task title",
            "description": "This is second task descriptopm",
            "completed": false,
            "created_at": "2025-10-03T13:48:22.854398Z",
            "updated_at": "2025-10-03T13:48:22.854453Z"
        }
    ]
}




5-Edit Task Viewset
curl --location --request PUT 'http://127.0.0.1:8000/api/task/5/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU5NjM4NjUwLCJpYXQiOjE3NTk2MzUwNTAsImp0aSI6IjI1MzA2NTkxOTQ3MjRkYjJhNGMyOWE0NzI3N2FmZGQ2IiwidXNlcl9pZCI6IjUifQ.DXCDm9Pvka9XKjrpWEXu8o8TcPoSnqpbHq53BUh4MsA' \
--data '{
"title": "This is third task edited title",
"description": "This is third task descriptopm"
}'

Response-{
    "id": 5,
    "title": "This is third task edited title",
    "description": "This is third task descriptopm",
    "completed": false,
    "created_at": "2025-10-05T03:46:25.072659Z",
    "updated_at": "2025-10-03T14:09:11.991366Z"
}
6- Delete Task Viewset
curl --location --request DELETE 'http://127.0.0.1:8000/api/task/1/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU5NjM4NjUwLCJpYXQiOjE3NTk2MzUwNTAsImp0aSI6IjI1MzA2NTkxOTQ3MjRkYjJhNGMyOWE0NzI3N2FmZGQ2IiwidXNlcl9pZCI6IjUifQ.DXCDm9Pvka9XKjrpWEXu8o8TcPoSnqpbHq53BUh4MsA' \
--data '{
"title": "This is second task title",
"description": "This is second task descriptopm"
}'

Response-{
    "message": "Only Admin can delete posts"
}



I have also writtetn custom User API


1-List Task Custom API
curl --location 'http://127.0.0.1:8000/api/task-custom?completed=false'

Response-[
    {
        "id": 5,
        "title": "This is third task edited title",
        "description": "This is third task descriptopm",
        "completed": false,
        "created_at": "2025-10-05T03:46:25.072659Z",
        "updated_at": "2025-10-03T14:09:11.991366Z"
    },
    {
        "id": 8,
        "title": "Hello welcom to Youtube",
        "description": "Youtube is owned by Google",
        "completed": false,
        "created_at": "2025-10-05T03:41:21.655219Z",
        "updated_at": "2025-10-05T03:41:21.655263Z"
    },
    {
        "id": 6,
        "title": "Hello welcom to Youtube",
        "description": "Youtube is owned by Google",
        "completed": false,
        "created_at": "2025-10-03T14:27:43.102036Z",
        "updated_at": "2025-10-03T14:27:43.102072Z"
    },
    {
        "id": 4,
        "title": "ttile 4",
        "description": "This description 4",
        "completed": false,
        "created_at": "2025-10-03T14:08:51.185232Z",
        "updated_at": "2025-10-03T14:08:51.185251Z"
    },
    {
        "id": 2,
        "title": "This is second task title",
        "description": "This is second task descriptopm",
        "completed": false,
        "created_at": "2025-10-03T13:48:22.854398Z",
        "updated_at": "2025-10-03T13:48:22.854453Z"
    }
]


2-Add Task Custom API
curl --location 'http://127.0.0.1:8000/api/task-custom/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU5NjM4NjUwLCJpYXQiOjE3NTk2MzUwNTAsImp0aSI6IjI1MzA2NTkxOTQ3MjRkYjJhNGMyOWE0NzI3N2FmZGQ2IiwidXNlcl9pZCI6IjUifQ.DXCDm9Pvka9XKjrpWEXu8o8TcPoSnqpbHq53BUh4MsA' \
--header 'Content-Type: application/json' \
--data '{
"title": "Hello welcom to Tiktok",
"description": "Tiktik is owned by Bytedance"
}'

Response-{
    "id": 9,
    "title": "Hello welcom to Tiktok",
    "description": "Tiktik is owned by Bytedance",
    "completed": false,
    "created_at": "2025-10-05T03:58:18.928536Z",
    "updated_at": "2025-10-05T03:58:18.928557Z"
}

3-Edit Task Custom API
curl --location --request PUT 'http://127.0.0.1:8000/api/task-custom/7/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU5NjM4NjUwLCJpYXQiOjE3NTk2MzUwNTAsImp0aSI6IjI1MzA2NTkxOTQ3MjRkYjJhNGMyOWE0NzI3N2FmZGQ2IiwidXNlcl9pZCI6IjUifQ.DXCDm9Pvka9XKjrpWEXu8o8TcPoSnqpbHq53BUh4MsA' \
--data '{
    "completed": true
}'

Response-{
    "id": 7,
    "title": "Hello welcom to Tiktok",
    "description": "Tiktik is owned by Bytedance",
    "completed": true,
    "created_at": "2025-10-05T03:57:33.365233Z",
    "updated_at": "2025-10-03T14:43:48.096439Z"
}

4-Delete TAsk Custom APi
curl --location --request DELETE 'http://127.0.0.1:8000/api/task-custom/3/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU5NjQwNDY2LCJpYXQiOjE3NTk2MzY4NjYsImp0aSI6IjkxMjBlYTExZGY4YzRhMGE4NjEwMGFmYTNjOTkwM2I4IiwidXNlcl9pZCI6IjUifQ.0guP2ReiBGFURD2UsQAtOpSM3kxHCeAOSvb9ZwZ7tGY' \
--data '{
"title": "This is third task edited title again",
"description": "This is third task description again"
}'

Response-{
    "message": "Only Admin can delete posts"
}



Example Task Object:
{
  "id": 1,
  "title": "Finish Django project",
  "description": "Complete API endpoints and testing",
  "status": "Pending",
  "priority": "High",
  "created_at": "2025-10-05T10:00:00Z",
  "updated_at": "2025-10-05T10:30:00Z"
}


Filtering & Ordering

Filtering: You can filter tasks by fields such as status, priority, and date.
Ordering: Use query params like ?ordering=date or ?ordering=-date to sort tasks ascending/descending.

Example:
GET /api/tasks/?status=completed&ordering=-date

Project Structure

task_management/
│
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── task_management/
│   ├── settings.py
│   ├── urls.py
│
├── requirements.txt
└── manage.py

Future Enhancements
  Add due date reminders via email
  Add task categories and tags
  Dashboard for task analytics
  Deploy using Docker and Render/AWS

Contributing:Contributions are always welcome!
To contribute:
  Fork this repository
  Create a new branch (feature/your-feature-name)
  Commit your changes
  Push to your branch and open a pull request

License
This project is licensed under the MIT License

Author
Vaibhav Anand
GitHub Profile






