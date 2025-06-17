# Live Session: 23 Jan 2025

[![2025-01-23 Week 3 - Session 4 - TDS Jan 25](https://i.ytimg.com/vi_webp/TxGY540ru3A/sddefault.webp)](https://youtu.be/TxGY540ru3A
<youtube_summary>The discussion covered several technical topics including solving programming questions using bash and Python, Git and GitHub usage, SQL basics, and developing and deploying Flask applications.

1. **Solving Questions with Bash and Python:**
   - Participants discussed solving file renaming tasks across directories using a combination of bash commands (like `find` and `mv`) and Python scripts.
   - The Python script used the `os` module to list files, create a translation table to increment numbers in filenames, and rename files accordingly.
   - The bash `find` command with `-exec` was used to move all files from nested directories into a single folder.

2. **Git and GitHub:**
   - Git initialization (`git init`), adding files (`git add .`), committing with messages (`git commit -m "message"`), and pushing to GitHub were explained.
   - The importance of `.gitignore` to exclude files/folders like virtual environments (`EnV`) from Git tracking was emphasized.
   - VS Code's source control tab was demonstrated as a GUI method to commit and push changes.
   - Git commands to list commits and view file differences (`git diff`) were shown.
   - Using GitHub for continuous integration and continuous deployment (CI/CD) with platforms like Vercel was discussed.

3. **SQL Basics:**
   - SQL (Structured Query Language) was introduced as a language to query data from databases.
   - Basic SQL commands such as `SELECT`, `FROM`, and `WHERE` were explained.
   - It was noted that only basic extraction commands are necessary for the course, and full database management commands (like `INSERT` or `CREATE TABLE`) are not required.
   - Resources like SQL Zoo were recommended for learning SQL basics.
   - The relevance of SQL for data analytics and modern databases like DuckDB was mentioned.

4. **Flask Web Application Development and Deployment:**
   - Flask, a Python web framework, was introduced for creating web applications and APIs.
   - A sample Flask app was developed that takes a user's year of birth as input and returns their generational cohort (Millennials, Gen Z, Gen Alpha, etc.) as a JSON response.
   - The use of route decorators to create endpoints and handling URL parameters was shown.
   - The concept of virtual environments was explained, including their creation (`python -m venv EnV`), activation, and why to exclude them from GitHub.
   - The process of setting up a GitHub repository and pushing Flask code was demonstrated.
   - Deployment on Vercel was covered, including creating `requirements.txt` using `pip freeze > requirements.txt` and configuring `vercel.json` for build instructions.
   - The automatic redeployment feature of Vercel (CI/CD) was highlighted.
   - Ngrok was briefly discussed as a tool for tunnel forwarding to expose local servers to the internet, but permanent deployment was preferred.
   - An assignment was given to create a Flask app that returns a zodiac sign based on the user's month or date of birth.
   - The session concluded with reminders about accessing live session recordings and encouragement to deploy Flask apps on platforms like Vercel or Netlify.

5. **Database Deployment:**
   - It was shared that databases like PostgreSQL, MongoDB, and Redis can be deployed on Vercel, including in free plans.
   - Integration of cloud databases such as Supabase was mentioned to support full-stack applications.

Overall, the session provided a comprehensive walkthrough of using bash and Python for file operations, Git for version control, SQL basics for data querying, and Flask for web development and deployment, along with practical tips and assignments to reinforce learning.</youtube_summary>
)

**Q1: How can I compare two files using the command line?**

**A1:** You can use the `diff` command in bash, or the `git diff` command if you've initialized a git repository. The `diff` command shows the differences between two files directly. `git diff` compares commits in a git repository.

**Q2: I'm having trouble viewing my GA1. It's showing zero ones. Can you help?**

**A2:** Let's look at your screen. It appears there are different timestamps. I'll help you troubleshoot.

**Q3: How can I move files from multiple subfolders into a single folder using the command line?**

**A3:** I used a bash script that combines the `find` command (to locate files of a specific type, like `.txt` files) and the `mv` command (to move them). The `find` command searches the current directory (`./`) for files (`-type f`) and the `-exec` option executes the `mv` command on each file found. The curly braces `{}` are placeholders for the filenames.

**Q4: Will knowing only six SQL commands (SELECT, FROM, GROUP BY, etc.) be enough to complete this course?**

**A4:** You'll only need basic SQL for this course, mainly for extracting data. We're not covering a full DBMS course. A good resource to learn more is SQLZoo. While you might not need more than six commands for this course, ChatGPT can help if you encounter more complex SQL queries.

**Q5: How can I deploy a Flask application to Vercel?**

**A5:** First, set up a git repository and connect it to your GitHub account. Then, create a virtual environment for your Python project using `python -m venv <env_name>`. Activate it using the appropriate script (e.g., `.\env\Scripts\activate`). Install Flask using `pip install flask`. Create a `.gitignore` file to exclude the virtual environment folder. Then, create a `vercel.json` file with build instructions for Vercel. Commit and push your code to GitHub. Finally, add your project to Vercel, selecting the correct repository and build settings (Python, not Node). Vercel will automatically redeploy your application whenever you push changes to GitHub. This is called CI/CD (Continuous Integration/Continuous Deployment).

**Q6: What does the port number matter when deploying to Vercel?**

**A6:** When deploying to Vercel, the port number you use locally doesn't matter because Vercel will assign your application its own domain. You should remove `debug=True` from your Flask application before deploying to production.

**Q7: Why do I need administrator permissions to use ngrok?**

**A7:** ngrok is a command-line tool that forwards requests to your local host. It doesn't need to be installed in your virtual environment. However, you might need administrator privileges to forward requests through a port. If you encounter permission issues, try running PowerShell as administrator.

**Q8: What is ngrok and how does it work?**

**A8:** ngrok creates a public URL that forwards requests to your locally running application. This allows anyone on the internet to access your application, even though it's running on your local machine. Your computer acts as a server. Note that ngrok only works while your local server is running. For a permanent solution, deploy to a platform like Vercel or Netlify.

**Q9: What is a virtual environment and why is it useful?**

**A9:** A virtual environment creates a separate, isolated environment for your project. This prevents conflicts between different project dependencies. Think of it like creating a separate section in a swimming pool for a child, where the depth is less than the main pool. You can install libraries (like Flask and Pandas) within the virtual environment without affecting your global Python packages.

**Q10: What is the assignment?**

**A10:** Create a Flask application that takes a user's birth month as input and returns their zodiac sign. This is a fun exercise to improve your Flask skills. You can deploy it to Vercel or Netlify and share the link. Remember to create a `.gitignore` file to exclude the virtual environment folder.
