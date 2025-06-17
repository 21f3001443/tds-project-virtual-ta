## Scraping with Excel

[![Weather Scraping with Excel: Get the Data](https://i.ytimg.com/vi_webp/OCl6UdpmzRQ/sddefault.webp)](https://youtu.be/OCl6UdpmzRQ
<youtube_summary>This exercise demonstrates how to import and refresh web data in Excel using the query feature from the Data tab. The example involves importing a two-week weather forecast for Chennai from timeanddate.com. The steps are:

1. Navigate to the desired webpage (timeanddate.com, weather, two-week forecast for Chennai) and copy the URL.
2. In Excel, go to the Data tab, select New Query > From Other Sources > From Web, and paste the copied URL.
3. Excel establishes a connection and opens the Query Editor, showing both the webpage view and available tables.
4. Select the appropriate table containing the forecast data (Table 0).
5. You can either transform the data immediately or load it first and then edit the query later by double-clicking it.
6. In the Query Editor, remove unnecessary columns (e.g., conditions, comfort, humidity, precipitation chance, Sun UV, sunrise, sunset) using the applied steps pane, which tracks all transformations sequentially.
7. Close and load the cleaned data into Excel.
8. To update the data with the latest forecast, use the Refresh option from the Data tab or right-click the table and select Refresh.
   
This process allows continuous access to up-to-date web data for further analysis within Excel.</youtube_summary>
)

You'll learn how to [import tables on the web using Excel](https://support.microsoft.com/en-au/office/import-data-from-the-web-b13eed81-33fe-410d-9247-1747269c28e4), covering:

- **Data Import from Web**: Use the query feature in Excel to scrape data from websites.
- **Establishing Web Connections**: Connect Excel to a web page using a URL.
- **Using Query Editor**: Navigate the query editor to view and manage web data tables.
- **Loading Data**: Load data from the web into Excel for further manipulation.
- **Data Transformation**: Remove unnecessary columns and transform data as needed.
- **Applying Transformations**: Track applied steps in the sequence for reproducibility.
- **Refreshing Data**: Refresh the imported data to get the latest updates from the web.

Here are links used in the video:

- [Chennai Weather Forecast](https://www.timeanddate.com/weather/india/chennai/ext)
- [Excel Scraping Workbook](https://docs.google.com/spreadsheets/d/1a12ApZMD6CTiKRyO4RuauOO8IdYgACRL/view)

If you use Excel on Mac, the process is a bit different. See [Importing External Data Into Excel on Mac](https://youtu.be/PuqVoVNWF20
<youtube_summary>This tutorial explains how to import external data, specifically Apple stock prices, into Excel on a Mac, as the Windows workflow differs. The goal is to avoid logging into a broker repeatedly by having live stock data in Excel.

Steps:

1. Find a webpage with current stock data, e.g., Yahoo Finance, and copy the URL for the Apple stock page.
2. Open a blank Word document, paste the URL, and ensure it is recognized as a hyperlink (press Enter twice if needed).
3. Save the Word document as a plain text file, but change the file extension from ".txt" to ".iqy"—the format Excel requires to import web queries.
4. In the save dialog, select "Mac OS CR only" and "Left to Right" text direction; default settings usually suffice.
5. Open Excel, go to the desired sheet, then to the Data tab, select "Get External Data," and choose "Run Saved Query."
6. Locate and select your saved .iqy file, then click "Get Data." Excel will import the stock data into the sheet, which may take a few seconds.
7. Since imported data may contain non-numeric characters (e.g., letters mixed with prices), use Excel’s LEFT function to extract only the numeric portion needed for calculations (e.g., =LEFT(cell,7)).
8. To update the data regularly, use the "Refresh All" button under the Data tab; Excel will retrieve the latest stock prices from the web.

Note: The example uses German webpage content, but the method applies generally. The tutorial emphasizes that market data will only update during trading days. The presenter invites viewers to like or subscribe for more Excel tutorials.</youtube_summary>
).
