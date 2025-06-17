# Live Session: 06 Feb 2025

[![2025-02-06 Week 4 - Session 3 - TDS Jan 25](https://i.ytimg.com/vi_webp/u5RFmePd7NQ/sddefault.webp)](https://youtu.be/u5RFmePd7NQ
<youtube_summary>The live session begins with an introduction to G4, highlighting that it is easier than previous sessions and will be lighter for participants. The first topic covered is extracting tables from HTML using Google Sheets' IMPORTHTML function, which is not available in Excel without plugins. The example used is extracting a table of top-ranked animes from a website. The function requires four parameters: URL, query (either "list" or "table"), index (which table number), and locale. The instructor demonstrates extracting the first table (index 0) and explains zero-based indexing similar to Python. Questions clarify that the function automatically finds tables and the indexing method.

Next, the session shifts to web scraping IMDb data using JavaScript, specifically with query selectors. The instructor references a previous session explaining query selectors and how to extract data such as participant names. The session covers three cases for extracting data: when JSON data is available, when it is not, and alternative methods. The instructor shows how to find JSON data in network tabs using browser developer tools and demonstrates fetching JSON data using Python's requests library and VS Code's Thunder Client extension. 

In the second case, where JSON is not directly accessible, the instructor guides students to use JavaScript query selectors to extract data from HTML elements. The example used is an IPL player list table. The instructor explains how to inspect elements, find common classes, and use JavaScript's document.querySelectorAll (represented as $$ in the console) to select elements by class. They break down the JavaScript code to extract player names, explaining the use of class selectors (prefixed with a dot), IDs (prefixed with #), and the difference between innerText and innerHTML properties. The map function is used to iterate over selected elements and extract their text content. The importance of choosing the correct class to avoid extraneous data is emphasized.

The third case involves websites that do not expose JSON data via network requests but embed data within JavaScript files. The instructor demonstrates how to find embedded JSON data in JS files loaded by the page. They explain this is a poor practice by developers but sometimes necessary to retrieve data. Students are shown how to locate relevant JS files that contain the needed data, access it via URLs, and fetch it using Thunder Client or Python requests. The process is manual and requires checking multiple JS files.

Following this, the session introduces Beautiful Soup, a Python library for parsing HTML and extracting data. The instructor compares using JavaScript console query selectors to Beautiful Soup's methods such as find, find_all, and select, which operate using CSS selectors. They demonstrate requesting HTML pages via Python's requests module, parsing with Beautiful Soup, and selecting elements by ID, class, or complex CSS selectors. Examples include extracting anime ranking data from a web page. The instructor also discusses running a FastAPI server to create endpoints that accept query parameters to return specific data like anime rank based on name.

Several participant questions revolve around FastAPI usage, request methods (GET/POST), running servers, and debugging errors related to method not allowed or bad requests. The instructor offers to assist offline and encourages posting detailed issues on the course’s Discourse forum for collaborative troubleshooting.

The session concludes with a discussion about ambiguities and broad scopes in project requirements, particularly related to file formats (Markdown, Python), formatting tools, API design, and testing mechanisms. The instructor acknowledges that some questions are outside their control as assignments are prepared by another instructor, encourages students to post detailed questions on Discourse, and suggests arranging meetings with the assignment creator for clarifications. The importance of clear requirements and testing environments is emphasized. Suggestions include face-to-face meetings with the project stakeholder for better understanding. The instructor apologizes for any lack of clarity and promises efforts to resolve ambiguities.

Action items include posting all doubts on Discourse, tagging instructors and the assignment creator, and attending future live sessions for better support. The instructor reminds students of upcoming sessions and offers further help with FastAPI and other technical issues as needed.

In summary, the session covers:
- Using Google Sheets IMPORTHTML to extract tables from web pages.
- Extracting JSON data via browser network tools and Python requests.
- Using JavaScript query selectors to scrape data when JSON is unavailable.
- Parsing HTML with Beautiful Soup in Python.
- Creating FastAPI endpoints to serve extracted data.
- Debugging FastAPI request issues.
- Addressing project ambiguities through Discourse and planned meetings.
- Encouraging participation in live sessions for ongoing support.</youtube_summary>
)

**Q1: In this GA4 session, what's new compared to previous GAs?**

**A1:** The trajectory has moved from hard to easy. This GA is much easier and lighter than previous ones.

**Q2: How do I extract a table from HTML using Google Sheets?**

**A2:** This functionality is available in Google Sheets but not in Excel (unless you use plugins). The `IMPORTHTML` function will give you a #NAME? error in Excel.

**Q3: How can I extract data from the ODI Batsman Stats webpage?**

**A3:** I'll show you how to extract data from a different webpage, but you can find a similar example in my previous live session on YouTube.

**Q4: What do the parameters in the `IMPORTHTML` function mean?**

**A4:** The four parameters are: URL, query (either "list" or "table"), index (table number), and locale. The index is zero-based (like Python).

**Q5: How does the `IMPORTHTML` function automatically find the table?**

**A5:** It finds the table based on the index you provide. If there are multiple tables, you'll need to adjust the index accordingly.

**Q6: How can I extract data from a webpage that doesn't use a JSON object?**

**A6:** There are three ways:

- **Method 1:** If the webpage uses a JSON object, you can extract it directly.
- **Method 2:** Use query selectors in the browser's console to extract the data. This involves finding a common element (class) in the HTML and using JavaScript to extract the data. The `$$` operator establishes a connection between the console and the elements tab. The `.` prefix selects elements by class, and `#` selects by ID.
- **Method 3:** Sometimes, the data is embedded in JavaScript code within the webpage itself. You can find this in the browser's "Sources" tab. You can then use this JavaScript object to extract the data.

**Q7: What's the difference between `innerText` and `innerHTML`?**

**A7:** `innerText` returns only the text content of an element, while `innerHTML` returns the entire HTML code within that element.

**Q8: I'm having trouble using the FastAPI in Chrome. I've posted on Discourse multiple times, but it's still not working. The error is "Method Not Allowed".**

**A8:** When using POST requests with FastAPI, you need to specify the method in the request. I'll look into your Discourse post and get back to you. We can also schedule a separate meeting to discuss this further. The issue might be related to how your system interacts with the host (it might be localhost).

**Q9: Regarding the project, the scope seems too broad. Can we narrow it down? Also, what tools are required? Is there a sandbox environment for testing?**

**A9:** The scope is indeed broad. The project's requirements are defined by Anand, who is also the CEO of a company. He's busy, but you can contact him through Discourse. We can discuss the scope and tools further in a meeting. There is no sandbox environment for testing. The goal is to extract data, but the method is not specified. You can enhance the goal by using other tools (Autodesk, Blender, etc.), but the scope should be restricted by the QA team. We can discuss this further in a meeting.
