# Live Session: 31 Jan 2025

[![2025-01-31 Week 3 - Session 4 - TDS Jan 25](https://i.ytimg.com/vi_webp/sdg4N-H4BR0/sddefault.webp)](https://youtu.be/sdg4N-H4BR0
<youtube_summary>The session focused on demonstrating OpenAI's function calling feature by automating an order placement and update system. The instructor showed how to create a Python program that takes a user's natural language prompt (e.g., ordering laptops, smartphones, tablets with delivery address and date), sends it to OpenAI, which identifies the appropriate function to call and extracts structured parameters in JSON format. This structured data can then be processed by the program to update a pandas DataFrame simulating a database.

Key points discussed:

1. **Function Calling Concept**: OpenAI can analyze natural language prompts and determine which predefined function to execute along with required parameters, enabling applications to handle user requests without complex UIs.

2. **Defining Functions and JSON Schema**: Functions like `order` were defined with a JSON schema specifying required parameters such as ordered items (array of objects with item name and quantity), delivery address, and delivery time. This schema guides OpenAI to return structured, non-hallucinated responses.

3. **Implementation Details**: 
   - Used Python functions to insert order data into a pandas DataFrame acting as a database.
   - Generated unique order IDs using UUID.
   - Calculated total price based on item quantities and prices stored in a dictionary.
   - Showed how to parse OpenAI's JSON responses and execute corresponding Python functions.

4. **Multiple Functions and Dynamic Function Selection**: Demonstrated adding another function, e.g., `delete_order`, and how OpenAI decides which function to call based on the user's prompt.

5. **Error Handling and Robustness**: Discussed how required parameters can be enforced, and how OpenAI can be instructed to ask users for missing information via system prompts.

6. **Integration with Speech-to-Text**: Briefly mentioned the possibility of integrating speech-to-text (e.g., using OpenAI’s Whisper model) to convert voice commands into text prompts.

7. **Deployment and Packaging**: Plans to demonstrate packaging the code into a full-fledged application with API endpoints and Docker in subsequent sessions.

8. **Additional Q&A**: 
   - Explained managing environment variables and tokens in Google Colab versus other environments.
   - UUID uniqueness and usage considerations.
   - Handling variable names like `class` in API parameters using aliases.
   - Debugging deployment issues with Vercel and API routing.
   - Strategies for handling nested JSON data and passing parameters correctly.
   - Tips for prompt engineering and robust function calling design.
   - Discussion on RO (Rapid Online) exam details including duration, submission tips, and question handling.

The session provided a comprehensive walkthrough of using OpenAI function calling to bridge natural language user input and structured programmatic function execution, enabling intelligent automation of tasks like ordering and updates. It also covered practical coding, debugging, and deployment considerations, preparing students for further project work and real-world applications.</youtube_summary>
)

**Q1: In today's session, what will be covered?**

**A1:** We will be discussing the function calling part of OpenAI. We will create a program that takes user prompts in English, identifies which function to call based on the prompt, and then calls that function.

**Q2: What is the first step in the process?**

**A2:** First, we import the `requests` library. Then, we'll get the headers and URL for the request, and finally, we'll create a JSON body for the request.

**Q3: What is the goal of the program?**

**A3:** The program aims to automate the process of ordering something from an online store. It will take a user's order in plain English, understand the request, and place the order. It will also include a feature for updating existing orders.

**Q4: How will the program understand the user's prompt?**

**A4:** The program will send the user's prompt to OpenAI. OpenAI will use its function calling capabilities to identify the appropriate function to call from a predefined set of functions within your application, and return the function name and parameters in a JSON format.

**Q5: What are the predefined functions?**

**A5:** The predefined functions are a set of tools your application provides. Examples include `get_weather_info` (which takes a location as a parameter) and `best_hotels` (which also takes a location). OpenAI will determine which function to call based on the user's prompt.

**Q6: How does OpenAI determine which function to call?**

**A6:** OpenAI analyzes the user's prompt and, based on its understanding of the context and semantics, selects the appropriate function from the predefined set. The response from OpenAI will include the function name and its required parameters in JSON format.

**Q7: How does the program use the OpenAI response?**

**A7:** Your application receives the JSON response from OpenAI, extracts the function name and parameters, and then executes the function with those parameters. The result is then sent back to the user. OpenAI acts as a proxy for a human agent, handling natural language input and translating it into structured data for your application.

**Q8: Is the `order` function dependent on the above-written cell?**

**A8:** Yes, the `order` function uses variables defined in previous cells.

**Q9: How is the JSON response handled?**

**A9:** The JSON response from OpenAI is structured data that your application can easily process. It contains the function name and the parameters needed to execute that function.

**Q10: How can we handle cases where the user doesn't provide complete information?**

**A10:** You can instruct OpenAI to request missing information. The handling of incomplete requests depends on your application's design. OpenAI itself might request the missing data.

**Q11: How can we integrate a voice model?**

**A11:** You can integrate a speech-to-text model (like Whisper from OpenAI) to convert voice commands into text prompts for your application.

**Q12: How do we package the Colab notebook into a full-fledged application?**

**A12:** We'll demonstrate this in a future session by creating another function and packaging the entire application into a Docker image.

**Q13: What is the role of prompt engineering in this process?**

**A13:** Prompt engineering is less about a specific science and more about understanding how the system works to write effective prompts that yield the desired results. The course will cover this in more detail.

**Q14: What if the `order` function doesn't work as expected?**

**A14:** The instructor suggests checking the code, ensuring the correct parameters are passed, and handling potential errors gracefully. The instructor also suggests using `json.loads` to convert strings to JSON objects.

**Q15: What is the duration of the Review of Exercises (ROE)?**

**A15:** The ROE duration varies from term to term, ranging from 45 minutes to 1.5 hours. It's recommended to save your work frequently.

**Q16: What if the user's prompt is missing information?**

**A16:** The instructor suggests adding a system prompt to OpenAI to explicitly request missing parameters.

**Q17: How do we handle the `UUID` generation to ensure uniqueness?**

**A17:** The `UUID` library generally provides unique identifiers. If you need to reduce the chance of collisions, you can increase the size of the UUID. More information is available in the UUID documentation.

**Q18: How do we handle the file path in a deployed application?**

**A18:** Instead of using absolute paths (`os.path`), use relative paths to ensure the application works correctly in different environments. For deployed applications, you would typically use a `.env` file to store sensitive information like API keys.

**Q19: What is the overall approach to building this application?**

**A19:** The approach is to use OpenAI's function calling capabilities to translate natural language prompts into structured data that your application can process. This allows for a more natural user experience without the need for a complex UI. The instructor emphasizes the importance of understanding how to parse JSON responses and handle errors.
