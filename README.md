# Library Management System API

This is a **Flask-based Library Management System API** integrated with **MongoDB** for database operations. The API supports CRUD operations for managing books and members, along with features like search, pagination, and token-based authentication.

---

## Features

1. **CRUD Operations**:
   - Manage books and members with Create, Read, Update, and Delete functionalities.

2. **Search Books**:
   - Search books by title or author with case-insensitive matching.

3. **Pagination**:
   - Support for paginated responses for book listing and search.

4. **Token-Based Authentication**:
   - Secures endpoints using JWT (JSON Web Token).

5. **MongoDB Integration**:
   - Uses MongoDB as the database for efficient and scalable data storage.

---

## Design Choices

### 1. **Framework: Flask**
   - Flask was chosen for its lightweight nature and flexibility for building RESTful APIs.
   - It supports modular application structures, which aligns well with the separation of concerns in this project.

### 2. **Database: MongoDB**
   - A NoSQL database was chosen to allow for flexibility in schema design and to handle potential hierarchical data (e.g., nested information about books or members).
   - MongoDB’s native support for querying with filters, pagination, and text search makes it suitable for features like searching and filtering.

### 3. **Authentication: JWT**
   - Token-based authentication with `Flask-JWT-Extended` ensures secure endpoints.
   - JWTs allow stateless authentication, which is lightweight and scalable for APIs.

### 4. **Directory Structure**
   - Organized in a modular structure to separate concerns, making the application easier to maintain and extend.

### 5. **Pagination**
   - Added to book listing and search endpoints to prevent overloading the server and to ensure efficient handling of large datasets.

### 6. **Environment Variables**
   - Sensitive configurations like database URI and JWT secret keys are stored securely in a `.env` file, ensuring security and configurability across environments.

---

## Assumptions

1. **Authentication**:
   - The application currently uses hardcoded user credentials for login. In a production system, this would be replaced with a proper user management system (e.g., a users collection in the database).

2. **Books and Members Schema**:
   - The data models for books and members are basic, assuming each book has a title, author, ISBN, and available copies.
   - The members model assumes simple fields like name and email, without advanced relationships or borrowing histories.

3. **Pagination Defaults**:
   - Default `page` is `1`, and `per_page` is `10` unless explicitly provided in the request.

---

## Limitations

1. **Authentication System**:
   - Lacks role-based access control (e.g., admin vs. regular users).
   - User management (e.g., registration, password reset) is not implemented.

2. **Database Transactions**:
   - MongoDB does not inherently support transactions across multiple collections. This could be a limitation for complex operations involving both books and members.

3. **Search Functionality**:
   - Search supports only title and author fields, and is limited to basic regex matching. Advanced search (e.g., using weights or fuzzy matching) is not implemented.

4. **Scalability**:
   - While MongoDB and Flask support scalability, the current implementation is not optimized for horizontal scaling (e.g., caching, database indexing).

5. **Testing**:
   - No unit or integration tests are included. These are essential for ensuring robust API functionality.

---

## Installation

### Prerequisites

- Python 3.8+
- MongoDB installed and running locally or hosted remotely

---

### Steps to Run the Project

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd library-management
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the root directory:
     ```plaintext
     SECRET_KEY=your_secret_key
     JWT_SECRET_KEY=your_jwt_secret_key
     MONGO_URI=mongodb://localhost:27017/library
     ```

5. **Run the Application**
   ```bash
   python run.py
   ```

6. **Access the API**
   - Base URL: `http://127.0.0.1:5000`

---

## API Endpoints

### Authentication
| Method | Endpoint         | Description                  |
|--------|------------------|------------------------------|
| POST   | `/auth/login`    | Generate a JWT token         |

- **Request Body**:
  ```json
  {
    "username": "admin",
    "password": "password123"
  }
  ```

---

### Books
| Method | Endpoint            | Description                       |
|--------|---------------------|-----------------------------------|
| GET    | `/books/`           | List books (with pagination)      |
| GET    | `/books/search`     | Search books by title or author   |
| GET    | `/books/<id>`       | Get book details by ID            |
| POST   | `/books/`           | Create a new book (auth required) |
| PUT    | `/books/<id>`       | Update book details (auth req.)   |
| DELETE | `/books/<id>`       | Delete a book (auth required)     |

- **Search Example**:
  - GET `/books/search?title=Python&page=1&per_page=5`

---

### Members
| Method | Endpoint            | Description                       |
|--------|---------------------|-----------------------------------|
| GET    | `/members/`         | List members                     |
| GET    | `/members/<id>`     | Get member details by ID          |
| POST   | `/members/`         | Create a new member (auth req.)   |
| PUT    | `/members/<id>`     | Update member details (auth req.) |
| DELETE | `/members/<id>`     | Delete a member (auth required)   |

