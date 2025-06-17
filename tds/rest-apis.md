## REST APIs

REST (Representational State Transfer) APIs are the standard way to build web services that allow different systems to communicate over HTTP. They use standard HTTP methods and JSON for data exchange.

Watch this comprehensive introduction to REST APIs (52 min):

[![REST API Crash Course - Introduction + Full Python API Tutorial (52)](https://i.ytimg.com/vi_webp/qbLc5a9jdXo/sddefault.webp)](https://youtu.be/qbLc5a9jdXo
<youtube_summary>This REST API crash course by Caleb covers fundamental concepts, how to consume APIs, and building a REST API in Python using Flask and SQLAlchemy.

Key Points:

1. **What is an API?**
   - API (Application Programming Interface) allows different software applications, possibly built in different languages (e.g., Python, JavaScript), to communicate.
   - Communication is typically one-way: client requests data from a server, which responds.
   - REST (Representational State Transfer) APIs communicate over the web using HTTP requests, typically returning data in JSON format (preferred over XML).

2. **JSON Explained**
   - JSON (JavaScript Object Notation) is a text-based format for representing structured data as key-value pairs, similar to JavaScript objects or Python dictionaries.
   - It is the standard language for APIs.

3. **API Structure**
   - APIs have endpoints (e.g., `/drinks`, `/drinks/{id}`) representing resources.
   - URLs can be organized via subdomains (e.g., `api.example.com`) or subdirectories.

4. **Reasons for API Architecture**
   - Security: Prevent direct database access from clients (especially JavaScript clients).
   - Versatility: Multiple front-end apps (web, mobile) can share the same backend and data.
   - Modularity: Backend can be updated or swapped without breaking front-end apps.
   - Interoperability: Public APIs allow third parties to build apps using your data.

5. **HTTP Methods & CRUD**
   - GET: Retrieve data (Read).
   - POST: Create new data (Create).
   - PUT: Update/replace existing data (Update).
   - DELETE: Delete data (Delete).
   - PATCH: Partial updates (less common here).
   - PUT is idempotent (same request repeated causes no additional effect), POST is not guaranteed idempotent.

6. **Consuming an API Example**
   - Demonstrated using Stack Overflow’s public API via `api.stackexchange.com`.
   - Use query parameters to filter or sort results.
   - Recommended tool: Postman for testing API requests.
   - Python example with `requests` library to perform GET requests, parse JSON, and filter data (e.g., print questions with zero answers).

7. **Creating a REST API in Python**
   - Use Flask for web framework and SQLAlchemy for ORM (object-relational mapping).
   - Set up virtual environment and install dependencies (`flask`, `flask_sqlalchemy`).
   - Define a Drink model with fields: `id` (primary key), `name` (unique, non-null string), `description` (string).
   - Initialize Flask app, configure SQLite database, and create tables.
   - Insert data using ORM objects and commit to database.
   - Create API endpoints:
     - GET `/drinks`: returns all drinks as JSON list.
     - GET `/drinks/<id>`: returns a single drink by ID or 404 if not found.
     - POST `/drinks`: add a new drink by parsing JSON from request body.
     - DELETE `/drinks/<id>`: delete a drink by ID with error handling if not found.
   - Return JSON responses by constructing dictionaries or lists of dictionaries.
   - Use Postman to test POST and DELETE requests.
   - Explanation of route definitions, request methods, and handling JSON input/output.

8. **Best Practices and Notes**
   - Separate frontend and backend for security and modularity.
   - Use consistent API interface so frontends don't break when backend changes.
   - For updating data, PUT can be used or alternatively deleting and creating anew.
   - Error handling (e.g., for missing resources) improves robustness.
   - Use `jsonify` when needed; returning dictionaries is often sufficient.
   - Maintain a `requirements.txt` for dependencies.
   - Use virtual environments for project isolation.

The course includes practical code examples, detailed explanations of concepts, and encourages using tools like Postman and Python `requests` for API development and consumption.</youtube_summary>
)

Key Concepts:

1. **HTTP Methods**
   - `GET`: Retrieve data
   - `POST`: Create new data
   - `PUT/PATCH`: Update existing data
   - `DELETE`: Remove data
2. **Status Codes**
   - `2xx`: Success (200 OK, 201 Created)
   - `4xx`: Client errors (400 Bad Request, 404 Not Found)
   - `5xx`: Server errors (500 Internal Server Error)

Here's a minimal REST API using FastAPI. Run this `server.py` script via `uv run server.py`:

```python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastapi",
#     "uvicorn",
# ]
# ///
from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

# Create a list of items that will act like a database
items: List[Dict[str, float | int | str]] = []

# Create a GET endpoint that returns all items
@app.get("/items")
async def get_items() -> List[Dict[str, float | int | str]]:
    return items

# Create a GET endpoint that returns a specific item by ID
@app.get("/items/{item_id}")
async def get_item(item_id: int) -> Dict[str, float | int | str]:
    if item := next((i for i in items if i["id"] == item_id), None):
        return item
    raise HTTPException(status_code=404, detail="Item not found")

# Create a POST endpoint that creates a new item
@app.post("/items")
async def create_item(item: Dict[str, float | str]) -> Dict[str, float | int | str]:
    new_item = {"id": len(items) + 1, "name": item["name"], "price": float(item["price"])}
    items.append(new_item)
    return new_item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Test the API with curl:

```bash
# Get all items
curl http://localhost:8000/items

# Create an item
curl -X POST http://localhost:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Book", "price": 29.99}'

# Get specific item
curl http://localhost:8000/items/1
```

Best Practices:

1. **Use Nouns for Resources**
   - Good: `/users`, `/posts`
   - Bad: `/getUsers`, `/createPost`
2. **Version Your API**
   ```
   /api/v1/users
   /api/v2/users
   ```
3. **Handle Errors Consistently**
   ```python
   {
     "error": "Not Found",
     "message": "User 123 not found",
     "status_code": 404
   }
   ```
4. **Use Query Parameters for Filtering**
   ```
   /api/posts?status=published&category=tech
   ```
5. **Implement Pagination**
   ```
   /api/posts?page=2&limit=10
   ```

Tools:

- [Postman](https://www.postman.com/): API testing and documentation
- [Swagger/OpenAPI](https://swagger.io/): API documentation
- [HTTPie](https://httpie.io/): Modern command-line HTTP client
- [JSON Schema](https://json-schema.org/): API request/response validation

Learn more about REST APIs:

- [REST API Design Best Practices](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
- [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines)
- [Google API Design Guide](https://cloud.google.com/apis/design)
