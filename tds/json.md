## JSON

JSON (JavaScript Object Notation) is the de facto standard format for data exchange on the web and APIs. Its human-readable format and widespread support make it essential for data scientists working with web services, APIs, and configuration files.

For data scientists, JSON is essential when:

- Working with REST APIs and web services
- Storing configuration files and metadata
- Parsing semi-structured data from databases like MongoDB
- Creating data visualization specifications (e.g., Vega-Lite)

Watch this comprehensive introduction to JSON (15 min):

[![JSON Crash Course](https://i.ytimg.com/vi_webp/GpOO5iKzOmY/sddefault.webp)](https://youtu.be/GpOO5iKzOmY
<youtube_summary>This video tutorial explains JSON (JavaScript Object Notation), a crucial data representation format widely used by programmers and web developers, especially for APIs, config files, and more. JSON is lightweight, easy to read compared to XML, and integrates seamlessly with JavaScript. Almost all major programming languages support parsing JSON into objects.

JSON supports several data types: strings, numbers (including decimals, negatives, scientific notation), booleans (true/false), null, arrays, and objects. Objects are key-value pairs where keys must be in double quotes, and values can be any JSON type. Arrays are ordered lists of values separated by commas.

To create a JSON file, use the .json extension and include a JSON object or array as the top-level structure. An example user object includes keys like "name" (string), "favoriteNumber" (number), "isProgrammer" (boolean), "hobbies" (array of strings), and "friends" (array of nested user objects), demonstrating JSON's ability to represent deeply nested data hierarchies.

The video provides a live example creating a companies.json file containing an array of company objects with properties like name, number of employees, CEO (which can be null), and rating. It highlights the importance of double quotes around keys and string values, comma placement, and shows how Visual Studio Code helps identify JSON syntax errors.

In JavaScript, JSON data can be directly assigned to variables since JSON is valid JavaScript syntax. However, when JSON data is received as a string (common in APIs), it must be parsed using JSON.parse() to convert it into usable JavaScript objects. The video demonstrates accessing parsed data, such as company names, from the resulting objects.

The tutorial emphasizes JSON's simplicity, readability, lightweight nature, and widespread use, making it essential knowledge for developers working with APIs or data interchange. Viewers are encouraged to like and subscribe for more tutorials.</youtube_summary>
)

Key concepts to understand in JSON:

- JSON only supports 6 data types: strings, numbers, booleans, null, arrays, and objects
- You can nest data. Arrays and objects can contain other data types, including other arrays and objects
- Always validate. Ensure JSON is well-formed. Comm errors: Trailing commas, missing quotes, and escape characters

[JSON Lines](https://jsonlines.org/) is a format that allows you to store multiple JSON objects in a single line.
It's useful for logging and streaming data.

Tools you could use with JSON:

- [JSONLint](https://jsonlint.com/): Validate and format JSON
- [JSON Editor Online](https://jsoneditoronline.org/): Visual JSON editor and formatter
- [JSON Schema](https://json-schema.org/): Define the structure of your JSON data
- [jq](https://stedolan.github.io/jq/): Command-line JSON processor

Common Python operations with JSON:

```python
import json

# Parse JSON string
json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)

# Convert to JSON string
json_str = json.dumps(data, indent=2)

# Read JSON from file
with open('data.json') as f:
    data = json.load(f)

# Write JSON to file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read JSON data a Pandas DataFrame. JSON data is typically stored as an array of objects.
import pandas as pd
df = pd.read_json('data.json')

# Read JSON lines from file into a DataFrame. JSON lines are typically one line per object.
df = pd.read_json('data.jsonl', lines=True)
```

Practice JSON skills with these resources:

- [JSON Generator](https://json-generator.com/): Create sample JSON data
- [JSON Path Finder](https://jsonpathfinder.com/): Learn to navigate complex JSON structures
- [JSON Schema Validator](https://www.jsonschemavalidator.net/): Validate JSON against schemas
