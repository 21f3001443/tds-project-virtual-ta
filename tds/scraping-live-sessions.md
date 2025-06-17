## Scraping: Live Sessions

[![Intro to Web scraping and HTML](https://i.ytimg.com/vi_webp/cAriusuJsmw/sddefault.webp)](https://youtu.be/cAriusuJsmw
<youtube_summary>Amit Gupta, a diploma-level TDS instructor, conducted an introductory session on web scraping and HTML basics using OBS software for the first time. He began by surveying participants' prior knowledge of HTML, finding about 40% had some experience. Amit demonstrated the power of web scraping using Python scripts in Jupyter Notebook and Google Colab, showing how scripts can quickly extract hundreds of links from a Wikipedia page and save them as CSV files, tasks that would take hours manually.

He showcased web scraping of a practice website listing countries with details like name, capital, population, and area, using Selenium to automate browser actions invisibly. The scraped data was saved as Excel files for further analysis. Amit discussed real-world applications such as price monitoring on e-commerce sites and automated weather data collection, emphasizing automation through system commands to schedule script execution.

Further, he demonstrated scraping Amazon for smartphones under a price threshold across multiple pages, extracting product details and exporting them to CSV within minutes, highlighting the efficiency over manual methods.

The session then shifted to foundational HTML instruction. Amit explained HTML structure, tags, attributes, and how to create simple web pages using Notepad, including elements like paragraphs, headings (H1-H6), line breaks (br), horizontal rulers (hr), anchor tags (a) with href attributes for links, and image tags (img) with src for images. He emphasized the importance of closing tags and good coding practices, noting HTML's forgiving nature but encouraging proper syntax for collaborative work.

Amit introduced tables with table (table), table row (tr), table data (td), and table header (th) tags, demonstrating how to build structured data tables and add borders. Lists were covered using unordered lists (ul) and ordered lists (ol) with list items (li), including nested lists.

He recommended resources like W3Schools and MDN for learning HTML and suggested using VS Code as an advanced code editor for better coding experience. The instructor encouraged hands-on practice and interaction, addressing questions about tags, syntax, and editor usage.

Amit then explained how to inspect live websites using browser developer tools (Inspect Element), showing how to identify HTML elements, read attributes like src for images, and modify content temporarily. He demonstrated how to edit text and images on Wikipedia pages locally via Inspect Element.

The session covered monitoring network traffic within developer tools, explaining API calls, GET/POST requests, and how APIs act as intermediaries providing controlled data access from servers, using Wikipedia's API as an example. Amit highlighted the importance of understanding network requests for advanced web scraping.

He briefly touched on cookies and promised to discuss them in future sessions. Participants asked questions about HTML editing, tag usage, and web scraping concepts. Amit clarified differences between HTML (markup language for webpage structure) and Python (programming language for computation and automation).

The session concluded with a feedback form request and encouragement for continued practice. Amit offered support via Discord and planned further detailed web scraping sessions in upcoming classes.</youtube_summary>
)

Fundamentals of web scraping with urllib and BeautifulSoup

[![Fundamentals of web scraping with urllib and BeautifulSoup](https://i.ytimg.com/vi_webp/I3auyTYORTs/sddefault.webp)](https://youtu.be/I3auyTYORTs
<youtube_summary>The text is a detailed transcript of a web scraping tutorial session focusing on Python and the use of libraries like urllib and Beautiful Soup. Key points covered include:

1. Tools Required:
   - A browser to open websites (Wikipedia preferred).
   - An environment to write and execute Python code, with Google Colab recommended for its online, CPU-friendly nature.

2. Using Google Colab:
   - How to open, rename, and run Python notebooks in Colab.
   - Colab runs Python code on Google servers, relieving local CPU load.
   - Code sharing and collaboration features in Colab.

3. Basics of Web Scraping:
   - Understanding URLs as addresses for web pages.
   - When a URL is requested, the server returns HTML code, not the visual page.
   - Browsers render HTML into visual content; scraping involves working with raw HTML.

4. Libraries for Web Scraping:
   - urllib.request (specifically urlopen) to fetch HTML content from URLs.
   - Beautiful Soup (bs4) to parse and beautify HTML, making it easier to read and search.
   - Demonstration of reading HTML content from a URL and printing it.
   - Difference between x (the urlopen object) and x.read() (method to get HTML content as string).
   - Use of different parsers with Beautiful Soup like 'html.parser', 'lxml', and 'html5lib'.

5. HTML Structure and Tags:
   - How to find specific HTML tags like <title>, <a> (anchor), <img> (image), <h1>, <head>, etc.
   - Using Beautiful Soup's find() method to get the first occurrence of a tag.
   - Using find_all() to get all occurrences of a tag.
   - Output of find_all() is a list-like structure; indexing can access specific elements.
   - Differences between find() and find_all().

6. Working with Local HTML Files:
   - Uploading files to Colab to read local HTML files.
   - Issues encountered and troubleshooting steps.

7. Navigating Nested Tags:
   - How to traverse HTML hierarchies (e.g., table > tr (table row) > td (table data)).
   - Extracting text content from tags.
   - Understanding empty tags or tags containing other tags instead of text.

8. Using Attributes and Classes:
   - Importance of attributes like class, id, href, src in identifying specific elements.
   - Syntax for finding tags with specific attributes using Beautiful Soup.
   - Handling multiple class values.
   - Using attributes like width and height to filter elements.
   - Demonstrated finding tables or images by their class attributes.

9. Common Errors and Debugging:
   - Typographical errors such as incorrect capitalization in library names.
   - Sequence of commands: Import library > define URL > read URL > parse with Beautiful Soup.
   - Handling errors related to parsers and library usage.

10. Practical Exercises:
    - Encouragement to practice by scraping different websites.
    - Use of find and find_all methods.
    - Extracting specific elements like the fifth image or all anchor tags.
    - Using loops and conditional checks in Python to filter and find elements.

11. Additional Concepts:
    - Explanation of what a class is in HTML (an attribute for styling and identification).
    - Discussion on how multiple classes can be assigned to a tag.
    - Using developer tools and Ctrl+F to find occurrences of tags or classes in HTML.
    - Mention of upcoming topics like handling cookies.

12. Session Interactions:
    - Participants asked questions about code specifics, errors, and concepts.
    - Instructor encourages active participation and experimentation.
    - Sharing of code snippets and collaborative debugging.

In summary, the session thoroughly introduces beginners to web scraping fundamentals using Python, urllib, and Beautiful Soup, emphasizing practical coding steps, HTML structure understanding, and attribute-based element searching, all within an interactive and collaborative learning environment.</youtube_summary>
)

Intermediate web scraping use of cookies

[![Intermediate web scraping use of cookies](https://i.ytimg.com/vi_webp/DryMIxMf3VU/sddefault.webp)](https://youtu.be/DryMIxMf3VU
<youtube_summary>The session is a detailed lecture on web scraping, focusing on practical coding exercises, challenges, and the importance of cookies in scraping secure websites. Key points covered include:

1. **Why Web Scraping?**  
   - Manual data collection is time-consuming and inefficient, especially for large or frequently changing datasets like world population or stock market data.  
   - Scraping automates data extraction, saving hours of manual work and enabling daily updates with minimal effort.

2. **Scraping Dynamic and Large Data**  
   - Examples include scraping data tables of countries and populations from websites with hundreds of rows.  
   - Writing code initially takes time but pays off by saving much more time in the long run.

3. **Practical Coding Exercises**  
   - Students practiced scraping a table of countries and populations from a website with clean HTML using Python libraries like BeautifulSoup and pandas.  
   - Various approaches were discussed, including using attributes like IDs to pinpoint specific tables and making code generic with loops to handle unknown row counts.  
   - Common issues like spelling mistakes, indexing errors, and handling headers were addressed interactively.

4. **Handling Website Variations**  
   - Websites differ greatly; no fixed formula fits all.  
   - If website structure changes, scraping code must be updated accordingly.  
   - Some websites use simple HTML tables while others use complex, JavaScript-heavy pages requiring more advanced techniques.

5. **Introduction to Cookies and Login Handling**  
   - Many websites require login to access data, making scraping more complex.  
   - Cookies store session information proving user identity and are essential for scraping logged-in content.  
   - The lecture demonstrated how to inspect cookies via browser developer tools (Network tab) and extract session cookies.

6. **Using Requests Library with Cookies**  
   - Compared to urllib, the requests library is more suitable for handling cookies in scraping.  
   - Students learned how to convert cookies into Python dictionary format and include them in HTTP requests to access secure pages.

7. **Scraping a Complex Website (MovieLens)**  
   - The MovieLens website requires login and uses dynamic content loading via APIs.  
   - The instructor showed how inspecting the Network tab reveals API endpoints returning JSON data containing the desired information (movie titles, ratings, etc.).  
   - By sending requests with proper cookies to these API URLs, one can scrape data not directly visible in the HTML source.

8. **Parsing JSON Data**  
   - The JSON module is used to convert raw JSON text into Python dictionaries for easier data extraction.  
   - Techniques to navigate nested dictionaries to extract movie titles and other details were demonstrated.

9. **Security and Ethical Considerations**  
   - Cookies are sensitive and unique per user session; sharing cookies can expose personal data.  
   - The instructor warned against sharing cookies carelessly and highlighted the security risks involved.  
   - Mentioned the concept of session expiration and the temporary validity of cookies.

10. **Summary and Q&A**  
    - Majority of students were able to write working scraping code after practice.  
    - Common errors and debugging tips were discussed.  
    - The instructor encouraged students to practice independently and explore advanced topics like cookies and API scraping further.  
    - The session concluded with plans to share recordings and continue with topics like cookies in upcoming lectures.

Overall, the session combined theoretical explanations with hands-on coding practice, emphasizing the practical challenges of web scraping, especially on secure, dynamic websites, and the crucial role of cookies for authenticated scraping.</youtube_summary>
)

XML intro and scraping

[![XML intro and scraping](https://i.ytimg.com/vi_webp/8S_jvsjtaYg/sddefault.webp)](https://youtu.be/8S_jvsjtaYg
<youtube_summary>The session is about XML scraping, focusing on understanding XML structure, reading, and parsing XML files using Python, particularly with pandas and the ElementTree library. Here's a detailed summary:

1. Introduction to XML:
   - XML stands for Extensible Markup Language.
   - Unlike HTML, XML allows user-defined tags and is not limited to predefined tags.
   - XML is a markup language used to store and transfer data with a hierarchical (tree-like) structure.
   - Comparison with JSON and CSV: XML is more verbose than JSON; CSV is flat, while XML supports nested data.
   - XML files can be opened in browsers but are not rendered like HTML; visualization tools (online XML viewers) help understand structure.

2. XML Structure and Tree Visualization:
   - XML consists of nested tags (envelopes), e.g., a root tag containing multiple child tags.
   - Example: A "note" object with tags like link, style, to, from, heading, and body.
   - Each tag can have child tags, attributes, and text content.
   - The hierarchical structure is important for understanding and scraping XML data.

3. Reading and Parsing XML in Python:
   - Use pandas to read XML files: `pd.read_xml()`.
   - ElementTree (`xml.etree.ElementTree`) is a Python library suited for parsing XML due to its tree structure handling.
   - Key functions:
     - `ET.parse(filename)` to parse XML.
     - `tree.getroot()` to get the root element.
     - Access elements by indexing, `.find()`, `.findall()` methods.
   - Iteration over elements is done to extract data, often using nested loops.
   - Example: Extracting data from rows and columns in XML representing medal counts by year.

4. Practical Exercise and Code Examples:
   - Download XML and CSV datasets from data.gov.in for comparison.
   - Demonstration of how to open and interpret XML files.
   - Writing Python code to parse XML, extract data such as year, medal counts, etc.
   - Different coding approaches shared by participants including:
     - Using loops to iterate over rows and tags.
     - List comprehensions for concise extraction.
     - Creating Python lists for each column (year, serial number, medal types).
     - Converting lists into pandas DataFrames for structured analysis.

5. DataFrames and Data Manipulation:
   - Creating pandas DataFrames from lists extracted from XML.
   - Assigning column names.
   - Discussion on row-wise vs column-wise data representation.
   - Advantages of column-wise data for data analysis.

6. Additional Points:
   - Discussion on attributes in XML tags (not present in the example dataset).
   - Importance of understanding XML structure for data science and scraping tasks.
   - Encouragement to practice and explore XML parsing independently.
   - Mention of other data formats like JSON, CSV, YAML, PDF, and their relevance.
   - Clarification on session recordings and resources on YouTube for further learning.
   - Emphasis on learning Python fundamentals as essential for XML scraping.

7. Q&A and Community Interaction:
   - Participants shared code snippets, solutions, and helped each other.
   - Discussion of tools for viewing and formatting XML files.
   - Clarifications about the role of XML, its advantages over CSV, and use cases.
   - Guidance on how to handle large XML files and nested structures.
   - Encouragement to use loops and Python libraries effectively.

In summary, the session provided a comprehensive introduction to XML scraping, focusing on understanding XML's hierarchical structure, parsing XML files using Python (ElementTree and pandas), extracting relevant data, and converting it into usable formats like DataFrames. The importance of practicing Python and XML parsing was emphasized, alongside collaborative problem-solving and sharing of coding techniques.</youtube_summary>
)
