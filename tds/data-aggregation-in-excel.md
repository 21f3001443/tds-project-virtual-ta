## Data Aggregation in Excel

[![Data aggregation in Excel](https://i.ytimg.com/vi_webp/NkpT0dDU8Y4/sddefault.webp)](https://youtu.be/NkpT0dDU8Y4
<youtube_summary>The exercise demonstrates data aggregation and visualization using Excel pivot tables with a COVID-19 dataset containing new cases, total cases, new deaths, and total deaths for various countries. 

1. **Data Cleanup:** 
   - Remove empty columns and rows with missing values, especially focusing on the "new cases" column since the analysis centers on it.
   - Use Excel's "Find and Select" with "Blanks" to locate and delete rows with blank cells in critical columns.

2. **Data Manipulation:** 
   - Convert the cleaned data into an Excel table for easier management and automatic formula application.
   - Extract week, month, and year from the date column using Excel functions (`WEEKNUM`, `TEXT`) to create new columns for aggregation purposes.
   - Adjust data types and formatting (e.g., remove decimal places, set month format to "mmm", year to "yyyy").

3. **Color Scales:** 
   - Apply conditional formatting with 3-color scales on the new cases column to visually identify clusters of low (green), medium (yellow), and high (red) new case counts.
   - This visualization helps quickly spot trends and clusters in the data when zoomed out.

4. **Pivot Table Creation:** 
   - Insert a pivot table to aggregate new cases by country and week.
   - Drag location to rows, week to columns, and sum of new cases to values.
   - Add year as a filter or row field to separate data by year.
   - Pivot tables allow changing aggregation methods like average, maximum, etc.

5. **Sparklines:** 
   - Create sparklines (mini line charts) in the pivot table to visualize weekly trends in new cases for each country by year.
   - Customize sparklines by increasing line weight and adding markers for high and low points.
   - Sparklines reveal trends and patterns in new cases over time that may not be obvious from raw numbers.

6. **Data Bars:** 
   - Use another pivot table aggregated by month and country, including year.
   - Apply conditional formatting with data bars (gradient or solid fill) to graphically illustrate new case volumes.
   - Data bars visually depict waves and peaks of new cases across months and countries, showing timing and intensity differences by year.

Overall, the exercise covers cleaning and preparing COVID-19 data, manipulating date information for aggregation, and using Excel features—color scales, pivot tables, sparklines, and data bars—to summarize and visualize trends in new COVID-19 cases across countries and time periods effectively.</youtube_summary>
)

You'll learn data aggregation and visualization techniques in Excel, covering:

- **Data Cleanup**: Remove empty columns and rows with missing values.
- **Creating Excel Tables**: Convert raw data into tables for easier manipulation and formula application.
- **Date Manipulation**: Extract week, month, and year from date columns using Excel functions (WEEKNUM, TEXT).
- **Color Scales**: Apply color scales to visualize clusters and trends in data over time.
- **Pivot Tables**: Create pivot tables to aggregate data by location and date, summarizing values weekly and monthly.
- **Sparklines**: Use sparklines to visualize trends within pivot tables, making data patterns more apparent.
- **Data Bars**: Implement data bars for graphical illustrations of numerical columns, showing trends and waves.

Here are links used in the video:

- [COVID-19 data Excel file - raw data](https://docs.google.com/spreadsheets/d/14HLgSmME95q--6lcBv9pUstqHL183wTd/view)
