# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice creating endpoints, validating request data, and returning structured JSON responses. By the end of this assignment, you will be able to design and test a small API service for a real-world use case.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI project and implement endpoints for managing a simple resource, such as books, tasks, or products. Use in-memory data storage (a Python list or dictionary) for this assignment.

#### Requirements
Completed program should:

- Create a FastAPI app with a working root endpoint (for example, GET /).
- Implement at least two resource endpoints (for example, GET /items and POST /items).
- Return JSON responses with appropriate HTTP status codes.
- Include at least one path or query parameter in an endpoint.

### 🛠️ Add Validation and Error Handling

#### Description
Improve your API by using Pydantic models for request validation and by handling common errors. Ensure the API provides clear, student-friendly feedback when input is invalid or data is not found.

#### Requirements
Completed program should:

- Define at least one Pydantic model for request bodies.
- Validate incoming data and reject invalid requests with useful error messages.
- Handle a not-found case (for example, item ID does not exist) with a 404 response.
- Include clear comments or docstrings for any non-obvious API logic.
