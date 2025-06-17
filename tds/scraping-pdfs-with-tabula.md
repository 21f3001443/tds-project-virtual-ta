## Scraping PDFs with Tabula

[![Scrape PDFs with Tabula Python library](https://i.ytimg.com/vi_webp/yDoKlKyxClQ/sddefault.webp)](https://youtu.be/yDoKlKyxClQ
<youtube_summary>The session explains how to scrape PDFs from a given URL and extract tables from them using Python. It begins by highlighting the importance of data sourcing and preparation in data science. The tutorial focuses on downloading multiple PDFs from a URL hosting them, using the Beautiful Soup library to parse the webpage and find PDF links, and saving these PDFs to a specified location, such as a Google Drive folder mounted in a Colab environment. The example URL used is a Premier League page containing about 50 PDFs related to different seasons.

The code creates a Beautiful Soup object to parse the URL, then loops through all links ending with ".pdf," extracting each file name from the link and downloading the file to the designated folder. After downloading, the tutorial demonstrates extracting tabular data from a specific PDF using the Tabula library, which reads tables from PDFs into structured formats like CSV or Excel. 

The example PDF is "pl interactivecombine.pdf," from which a table on page 18 showing the final club standings is extracted. Initial attempts to extract the table capture unwanted text due to the PDF’s landscape layout and multiple tables. To refine this, the tutorial uses Tabula’s ability to specify the exact area (coordinates) on the page to extract only the desired table. The coordinates can be obtained using image software by identifying pixel positions.

After extracting the table and saving it as a CSV file, the data is read back into a dataframe. Some unwanted rows appear, such as extra lines under "Newcastle United" related to club badges and notes (e.g., "125 years old"), which will require further cleaning. The session concludes by emphasizing that using Beautiful Soup and Tabula together enables efficient scraping of PDFs from URLs and extraction of specific tables for further data analysis.</youtube_summary>
)

You'll learn how to scrape tables from PDFs using the `tabula` Python library, covering:

- **Import Libraries**: Use Beautiful Soup for URL parsing and Tabula for extracting tables from PDFs.
- **Specify Save Location**: Mount Google Drive to save scraped PDFs.
- **Identify PDF URLs**: Parse the given URL to identify and select all PDF links.
- **Download PDFs**: Loop through identified links, saving each PDF to the specified location.
- **Extract Tables**: Use Tabula to read tabular content from the downloaded PDFs.
- **Control Extraction Area**: Specify page and area coordinates to accurately extract tables, avoiding extraneous text.
- **Save Extracted Data**: Convert the extracted table data into structured formats like CSV for further analysis.

Here are links and references:

- [PDF Scraping - Notebook](https://colab.research.google.com/drive/102Fv2Ji0J4mvao3mCse52E7Th8bZiuyf)
- Learn about the [`tabula` package](https://tabula-py.readthedocs.io/en/latest/tabula.html)
- Learn about the [`pandas` package](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html). [Video](https://youtu.be/vmEHCJofslg
<youtube_summary>This video tutorial provides a comprehensive introduction to the Python pandas library, emphasizing its usefulness for data science tasks compared to Excel, particularly due to its flexibility and ability to handle large datasets. The tutorial begins by guiding viewers to install pandas via pip and download a Pokémon dataset from the creator’s GitHub, which is used throughout the video for demonstrations.

Key topics covered include:

1. **Loading Data:** Instructions on importing pandas, loading CSV, Excel, and tab-separated files into pandas DataFrames, and viewing data using functions like `.head()` and `.tail()`.

2. **Exploring Data:** How to inspect DataFrame columns, select single or multiple columns, and access rows using `.iloc` and `.loc`. Iterating through rows with `.iterrows()` is also shown.

3. **Filtering Data:** Using `.loc[]` with conditions (including multiple conditions using `&` for AND and `|` for OR), string containment with `.str.contains()`, and regular expressions for advanced text filtering. Case-insensitive filtering using regex flags is demonstrated.

4. **Modifying Data:** Adding new columns by summing existing columns, dropping columns, reordering columns, and safely handling data manipulation to avoid errors. Examples include creating a "total" stats column for Pokémon.

5. **Saving Data:** Exporting DataFrames to CSV, Excel, and tab-separated text files with options to exclude the index column.

6. **Advanced Filtering and Conditional Updates:** Changing column values based on conditions, modifying multiple columns simultaneously, and resetting the DataFrame to a checkpoint by reloading the CSV.

7. **Grouping and Aggregation:** Using `.groupby()` to compute aggregate statistics like mean, sum, and count grouped by columns (e.g., Pokémon type), sorting grouped results, and understanding use cases for aggregation.

8. **Handling Large Datasets:** Reading large CSV files in chunks to manage memory efficiently, processing each chunk with groupby operations, and concatenating results to build a summary DataFrame.

Throughout, the instructor emphasizes best practices such as verifying calculations, avoiding hard-coded indices when possible, and consulting pandas documentation. The video is designed both for beginners starting from scratch and intermediate users seeking specific pandas techniques. The creator encourages viewers to subscribe for future tutorials covering plotting and more advanced pandas and Python features and invites questions and suggestions in the comments.

Overall, the tutorial equips viewers with foundational and some advanced pandas skills for effective data manipulation, filtering, aggregation, and handling large datasets using Python.</youtube_summary>
)
