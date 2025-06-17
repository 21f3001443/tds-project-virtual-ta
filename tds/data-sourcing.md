# Data Sourcing

Before you do any kind of data science, you obviously have to get the data to be able to analyze it, visualize it, narrate it, and deploy it.
And what we are going to cover in this module is how you get the data.

There are three ways you can get the data.

1. The first is you can **download** the data. Either somebody gives you the data and says download it from here, or you are asked to download it from the internet because it's a public data source. But that's the first way—you download the data.
2. The second way is you can **query it** from somewhere. It may be on a database. It may be available through an API. It may be available through a library. But these are ways in which you can selectively query parts of the data and stitch it together.
3. The third way is you have to **scrape it**. It's not directly available in a convenient form that you can query or download. But it is, in fact, on a web page. It's available on a PDF file. It's available in a Word document. It's available on an Excel file. It's kind of structured, but you will have to figure out that structure and extract it from there.

In this module, we will be looking at the tools that will help you either download from a data source or query from an API or from a database or from a library. And finally, how you can scrape from different sources.

[![Data Sourcing - Introduction](https://i.ytimg.com/vi_webp/1LyblMkJzOo/sddefault.webp)](https://youtu.be/1LyblMkJzOo
<youtube_summary>This module covers the three main ways to acquire data for data science: downloading, querying, and scraping.

1. Downloading Data: You can download datasets directly from sources like Kaggle, data.world, or the Internet Movie Database (IMDB). For example, IMDB provides a comprehensive movie dataset available as gzipped TSV files, containing detailed information about movies, actors, directors, and crew. Analyzing such bulk data allows insights like movie ratings, popularity, and trends over time, such as the evolution of animation movies across decades.

2. Querying Data via APIs or Databases: When bulk downloads are unavailable, data can be obtained by querying databases or APIs. An example is using Google’s undocumented API to retrieve trending "how to" search queries by region, providing insights into public interests without costly surveys. By changing query parameters, one can gather and analyze search trends for different countries, revealing varying public concerns and interests.

3. Scraping Data: When data isn’t available in convenient formats or APIs, scraping becomes necessary. This involves extracting structured data from web pages, PDFs, or documents. For instance, scraping cricket statistics from a website like HowStat using Python’s Beautiful Soup library enables compiling player performance data across multiple pages. This scraped data can be analyzed to identify top players by strike rates, runs scored, and performance against specific opponents or venues.

The module also introduces practical tools and examples for each method, including downloading datasets, querying APIs like the nominatim API for geolocation or the BBC weather API, and scraping from various sources. The goal is to equip learners with the skills to gather required data efficiently for further analysis, visualization, and deployment in data science projects.</youtube_summary>
)

Here are links used in the video:

- [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
- [IMDb Datasets](https://imdb.com/interfaces/)
- [Download the IMDb Datasets](https://datasets.imdbws.com/)
- [Explore the Internet Movie Database](https://gramener.com/imdb/)
- [What does the world search for?](https://gramener.com/search/)
- [HowStat - Cricket statistics](https://howstat.com/cricket/home.asp)
- [Cricket Strike Rates](https://gramener.com/cricket/)
