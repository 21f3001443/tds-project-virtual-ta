## Data Analysis with SQL

[![Data Analysis with Databases](https://i.ytimg.com/vi_webp/Xn3QkYrThbI/sddefault.webp)](https://youtu.be/Xn3QkYrThbI
<youtube_summary>This session explores using SQL, specifically MySQL, combined with Python’s Pandas library to analyze relational databases, focusing on an anonymized Stats.StackExchange dataset hosted at relational-data.org. The database contains interconnected tables such as posts and users, linked by IDs, demonstrating database normalization to avoid data repetition. Using Pandas’ read_sql function along with SQLAlchemy, we connect to the MySQL database via a connection string, execute queries (e.g., fetching the first 10 posts), and handle dependencies like installing pymysql.

Key analyses include:
- Counting total posts (91,976) and identifying top users by post count, revealing an 80-20 distribution where the top 20% of users contribute 76% of posts.
- Investigating correlations between user attributes such as age and reputation, which showed almost no correlation (~1.7%), and between views and reputation, which showed a strong positive correlation (~89%).
- Performing linear regression using scipy to quantify that each additional view corresponds to about a 4-point increase in reputation.

The session emphasizes:
- Using SQL primarily for data retrieval and Pandas for analysis, but also leveraging SQL for aggregated calculations to reduce data transfer and improve efficiency.
- The capability of some databases (e.g., MySQL, DuckDB) to perform statistical functions like correlation directly within SQL queries.
- The growing importance of knowing how to ask for solutions (e.g., using ChatGPT) rather than memorizing syntax.
- Encouraging experimentation with SQLite, a popular embedded database stored as a single file and integrated with Python, especially relevant for exams.

Overall, the approach demonstrates integrating SQL and Python for effective data analysis, using public datasets, automated code assistance, and best practices in database querying and analytics.</youtube_summary>
)

You'll learn how to perform data analysis using SQL (via Python), covering:

- **Database Connection**: How to connect to a MySQL database using SQLAlchemy and Pandas.
- **SQL Queries**: Execute SQL queries directly from a Python environment to retrieve and analyze data.
- **Counting Rows**: Use SQL to count the number of rows in a table.
- **User Activity Analysis**: Query and identify top users by post count.
- **Post Concentration**: Determine if a small percentage of users contribute the majority of posts using SQL aggregation.
- **Correlation Calculation**: Calculate the Pearson correlation coefficient between user attributes such as age and reputation.
- **Regression Analysis**: Compute the regression slope to understand the relationship between views and reputation.
- **Handling Large Data**: Perform calculations on large datasets by fetching aggregated values from the database rather than entire datasets.
- **Statistical Analysis in SQL**: Use SQL as a tool for statistical analysis, demonstrating its power beyond simple data retrieval.
- **Leveraging AI**: Use ChatGPT to generate SQL queries and Python code, enhancing productivity and accuracy.

Here are the links used in the video:

- [Data analysis with databases - Notebook](https://colab.research.google.com/drive/1j_5AsWdf0SwVHVgfbEAcg7vYguKUN41o)
- [SQLZoo](https://www.sqlzoo.net/wiki/SQL_Tutorial) has simple interactive tutorials to learn SQL
- [Stats database](https://relational-data.org/dataset/Stats) that has an anonymized dump of [stats.stackexchange.com](https://stats.stackexchange.com/)
- [Pandas `read_sql`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)
- [SQLAlchemy docs](https://docs.sqlalchemy.org/)
