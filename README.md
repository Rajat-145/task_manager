# Task Manager API

## Overview

This project is a RESTful API for a task management system built with Flask. The API provides functionalities for user registration, authentication, and task management. It supports the following features:

- User Registration and Authentication
- CRUD operations for tasks (Create, Read, Update, Delete)
- Task assignment to users
- Filtering and searching tasks

## Features

### User Registration and Authentication

- Register users with a username and password.
- Securely hash passwords.
- Log in to receive a JWT token for authenticated requests.

### Task Management

- **Create Task**: Add new tasks.
- **Read Tasks**: Retrieve tasks assigned to the authenticated user.
- **Update Task**: Modify existing tasks.
- **Delete Task**: Remove tasks.

### Filtering and Searching

- Filter tasks based on status, priority, and due date.
- Search tasks by title and description.

## Setup and Installation

### Prerequisites

- Python 3.11 or later
- PostgreSQL
- Docker

### Installation

1. **Clone the Repository**

    ```bash
    git clone <repository_url>
    cd task_manager
    ```

2. **Install Dependencies**

   - Without Virtual Environment:

     ```bash
     pip install -r requirements.txt
     ```

3. **Create the Database Schema**

    Create a file named `create_db.py` in the root directory with the following content:

    ```python
    from app import create_app, db

    app = create_app()

    with app.app_context():
        db.create_all()
    ```

    Run the script to create the database schema:

    ```bash
    python create_db.py
    ```

4. **Environment Variables**

    Create a `.env` file in the root directory with the following content:

    ```makefile
    DATABASE_URL=postgresql://postgres:Pass@123@localhost:5432/mydatabase
    JWT_SECRET_KEY=myjwtsecretkey
    SECRET_KEY=mysecretkey
    ```

## Running the Application with Docker

1. **Build and Start Docker Containers**

    ```bash
    docker-compose up --build
    ```

2. **Access the Application**

    The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## API Endpoints

- **User Registration**
  - Endpoint: `/auth/register`
  - Method: POST
  - Request Body: JSON with username and password
  - Response: Success or error message

- **User Login**
  - Endpoint: `/auth/login`
  - Method: POST
  - Request Body: JSON with username and password
  - Response: JWT token

- **Create Task**
  - Endpoint: `/tasks/add`
  - Method: POST
  - Headers: Authorization: Bearer `<token>`
  - Request Body: JSON with title, description, status, priority, and due_date
  - Response: Success or error message

- **Get Tasks**
  - Endpoint: `/tasks`
  - Method: GET
  - Headers: Authorization: Bearer `<token>`
  - Query Parameters: Optional filtering and search parameters
  - Response: List of tasks

- **Update Task**
  - Endpoint: `/tasks/<task_id>`
  - Method: PUT
  - Headers: Authorization: Bearer `<token>`
  - Request Body: JSON with fields to update
  - Response: Success or error message

- **Delete Task**
  - Endpoint: `/tasks/<task_id>`
  - Method: DELETE
  - Headers: Authorization: Bearer `<token>`
  - Response: Success or error message

## Troubleshooting

- **Database Connection Issues**: Ensure PostgreSQL is running and the `DATABASE_URL` in `.env` is correctly configured.
- **Missing Dependencies**: Install missing Python packages as listed in `requirements.txt`.

## Contributing

Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
