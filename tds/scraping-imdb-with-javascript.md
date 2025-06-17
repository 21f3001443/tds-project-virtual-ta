## Scraping IMDb with JavaScript

[![Scraping the IMDb with Browser JavaScript](https://i.ytimg.com/vi_webp/YVIKZqZIcCo/sddefault.webp)](https://youtu.be/YVIKZqZIcCo
<youtube_summary>The video tutorial demonstrates how to scrape IMDb's Top 250 movies list using only the browser and JavaScript, without any external tools. The IMDb Top 250 page (imdb.com/chart/top) lists the highest-rated movies by audience votes, such as "The Shawshank Redemption" rated 9.3 with 2.9 million votes.

The goal is to extract data like the movie title, year, duration, rating, number of votes, and the movie's link, and export this into a CSV or Excel spreadsheet.

Steps and key points covered:

1. **Access Developer Tools:** Press F12 (or right-click → Inspect) in Chrome or Edge to open the browser's developer tools and view the HTML structure.

2. **Inspect Elements:** Using the Elements tab, inspect the webpage elements to identify the container holding the list of movies. The UL element with class `IPC-metadata-list` contains all 250 movie items.

3. **Selecting Elements with JavaScript:** Use `document.querySelectorAll` or the shortcut `$$` to select all movie list items by their CSS classes. This returns a list of 250 movie elements.

4. **Extracting Data:** 
   - Use `.map()` and arrow functions to iterate through each item.
   - Use `item.querySelector` to find sub-elements like the title (`.IPC-title-text`), year, duration, rating, votes, and links.
   - Extract text content with `.textContent` and attributes like `href` for links.
   - Handle cases where some data may be missing using the optional chaining operator `?.` to avoid errors.

5. **Data Structure:** Gather extracted data into an array of arrays where each inner array holds the data fields for a movie.

6. **Copying Data:** Use the browser `copy()` function to copy the resulting array to the clipboard.

7. **Converting to Spreadsheet:** 
   - Paste the copied JavaScript array (which resembles JSON) into an online JSON-to-CSV or JSON-to-Excel converter.
   - Download or copy the CSV and open it in Excel.
   - Clean up the data using Excel features like "Text to Columns" to separate votes and viewers, removing unwanted characters or spaces.

8. **Summary of JavaScript Functions Used:**
   - `$$` as alias for `document.querySelectorAll`
   - `.map()` for transforming lists
   - Arrow functions `(item) => ...` for concise callbacks
   - `.querySelector()` for selecting child elements
   - Optional chaining operator `?.` for safe property access
   - `copy()` to copy data to clipboard

The tutorial emphasizes that this approach is quick, requires only browser tools and JavaScript knowledge, and avoids the need for external scraping tools. It also notes that the webpage structure may change over time, which could require adjustments in selectors.</youtube_summary>
)

You'll learn how to scrape the [IMDb Top 250 movies](https://www.imdb.com/chart/top) directly in the browser using JavaScript on the Chrome DevTools, covering:

- **Access Developer Tools**: Use F12 or right-click > Inspect to open developer tools in Chrome or Edge.
- **Inspect Elements**: Identify and inspect HTML elements using the Elements tab.
- **Query Selectors**: Use `document.querySelectorAll` and `document.querySelector` to find elements by CSS class.
- **Extract Text Content**: Retrieve text content from elements using JavaScript.
- **Functional Programming**: Apply [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
  and [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
  for concise data processing.
- **Data Structuring**: Collect and format data into an array of arrays.
- **Copying Data**: Use the copy function to transfer data to the clipboard.
- **Convert to Spreadsheet**: Use online tools to convert JSON data to CSV or Excel format.
- **Text Manipulation**: Perform text splitting and cleaning in Excel for final data formatting.

Here are links and references:

- [IMDB Top 250 movies](https://www.imdb.com/chart/top/)
- [Learn about Chrome Devtools](https://developer.chrome.com/docs/devtools/overview/)
