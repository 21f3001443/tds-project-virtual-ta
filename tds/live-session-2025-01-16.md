# Live Session: 16 Jan 2025

[![2025-01-16 Week 1 - Session 1 - TDS Jan 25](https://i.ytimg.com/vi_webp/1H5Aq7HjqwQ/sddefault.webp)](https://youtu.be/1H5Aq7HjqwQ
<youtube_summary>The discussion covers various tools and concepts in data science, focusing on topics from week one and preparing for week two assignments and exams. The session begins with an overview of VS Code—its installation, productivity tips, extensions, debugging tools, and version control features—highlighting that the first graded assignment mainly requires installing VS Code and running a command to capture output, without technical complexity.

A significant part of the session is dedicated to explaining the UV command-line tool, which simplifies running Python applications by allowing inline metadata scripts specifying dependencies and Python versions, eliminating the need for manual virtual environment setup. UV is especially useful for deploying and automating the running of multiple Python scripts with diverse dependencies, as demonstrated by its application in grading hundreds of student submissions with varying requirements. Participants learn how to install UV on different operating systems and use it to run Python scripts that automatically handle dependencies. The distinction between global installations and project-specific environments is clarified, with UV and tools like npx and yarn (for JavaScript) helping maintain isolated environments for projects.

The discussion also touches upon the use of npx for running JavaScript code locally without global installs, facilitating web development with frameworks like React or Next.js. It explains that npx works across different shells (PowerShell and Bash), though some commands may require Bash for full functionality.

Regarding Excel and Google Sheets, it is noted that some formulas or functions work only in Google Sheets, and non-paid Excel users can utilize the free online Excel version.

A detailed tutorial on browser Developer Tools (DevTools) is provided, focusing on the Elements, Console, and Network tabs, which are most relevant for data science tasks in the course. The Elements tab shows the HTML and CSS structure of web pages, allowing users to inspect, modify, and experiment with page content locally. The Console tab enables running JavaScript code for tasks like data extraction. The Network tab displays all network requests and resources fetched by the browser, useful for understanding data sources and APIs.

The session demonstrates using DevTools to scrape data from web pages, such as extracting movie titles from IMDb. It explains CSS selectors, particularly classes and IDs, detailing how classes (prefixed with a dot) apply styles to multiple elements, while IDs (prefixed with a hash) uniquely identify single elements. The instructor shows how to use JavaScript in the Console tab with CSS selectors (e.g., using document.querySelectorAll via the shorthand $$) to collect elements and extract their innerText or innerHTML. The difference between innerText (text content) and innerHTML (HTML content) is clarified, with innerText recommended for extracting visible text. Participants are encouraged to practice extracting data from web pages using these tools.

Additional clarifications include how to copy extracted data from the console using the copy() function, understanding that elements with the same class can serve different purposes (e.g., movie titles and links), and the importance of unique IDs versus reusable classes in HTML structure.

The session concludes with an exercise to extract names from a meeting participant list using DevTools, encouraging hands-on practice and the use of resources like ChatGPT for assistance. The instructor recommends exploring the Elements, Console, and Network tabs further to build familiarity before the next session. The overall emphasis is on practical skills for data extraction, environment management with UV, and utilizing developer tools for web data science tasks.</youtube_summary>
)

**Q1: What will be covered in this session?**

**A1:** This session will cover concepts from Week 1 of the graded assignment in Tools in Data Science (TDS). The focus is on guiding students toward solutions, not providing exact answers. Week 2 will be covered in the next session.

**Q2: Is it possible to reschedule the TDS session?**

**A2:** The instructor will check if rescheduling is possible. If not, recordings will be available on YouTube.

**Q3: The first question in the graded assignment is about VS Code. What's involved?**

**A3:** The question focuses on installing VS Code and running a specific command in the terminal, then pasting the output into an input box. There's no significant technical component to this question.

**Q4: What are the benefits of using the UV command-line tool?**

**A4:** UV eliminates the need to create virtual environments. You include small portions of code and run the application with minimal setup.

**Q5: How does UV integrate with VS Code?**

**A5:** There's no integration; UV is used in the command prompt, similar to pip (Python), npm (JavaScript), or Node.js.

**Q6: Are there examples demonstrating UV usage and integration with VS Code?**

**A6:** No specific VS Code integration is needed. UV is used in the command line, like pip or npm. A previous project (Project 2) used UV to automate running 687 student Python submissions, each with unique requirements. Students added metadata to their Python files specifying the Python version and required libraries. UV dynamically handled these requirements for each submission.

**Q7: In the RWE exam, what will the format be like?**

**A7:** The format will be similar to the graded assignments: questions and answer boxes. You can use any tools you want. It's a non-proctored exam. It will cover concepts taught in the course, including new material.

**Q8: In Week 1, do we need to build advanced-level concepts, or will we learn them week by week?**

**A8:** Each week will have different content, including graded assignments. Content links are provided.

**Q9: The UV part of the project was only a 7-minute video. Do we need to learn UV fully in Week 1, or will we learn it in upcoming weeks?**

**A9:** UV is introduced in Week 1. The most useful aspect is embedding everything in inline metadata within the script, eliminating the need for virtual environments.

**Q10: How do we start the project?**

**A10:** There will be separate guidance sessions for the project.

**Q11: Will we get a screen recording of this session?**

**A11:** Yes, the session will be uploaded to YouTube.

**Q12: While putting in the directory for a specific file (e.g., question 2), do you need to provide the full address (drive, etc.)?**

**A12:** It works because the script is executed from the same directory. You need to provide the correct path (relative or absolute).

**Q13: Can you explain the use of DevTools?**

**A13:** Right-click on the browser and select "Inspect." This opens a world of code and information about the website. You can see HTML, JavaScript, CSS, etc. You can use the arrow tool to select an element, then modify the code. These changes are only local to your browser.

**Q14: Can you explain the use of the Console tab in DevTools?**

**A14:** The Console tab lets you run JavaScript. This will be covered later in the session, in the context of CSS selectors.

**Q15: Can you explain the Network tab in DevTools?**

**A15:** The Network tab shows all external information the browser is fetching. For TDS, the "Fetch" tab is most useful, showing APIs, JSON code, and CSS files. It shows what the website is pulling from the server.

**Q16: Can we modify the content in the Network tab?**

**A16:** No, you can only modify the website's structure in the Elements tab.

**Q17: Can you explain the Network tab again, briefly?**

**A17:** The Network tab shows external information the browser is fetching from where the website is deployed. The "Fetch" tab is particularly useful for TDS, showing APIs, JSON, and CSS files.

**Q18: In a later Week 1 question, we need to find values within a specific div class. Will the JavaScript code work on the entire site, or just the specified area?**

**A18:** The JavaScript will work on the entire site because the DOM structure is a tree. However, you can use selectors to target specific elements within that structure.

**Q19: How are HTML and CSS connected? Do we need JavaScript to extract information?**

**A19:** HTML is the skeleton, JavaScript the muscles, and CSS the skin. JavaScript is used to extract information from the HTML code using CSS selectors (classes or IDs).

**Q20: Can you explain the later part of the code used to extract data?**

**A20:** The code uses a map function to iterate through a list of elements. `innerText` gives the text content of an element, while `innerHTML` gives the entire HTML code. `innerText` is generally preferred for data extraction.

**Q21: Are there other commands or attributes besides `innerText`?**

**A21:** Yes, there are other attributes. `text` is similar to `innerText`, but `innerText` is more reliable. Always use `innerText` if `text` doesn't work.

**Q22: How do classes and IDs work in CSS selectors?**

**A22:** Classes are generic and can be applied to multiple elements. IDs are unique to a single element. In CSS selectors, classes are prefixed with a dot (.), and IDs with a hash (#).

**Q23: While showing `innerText`, you used a command that neatly organized the movie list. Why?**

**A23:** The console organizes the output for readability, packing items into groups of 100. Otherwise, it would be a single, long array.

**Q24: How can I copy the entire list from the console?**

**A24:** Enclose the code in a `copy()` function. This copies the output to your clipboard.

**Q25: Does the developer tool only work on Chrome?**

**A25:** It works on Edge and other browsers. In Safari or Mozilla, right-click anywhere on the webpage and look for the "Inspect" option.

**Q26: Can we modify the content in the Network tab?**

**A26:** No, you can only modify the website's structure in the Elements tab. The Network tab shows what the browser is fetching, not what you can change.

**Q27: Can you explain the use of classes in more detail?**

**A27:** Classes allow you to apply CSS to your code. If you remove a class, the associated CSS styling is removed. Classes can be applied to multiple elements, while IDs are unique to a single element.

**Q28: Can we limit JavaScript selection to a specific chunk of HTML data?**

**A28:** No, JavaScript will work on the entire site unless you use selectors to target specific elements.

**Q29: What is the origin of the exercise to extract names from the meeting participants?**

**A29:** The instructor created this exercise to encourage participation. A random participant is selected to answer a question.

**Q30: Can we go back to the syntax we typed?**

**A30:** The syntax was `$$(".className").map(...)`. The `$$` selects elements with the specified class, and `map` iterates through them. The instructor demonstrates how to extract the movie names using this. The instructor also explains the difference between `innerText` and `innerHTML`. `innerText` returns only the text, while `innerHTML` returns the entire HTML code. `innerText` is generally preferred for data extraction. If `text` doesn't work, use `innerText`.

**Q31: Should the `innerText` be written exactly as it appears, or can we modify the case (e.g., make "T" lowercase)?**

**A31:** Use the text exactly as it appears.

**Q32: What is the role of npx in this context?**

**A32:** npx creates a separate environment for a project, installing dependencies locally without affecting other projects. It's an alternative to npm, which installs globally.

**Q33: Does npx run primarily on Linux?**

**A33:** npx works on both PowerShell and Bash, but sha256sum might not work on Windows. You can run the npx command separately and use sha256sum on the resulting file.

**Q34: While showing `innerText`, you made the movie list extremely neat. Why?**

**A34:** That's how the console presents the data, organizing it into groups of 100 for readability.

**Q35: How can I copy the entire list from the console?**

**A35:** Use the `copy()` function in the console to copy the output to your clipboard.

**Q36: What should we focus on when using the Elements, Console, and Network tabs?**

**A36:** For the Elements tab, focus on extracting data using CSS selectors (classes and IDs). The Console tab is used for running JavaScript, particularly for data scraping with CSS selectors. The Network tab shows what the browser is fetching. The instructor recommends exploring these tabs and having fun with them.
