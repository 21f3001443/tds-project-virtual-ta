## Web Framework: FastAPI

[FastAPI](https://fastapi.tiangolo.com/) is a modern Python web framework for building APIs with automatic interactive documentation. It's fast, easy to use, and designed for building production-ready REST APIs.

Here's a minimal FastAPI app, `app.py`:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "uvicorn",
# ]
# ///

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Run this with `uv run app.py`.

1. **Handle errors by raising HTTPException**

   ```python
   from fastapi import HTTPException

   async def get_item(item_id: int):
       if not valid_item(item_id):
           raise HTTPException(
               status_code=404,
               detail=f"Item {item_id} not found"
           )
   ```

2. **Use middleware for logging**

   ```python
   from fastapi import Request
   import time

   @app.middleware("http")
   async def add_timing(request: Request, call_next):
       start = time.time()
       response = await call_next(request)
       response.headers["X-Process-Time"] = str(time.time() - start)
       return response
   ```

Tools:

- [FastAPI CLI](https://fastapi.tiangolo.com/tutorial/fastapi-cli/): Project scaffolding
- [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation
- [SQLModel](https://sqlmodel.tiangolo.com/): SQL databases
- [FastAPI Users](https://fastapi-users.github.io/): Authentication

Watch this FastAPI Course for Beginners (64 min):

[![FastAPI Course for Beginners (64 min)](https://i.ytimg.com/vi_webp/tLKKmouUams/sddefault.webp)](https://youtu.be/tLKKmouUams
<youtube_summary>This course by Tommy introduces FastAPI, a modern, fast, and high-performance Python web framework for building APIs. It requires Python 3.6+ and basic Python knowledge. Installation is done via pip, including FastAPI and Uvicorn, the ASGI server to run the API.

The tutorial begins by creating a Python file (my_api.py) and importing FastAPI. An instance of FastAPI is created to build the API. The concept of endpoints is explained: endpoints are URL paths like "/delete_user" representing API functions. Key HTTP methods are introduced: GET (retrieve data), POST (create new data), PUT (update existing data), and DELETE (remove data).

The first example creates a GET endpoint at "/" returning sample JSON data. Running the server with Uvicorn and visiting the URL shows the response. FastAPI automatically generates interactive API documentation at "/docs" using Swagger UI, allowing testing without external tools.

Next, the course covers path parameters and query parameters. Path parameters are dynamic parts of the URL (e.g., "/get_student/{student_id}") that capture input values; query parameters are appended after a question mark in the URL (e.g., "?name=john"). Examples demonstrate retrieving student data by ID (path parameter) and by name (query parameter), including making query parameters optional using Python's Optional type and FastAPI's Path function for validation (e.g., ensuring ID > 0).

The tutorial then covers combining path and query parameters in a single endpoint.

For creating new data, the POST method and request body are introduced. Using Pydantic's BaseModel, a Student class is defined with fields (name, age, year). A POST endpoint creates a new student entry with an ID path parameter and student details in the request body. Duplicate IDs are checked to avoid overwriting existing data.

The PUT method (update) is explained next. An UpdateStudent model with optional fields (name, age, year) allows partial updates. The update endpoint checks if the student exists, then updates only the provided fields, preserving unchanged data. Care is taken to avoid overwriting with null values, ensuring data integrity.

Finally, the DELETE method is shown to remove student entries by ID, with error handling if the student does not exist.

Throughout, the tutorial emphasizes running the server, testing endpoints via the auto-generated docs, and explains error messages and HTTP status responses.

In summary, this course covers FastAPI installation, creating endpoints with GET, POST, PUT, DELETE methods, working with path and query parameters, request bodies using Pydantic models, validation, and auto-generated API documentation, providing a solid foundation for building APIs with FastAPI in Python.</youtube_summary>
)
