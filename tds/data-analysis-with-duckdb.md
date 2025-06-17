## Data Analysis with DuckDB

[![Data Analysis with DuckDB](https://i.ytimg.com/vi_webp/4U0GqYrET5s/sddefault.webp)](https://youtu.be/4U0GqYrET5s
<youtube_summary>The session discusses two technologies considered "no-brainers" for data analytics: the Parquet file format and DuckDB. Parquet is a columnar, binary, compressed file format managed by the Apache Foundation, much faster and smaller than CSV, JSON, or SQLite formats. It supports native typing, enabling faster reads and writes, and is roughly five times smaller than the nearest alternative. The only downside is that Parquet files are not human-readable, so CSV or JSON may be kept for human inspection.

DuckDB is a fast, low-memory SQL database optimized for analytics and built in Rust, bypassing Python's GIL and using columnar storage. It is significantly faster than pandas for complex operations, such as grouping and counting unique flight routes by delay buckets, offering up to 20x speed improvements and minimal memory usage. DuckDB can query data directly from Parquet or other files without loading everything into memory and integrates well with pandas, allowing seamless data frame conversions and SQL queries on Python variables.

The workshop involves running a Jupyter notebook (available at codedog.com/c/dubbWorkshop) that demonstrates these benefits by timing file reads/writes and queries on a large flight dataset. Participants are encouraged to run the notebook locally and on Google Colab, then upload their results for validation. The session also covers creating custom queries, joining datasets, and performing correlation analyses using DuckDB and pandas. Some users noted needing to install SQLAlchemy for certain operations.

In summary, the recommendation is to standardize on Parquet for data storage due to its speed and size advantages and to use DuckDB for analytics workloads for its superior performance over pandas, especially on large datasets. CSV, JSON, and XLSX should be avoided as analysis formats. The workshop aims to teach practical usage of these tools to speed up and simplify data analytics tasks.</youtube_summary>
)

You'll learn how to perform data analysis using DuckDB and Pandas, covering:

- **Parquet for Data Storage**: Understand why Parquet is a faster, more compact, and better-typed storage format compared to CSV, JSON, and SQLite.
- **DuckDB Setup**: Learn how to install and set up DuckDB, along with integrating it into a Jupyter notebook environment.
- **File Format Comparisons**: Compare file formats by speed and size, observing the performance difference between saving and loading data in CSV, JSON, SQLite, and Parquet.
- **Faster Queries with DuckDB**: Learn how DuckDB uses parallel processing, columnar storage, and on-disk operations to outperform Pandas in speed and memory efficiency.
- **SQL Query Execution in DuckDB**: Run SQL queries directly on Parquet files and Pandas DataFrames to compute metrics such as the number of unique flight routes delayed by certain time intervals.
- **Memory Efficiency**: Understand how DuckDB performs analytics without loading entire datasets into memory, making it highly efficient for large-scale data analysis.
- **Mixing DuckDB and Pandas**: Learn to interleave DuckDB and Pandas operations, leveraging the strengths of both tools to perform complex queries like correlations and aggregations.
- **Ranking and Filtering Data**: Use SQL and Pandas to rank arrival delays by distance and extract key insights, such as the earliest flight arrival for each route.
- **Joining Data**: Create a cost analysis by joining datasets and calculating total costs of flight delays, demonstrating DuckDB's speed in joining and aggregating large datasets.

Here are the links used in the video:

- [Data analysis with DuckDB - Notebook](https://drive.google.com/file/d/1Y9XSs-LeSz-ZmnQj4OGP-Q4yDkPJrmsZ/view)
- [Parquet file format](https://parquet.apache.org/) - a fast columnar storage format that's becoming a de facto standard for big data
- [DuckDB](https://duckdb.org/) - a fast in-memory database that's very good with large-scale analysis
- [Plotly Datasets](https://github.com/plotly/datasets/) - a collection of sample datasets for analysis. This includes the [Kaggle Flights Dataset](https://www.kaggle.com/datasets/usdot/flight-delays) that the notebook downloads as [2015_flights.parquet](https://github.com/plotly/datasets/raw/master/2015_flights.parquet)
