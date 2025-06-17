## Scraping with Google Sheets

[![Scraping with Google Sheets](https://i.ytimg.com/vi_webp/eYQEk7XJM7s/sddefault.webp)](https://youtu.be/eYQEk7XJM7s
<youtube_summary>The video explains how to import data from tables on the web into Google Sheets using the IMPORTHTML formula. The formula syntax is =IMPORTHTML(URL, query, index), where the URL is the web page to pull data from, the query specifies whether to select a "table" or "list," and the index determines which table or list to import (e.g., first table, fourth table). 

An example is shown using a Wikipedia page with multiple tables; selecting the correct index number retrieves the desired table. Another example imports the list of highest-grossing Indian films from a Wikipedia page using the first table. The imported data cannot be sorted directly since it is the result of a formula, so it must be copied and pasted as values before sorting.

The video also notes that the IMPORTHTML formula is live, meaning it updates automatically if the source webpage changes. Other related Google Sheets functions mentioned include IMPORTXML (for structured data like XML, HTML, or APIs using XPath queries), IMPORTFEED (for RSS or Atom feeds), IMPORTRANGE (to import data from another spreadsheet), and IMPORTDATA (for CSV or TSV files). Among these, IMPORTHTML is highlighted as the most commonly used for web data scraping in Google Sheets.</youtube_summary>
)

You'll learn how to [import tables on the web using Google Sheets's `=IMPORTHTML()` formula](https://support.google.com/docs/answer/3093339?hl=en), covering:

- **Import HTML Formula**: Use =IMPORTHTML(URL, "query", index) to fetch tables or lists from a web page.
- **Granting Access**: Allow access for formulas to fetch data from external sources.
- **Checking Imported Data**: Verify if the imported table matches the data on the web page.
- **Handling Errors**: Understand common issues and how to resolve them.
- **Sorting Data**: Copy imported data as values and sort it within Google Sheets.
- **Freezing Rows**: Use frozen rows to maintain headers while sorting.
- **Live Formulas**: Learn how web data updates automatically when the source changes.
- **Other Import Functions**: IMPORTXML, IMPORTFEED, IMPORTRANGE, and IMPORTDATA for advanced data fetching options.

Here are links used in the video:

- [Google sheet used in the video](https://docs.google.com/spreadsheets/d/1Qp_YTh1-hJHxjMWE_GofkvLIKgEdKxb6NFImpId3z9o/view)
- [`IMPORTHTML()`](https://support.google.com/docs/answer/3093339)
- [`IMPORTXML()`](https://support.google.com/docs/answer/3093342)
- [Demographics of India](https://en.wikipedia.org/wiki/Demographics_of_India)
- [List of highest grossing Indian films](https://en.wikipedia.org/wiki/List_of_highest-grossing_Indian_films)
