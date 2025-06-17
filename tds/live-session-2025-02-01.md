# Live Session: 01 Feb 2025

[![2025-02-01 Week 3 - Session 5 - TDS Jan 25](https://i.ytimg.com/vi_webp/tsn7B7mDzw8/sddefault.webp)](https://youtu.be/tsn7B7mDzw8
<youtube_summary>The discussion recaps a coding session focused on building and deploying a web application that interacts with customers placing orders via natural language, using OpenAI's language models with function calling capabilities. Key points include:

1. **Application Overview**:  
   - Two main functions: `order` (to place orders) and `delete_order` (to cancel orders by order ID).  
   - Orders include items, quantities, delivery address, and delivery time.  
   - Orders are stored in a Pandas DataFrame (`order_df`).  
   - The system generates unique order IDs and calculates total prices based on a predefined price dictionary.

2. **Natural Language to Structured Data Conversion**:  
   - Customers can input unstructured natural language queries like "I want 1 laptop, 2 smartphones, and 1 tablet delivered to X by Y."  
   - The application sends this prompt to OpenAI's GPT model with a JSON schema describing the expected function parameters (items, delivery address, delivery time).  
   - GPT returns structured JSON arguments that the application uses to execute the appropriate function.

3. **Function Calling and JSON Schema**:  
   - A JSON schema defines the function signature, parameter types, and required fields.  
   - This schema is sent along with the prompt to GPT to get a structured response suitable for function execution.

4. **Error Handling & User Interaction**:  
   - If GPT returns incomplete information (e.g., missing quantity), the application prompts the user for missing details.  
   - The system distinguishes between regular text responses and function call responses based on the presence of specific keys in the GPT response.

5. **Web Application Setup**:  
   - The code is transitioned from Jupyter notebooks (used for teaching/debugging) to a production-ready Python script (`app.py`) using FastAPI.  
   - FastAPI endpoints handle GET requests with query parameters carrying user prompts.  
   - Environment variables are used to securely manage API keys (e.g., AI proxy tokens).  
   - The server runs locally on `localhost` port 8000.

6. **Deployment Using Docker**:  
   - Docker images are created to containerize the application, ensuring consistent environments across different systems.  
   - Dockerfile sets up Python, copies application code, installs dependencies (including `uvicorn`), and runs the FastAPI app.  
   - Port mapping is configured to expose the server outside the container.  
   - Docker containers provide isolated, lightweight environments that are easy to deploy and scale.

7. **Use of UVicorn**:  
   - `uvicorn` is used to run the FastAPI app as an ASGI server.  
   - Explained advantages of `uvicorn` over traditional environment management tools like `pip` and virtualenvs, as it handles dependencies dynamically per run.

8. **Development Tools & Environment**:  
   - Discussion on differences between Jupyter notebooks and Python scripts: notebooks are for interactive development; scripts are for production.  
   - VS Code and WSL (Windows Subsystem for Linux) used as development environment.  
   - Terminals inside Docker containers and WSL explained as interaction points with virtualized environments.

9. **Function Execution Flow**:  
   - FastAPI decorators like `@app.get("/order")` route requests to respective functions.  
   - Query parameters are parsed and passed to the GPT API.  
   - Responses from GPT determine which function to call and with what parameters.

10. **Error and Response Handling**:  
    - Implemented logic to detect if GPT response contains function call data or just plain text.  
    - Application returns meaningful prompts back to the user for missing information.  
    - Handled errors such as missing keys in JSON or server errors gracefully.

11. **Demonstration and Testing**:  
    - Participants tested the API by sending various natural language queries through browser URLs with URL-encoded parameters.  
    - The system successfully placed orders and handled errors interactively.

12. **Discussion on Docker vs Podman and Open Source Concerns**:  
    - Podman used as an alternative to Docker (due to Docker’s paid model).  
    - Docker images are portable and can run on various systems without worrying about dependencies or OS differences.

13. **Future Work and Project Expectations**:  
    - Next sessions will cover advanced topics like dynamic code generation by LLMs, error feedback loops, and prompt engineering.  
    - Emphasis on building robust applications for projects that can self-correct code based on runtime errors.  
    - Students encouraged to start early and use the learned workflow for their projects.

14. **Additional Notes**:  
    - Explanation of Python’s `if __name__ == "__main__":` as entry point for script execution.  
    - How environment variables are exported and accessed in Python applications.  
    - Differences between synchronous and asynchronous HTTP request libraries (`requests` vs `httpx`).  
    - Importance of clear documentation, markdown, and sharing code in collaborative environments.

Overall, the session provided a comprehensive workflow from natural language input through GPT function calling, to building, testing, deploying, and running a scalable web application inside Docker containers, preparing students for practical AI-driven application development and deployment.</youtube_summary>
)

**Q1: Can I use Python notebooks instead of VS Code for this project?**

**A1:** You can use Python notebooks for interactive development and debugging, but for a production environment, a script file (.py) is better because it allows for a defined order of execution, unlike notebooks where code cells may not necessarily branch from one section to another. Notebooks are great for sharing with others who may not understand the code, as you can add Markdown to explain each step.

**Q2: In the delete order function, could a wrong order ID get deleted if the prompt contains multiple things that could match multiple orders?**

**A2:** That's a good question. This application isn't built to be very robust. The goal is to demonstrate GPT's ability to convert natural language into functions that the application understands. A real-world application would have a more robust interface (website or local app) with precisely crafted inputs to map to functions, preventing such errors.

**Q3: How can I avoid manually managing virtual environments and dependencies when deploying my application?**

**A3:** Use `uv`. `uv` is similar to Docker in that it handles dependencies without requiring manual management of virtual environments. You just specify your dependencies at the top of your code, and `uv` handles everything else, including creating and disposing of the virtual environment. This is especially useful when dealing with many submissions with different package requirements, as seen in a previous project with nearly 700 submissions.

**Q4: How does the application know which function to run based on the user's request?**

**A4:** You send the user's natural language request (prompt) and a list of your application's capabilities to GPT. GPT determines which function to run and the required parameters, returning this information as structured JSON. Your application then uses this JSON to execute the appropriate function.

**Q5: What is the purpose of `if __name__ == "__main__":`?**

**A5:** This is the entry point for your application. The Python interpreter runs from top to bottom, but it won't run the code within this block unless the file is the starting file of the application. This is crucial for multi-file applications where the interpreter needs to know where to begin.

**Q6: Should I create a tunnel for this application?**

**A6:** No, there's no need to create a tunnel if you want others to try it. Using a tool like ngrok allows others to access your server directly and send queries. However, be aware that this might crash your system if the queries aren't clean, as there's no robust error handling.

**Q7: How do I pass URL-encoded parameters to a FastAPI application?**

**A7:** You pass them in the URL itself. For example, `localhost:8000/order?q=Laptop,2,123 Main St,2024-02-29`. The application then reads the parameter from the URL.

**Q8: Why is my application returning a null response or a 422 error?**

**A8:** Several things could cause this. Ensure that:

- The `prices` dictionary is defined globally, not within a function.
- The prompt is correctly formatted and includes all necessary information (items, address, time).
- The application can communicate with the outside world (check network connectivity).
- You are using the correct key in the JSON response (`.keys()`).

**Q9: How do I use Docker?**

**A9:** Docker creates lightweight, self-contained images that run inside a Docker engine. This isolates your application from the underlying system, making it portable and easy to deploy anywhere. You build the image using `podman build -t tds-hello .` (the `.` refers to the current working directory). Then, you run it using `podman run -it tds-hello bash`. The `bash` command opens an interactive shell within the Docker container.

**Q10: What are the use cases for Docker?**

**A10:** Docker is useful for deploying applications to various environments without worrying about dependencies or system specifics. You create a Docker image containing your application and its dependencies. Anyone can then download and run the image regardless of their operating system. This is especially helpful for teams with different setups or when deploying to multiple clients.

**Q11: What should I focus on for the GA3 project?**

**A11:** The GA3 project will involve using the concepts covered today, but on a larger scale. You'll need to create more robust error handling and focus on prompt engineering to ensure the LLM generates the correct code. A previous session covered the basics of LLM calls, tokenization, embeddings, and image URI encoding. Review that session and the material on prompt engineering to prepare. The goal is to create a self-writing program that uses the LLM to generate and correct code dynamically.
