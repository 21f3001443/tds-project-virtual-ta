## Data Preparation in the Editor

[![Data preparation in the editor](https://i.ytimg.com/vi_webp/99lYu43L9uM/sddefault.webp)](https://youtu.be/99lYu43L9uM
<youtube_summary>The text explains how to perform basic data editing and processing using text editors like Visual Studio Code, using a JSON dataset as an example. The dataset contains an array of objects with fields such as city, product, and sales. Initially, the JSON is not human-readable, but using the "Format Document" command (Ctrl+Shift+P, then "format document"), it can be prettified for easier viewing.

To extract unique city names, the author demonstrates selecting the word "City" multiple times using multi-cursor/multi-select features (Ctrl+D to select next occurrences, Shift+Arrow keys to extend selection). Pressing Ctrl+F to find "City," then Alt+Enter selects all instances at once. Copying and pasting these selections into a new file extracts all city values (2,462 entries).

Next, the author sorts these city names alphabetically via the command palette (Ctrl+Shift+P, then "sort lines ascending") and removes duplicates using "delete duplicate lines," resulting in 150 unique city names. Some city names, like "Bangalore" and "Beijing," appear with various misspellings.

A smart search-and-replace is performed to fix misspellings. For example, searching for partial matches like "B NG" selects all variants of Bangalore (using Ctrl+F, Alt+Enter, Shift+End), then simultaneously replacing them with the correct spelling "Bangalore" via multi-cursor editing. This mass update changes all 2,500+ instances at once.

After replacement, the city list is extracted again, sorted, and duplicates removed, confirming only one correctly spelled "Bangalore" remains. This process shows that Visual Studio Code can be used for effective data cleansing—formatting, extracting fields, sorting, deduplicating, and bulk editing—primarily enabled by the multi-cursor/multi-select feature and built-in commands, without needing specialized data tools.</youtube_summary>
)

You'll learn how to use a text editor [Visual Studio Code](https://code.visualstudio.com/) to process and clean data, covering:

- **Format** JSON files
- **Find all** and multiple cursors to extract specific fields
- **Sort** lines
- **Delete duplicate** lines
- **Replace** text with multiple cursors

Here are the links used in the video:

- [City-wise product sales JSON](https://drive.google.com/file/d/1VEnKChf4i04iKsQfw0MwoJlfkOBGQ65B/view?usp=drive_link)
