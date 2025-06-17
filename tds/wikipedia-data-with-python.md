## Wikipedia Data with Python

[![Wikipedia data with Wikimedia Python library](https://i.ytimg.com/vi_webp/b6puvm-QEY0/sddefault.webp)](https://youtu.be/b6puvm-QEY0
<youtube_summary>This tutorial explains how to use the Wikipedia library in Python to access and extract information from Wikipedia pages easily. First, install the library using pip and import it. You can search Wikipedia pages by keywords using the search function, which returns all pages containing the keyword. To get only the top important results, use the 'result' argument with the desired number of results.

To obtain a summary of a page, use the summary function; you can specify the number of sentences for a shorter summary. For the full Wikipedia page with sections and references, use the page function. The page object also allows you to retrieve the page URL, reference links, title images (as a list of image links), and tables from the article.

For tables, the content is stored as a list, and you can extract specific tables as HTML and then use pandas to read and process them. Note that the first table might be a table of contents, usually not needed.

Overall, this library simplifies scraping Wikipedia data compared to traditional methods like using requests and BeautifulSoup. It provides straightforward functions to search, summarize, access full pages, references, images, and tables efficiently.</youtube_summary>
)

You'll learn how to scrape data from Wikipedia using the `wikipedia` Python library, covering:

- **Installing and Importing**: Use pip install to get the Wikipedia library and import it with import wikipedia as wk.
- **Keyword Search**: Use the search function to find Wikipedia pages containing a specific keyword, limiting results with the results argument.
- **Fetching Summaries**: Use the summary function to get a concise summary of a Wikipedia page, limiting sentences with the sentences argument.
- **Retrieving Full Pages**: Use the page function to obtain the full content of a Wikipedia page, including sections and references.
- **Accessing URLs**: Retrieve the URL of a Wikipedia page using the url attribute of the page object.
- **Extracting References**: Use the references attribute to get all reference links from a Wikipedia page.
- **Fetching Images**: Access all images on a Wikipedia page via the images attribute, which returns a list of image URLs.
- **Extracting Tables**: Use the pandas.read_html function to extract tables from the HTML content of a Wikipedia page, being mindful of table indices.

Here are links and references:

- [Wikipedia Library - Notebook](https://colab.research.google.com/drive/1-w8Jo6xcQs2jK0NxNddPW4HVCZhXmTBe)
- Learn about the [`wikipedia` package](https://wikipedia.readthedocs.io/en/latest/)

**NOTE**: Wikipedia is constantly edited. The page may be different now from when the video was recorded. Handle accordingly.
