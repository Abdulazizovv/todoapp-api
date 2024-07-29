# Todo App API

A Django-based API for managing todo lists, categories, and items with user authentication.

## Features

- User Registration and Authentication (JWT)
- Create, Read, Update, and Delete (CRUD) operations for Todo Lists, Categories, and Items
- Permissions and Authentication to ensure secure access
- Simple, clean, and easy-to-use API endpoints

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/todoapp.git
   cd todoapp
    ```
2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:** 

    Copy the `.env.dist` file to `.env` and edit it to include your settings.
    ```bash
    cp .env.dist .env
    ```
    Open the .env file and set the following variables:
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True  # Set to False in production
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```

5. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

## Setup

1. **Configure your database:**
    
    The default configuration uses SQLite. For production, configure your database settings in `settings.py`.

2. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

3. **Access the API:**
    
    Open your browser and go to http://127.0.0.1:8000/api .

## API Endpoints

#### Register new user

```http
POST /api/register
```

**Request body**
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**.|
| `email` | `string` | **Required**.|
| `password` | `string` | **Required**.|

**Example response body:**
```json
{
  "id": 0,
  "username": "your_username",
  "email": "your_email",
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

#### Get jwt token

```http
POST /api/token/
```
**Request body**
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**.|
| `password` | `string` | **Required**.|


**Example response body:**

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

**Get new access token via refresh token**
```http
POST /api/token/refresh
```
**Request body**
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `refresh` | `string` | **Required**.|

**Example response body:**

```json
{
  "access": "your_access_token"
}
```


#### Get user details

```http
GET /api/user/
```

##### Headers:
`Authorization: Bearer your_access_token`


#### *Todo Lists*

**Get todo lists**
```http
GET /api/todo/lists/
```

Headers: `Authorization: Bearer your_access_token`

**Example response:**
```json
[
  {
  "id": 0,
  "title": "string",
  "description": "string",
  "created": "2024-07-29T05:36:16.316Z",
  "updated": "2024-07-29T05:36:16.316Z"
  }
]
```

**Get todo items**
```http
GET /api/todo/items/
```

Headers: `Authorization: Bearer your_access_token`

**Example response:**
```json
[
  {
  "id": 0,
  "todo_list": {
    "id": 0,
    "title": "string",
    "description": "string",
    "created": "2024-07-29T05:37:15.631Z",
    "updated": "2024-07-29T05:37:15.631Z"
  },
  "title": "string",
  "description": "string",
  "created": "2024-07-29T05:37:15.631Z",
  "updated": "2024-07-29T05:37:15.631Z"
  }
]
```

**Get todo items**
```http
GET /api/todo/categories/
```

Headers: `Authorization: Bearer your_access_token`

**Example response:**
```json
[
  {
  "id": 0,
  "title": "string",
  "description": "string",
  "created": "2024-07-29T05:37:51.273Z",
  "updated": "2024-07-29T05:37:51.273Z"
}
]
```

## Running the Application

1. Ensure your virtual environment is activated

2. Run the development server
  ```bash
    python manage.py runserver
  ```

3. Access the application

    Open your browser and navigate to http://127.0.0.1:8000


## Contributing

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.