# Task Management System

A simple Task Management System built with Django and Django Rest Framework.

## Overview

This project provides a RESTful API for managing tasks. It allows users to perform CRUD (Create, Read, Update, Delete) operations on tasks.

## Features

- Create, Read, Update, and Delete tasks via API endpoints.
- Token-based authentication for API access.
- Unit tests for API views.

## Installation

1. Clone the repository:

   ```bash
   git clone <https://github.com/Vazidnh3/Task_Management>
   ```
2. Install dependencies:
   
  ```bash
  pip install -r requirements.txt
  ```

3. Apply migrations:

 ```bash
python manage.py migrate
```
4. Run the development server:
```bash
python manage.py runserver
```
Access the API at http://127.0.0.1:8000/api/.

## Usage

Authentication: To access API endpoints, you need to authenticate by obtaining a token. You can do this by logging in with a valid user account and obtaining a token.

## Endpoints

List all tasks: GET /api/tasks/
Retrieve a single task by ID: GET /api/tasks/<task_id>/
Create a new task: POST /api/tasks/
Update an existing task: PUT /api/tasks/<task_id>/ or PATCH /api/tasks/<task_id>/
Delete a task: DELETE /api/tasks/<task_id>/

## Testing
To run unit tests for API views:
```bash
python manage.py test
```
## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements or fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
