## Database: SQLite

Relational databases are used to store data in a structured way. You'll often access databases created by others for analysis.

PostgreSQL, MySQL, MS SQL, Oracle, etc. are popular databases. But the most installed database is [SQLite](https://www.sqlite.org/index.html). It's embedded into many devices and apps (e.g. your phone, browser, etc.). It's lightweight but very scalable and powerful.

Watch these introductory videos to understand SQLite and how it's used in Python (34 min):

[![SQLite Introduction - Beginners Guide to SQL and Databases (22 min)](https://i.ytimg.com/vi_webp/8Xyn8R9eKB8/sddefault.webp)](https://youtu.be/8Xyn8R9eKB8
<youtube_summary>This video is an introduction to SQLite by Caleb, highlighting its importance as an embedded, serverless database widely used in mobile phones, computers, and various applications. SQLite is favored for software distributed across many instances, such as desktop software, IoT devices, and appliances, rather than centralized web applications. It is free for commercial use and supports many use cases, though for web development, other databases like PostgreSQL might be preferred.

Caleb demonstrates how to install SQLite using Homebrew on Mac or via the official download page for other systems. He explains basic SQLite terminal commands, especially the dot (.) commands for database management that are not SQL, such as `.clear`, `.tables`, `.schema`, and `.databases`.

The tutorial covers core SQL commands to create, alter, and drop tables (DDL) using a users table example with columns like id (primary key), name, username (unique), email, age, and created_at (timestamp with default current time). Caleb recommends working with SQL files rather than directly in the terminal for ease of editing and reusability, demonstrated using Visual Studio Code.

He then moves to Data Manipulation Language (DML) commands: inserting data (with required fields like name and username), selecting data with filters (e.g., WHERE clause, LIMIT, ORDER BY), updating data with care to use WHERE to avoid updating all rows, and deleting data correctly with the `delete from` syntax.

Caleb introduces foreign keys for relational database design by creating a posts table linked to users via a user_id foreign key, explaining how to insert data referencing users. He shows how to query related data with JOINs to combine posts and user info, using table aliases for convenience.

To simplify repeated complex joins, Caleb demonstrates creating a VIEW named posts_info that acts as a virtual table combining posts and user details, making future queries easier.

He encourages viewers to explore more advanced SQLite features and upcoming videos on using SQLite from applications like Node.js. Caleb also offers free software development intro courses via Course Careers, provides links to ad-free videos and code on GitHub, and requests support through likes, subscriptions, and sharing.

In summary, the video provides a comprehensive beginner-friendly overview of SQLite installation, basic commands, table creation and modification, data insertion and querying, relational design with foreign keys and joins, and using views to simplify queries, preparing viewers to further explore SQLite development.</youtube_summary>
)

[![SQLite Backend for Beginners - Create Quick Databases with Python and SQL (13 min)](https://i.ytimg.com/vi_webp/Ohj-CqALrwk/sddefault.webp)](https://youtu.be/Ohj-CqALrwk
<youtube_summary>This tutorial introduces SQLite, a serverless, simple database library that uses standard SQL commands. The example uses Python and a list of GTA game releases, each stored as a tuple with release year, name, and fictional city. The tutorial covers:

1. Creating a SQLite database by importing sqlite3 and connecting to a database file (e.g., gta.db).
2. Creating a cursor object for executing SQL commands.
3. Creating a table named "gta" with columns for release year (integer), release name (text), and city (text).
4. Inserting multiple rows into the table using cursor.executemany() with placeholders.
5. Running the Python script to generate and populate the database file.
6. Selecting and printing all rows from the gta table to verify data insertion.
7. Filtering query results to select only rows where the city is "Liberty City" using parameterized queries and fetching results.
8. Creating a second table "cities" to map fictional GTA cities to their real-life counterparts (e.g., Liberty City to New York).
9. Inserting data into the cities table and selecting from it.
10. Combining data from both tables by replacing "Liberty City" in query results with "New York" using Python list comprehension.
11. The tutorial concludes by mentioning upcoming tutorials on web scraping to populate databases automatically and connecting the database to a Flask web application.

The tutorial emphasizes practical code examples, running scripts via IDE or terminal, and encourages liking, commenting, subscribing, and sharing.</youtube_summary>
)

There are many non-relational databases (NoSQL) like [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html), [MongoDB](https://www.mongodb.com/docs/manual/), [Redis](https://redis.io/docs/latest/), etc. that you should know about and we may cover later.

Core Concepts:

```sql
-- Create a table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert data
INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com');

-- Query data
SELECT name, COUNT(*) as count
FROM users
GROUP BY name
HAVING count > 1;

-- Join tables
SELECT u.name, o.product
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.status = 'pending';
```

Python Integration:

```python
import sqlite3
from pathlib import Path
import pandas as pd

async def query_database(db_path: Path, query: str) -> pd.DataFrame:
    """Execute SQL query and return results as DataFrame.

    Args:
        db_path: Path to SQLite database
        query: SQL query to execute

    Returns:
        DataFrame with query results
    """
    try:
        conn = sqlite3.connect(db_path)
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()

# Example usage
db = Path('data.db')
df = await query_database(db, '''
    SELECT date, COUNT(*) as count
    FROM events
    GROUP BY date
''')
```

Common Operations:

1. **Database Management**

   ```sql
   -- Backup database
   .backup 'backup.db'

   -- Import CSV
   .mode csv
   .import data.csv table_name

   -- Export results
   .headers on
   .mode csv
   .output results.csv
   SELECT * FROM table;
   ```

2. **Performance Optimization**

   ```sql
   -- Create index
   CREATE INDEX idx_user_email ON users(email);

   -- Analyze query
   EXPLAIN QUERY PLAN
   SELECT * FROM users WHERE email LIKE '%@example.com';

   -- Show indexes
   SELECT * FROM sqlite_master WHERE type='index';
   ```

3. **Data Analysis**

   ```sql
   -- Time series aggregation
   SELECT
       date(timestamp),
       COUNT(*) as events,
       AVG(duration) as avg_duration
   FROM events
   GROUP BY date(timestamp);

   -- Window functions
   SELECT *,
       AVG(amount) OVER (
           PARTITION BY user_id
           ORDER BY date
           ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
       ) as moving_avg
   FROM transactions;
   ```

Tools to work with SQLite:

- [SQLiteStudio](https://sqlitestudio.pl/): Lightweight GUI
- [DBeaver](https://dbeaver.io/): Full-featured GUI
- [sqlite-utils](https://sqlite-utils.datasette.io/): CLI tool
- [Datasette](https://datasette.io/): Web interface
