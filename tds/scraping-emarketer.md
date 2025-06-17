## Scraping emarketer

In this live scraping session, we explore a real-life scenario where Straive had to scrape data from emarketer.com for a demo. This is a fairly realistic and representative way of how one might go about scraping a website.

[![Live scraping session](https://i.ytimg.com/vi_webp/ZzUsDE1XjhE/sddefault.webp)](https://youtu.be/ZzUsDE1XjhE
<youtube_summary>The discussion centers around a project to build a semantic search demo for Insider Intelligence, part of eMarketer, which has an extensive archive of about 7,000 articles spanning 369 pages. Their existing search uses keyword-based Elastic Search, which lacks semantic understanding. The proposal was to create a semantic search demo capable of understanding queries contextually.

Key steps included:

1. **Scraping Data**: Due to the unavailability of direct data, the team scraped the entire archive. This involved:
   - Collecting URLs from all archive pages (369 pages, each with ~20 articles).
   - Using Python scripts with libraries like httpx (preferred over requests for future async capabilities) and lxml for HTML parsing.
   - Implementing a caching mechanism ("cached get") to avoid re-downloading pages if already fetched, addressing impatience and efficiency.
   - Handling pagination and URL extraction carefully with XPath queries and filtering for relevant article links.
   - Managing HTTP redirects and errors gracefully.

2. **Extracting Content**:
   - From each article URL, the title (from a specific H1 class) and main content (within certain div classes) were extracted.
   - Trial and error was involved to identify the correct HTML elements excluding sidebars and unrelated content.
   - The extracted data was stored in JSON format for further processing.

3. **Semantic Search Demo**:
   - Using the scraped and processed data, a semantic search prototype was built to respond to queries like “Who are the top retailers?” by finding contextually relevant articles, not just keyword matches.
   - The demo quantified similarity scores and summarized responses based on the scraped content.

4. **Insights and Best Practices**:
   - Demonstrating a proof of concept (POC) significantly improves client conversion compared to presentations alone.
   - Key programming virtues highlighted: laziness (automation), impatience (efficient workflows), and hubris (confidence to try).
   - Troubleshooting tips emphasized:
     - Liberal use of print statements to verify values.
     - Using breakpoints for interactive debugging.
     - Rubber duck debugging—explaining problems aloud or to AI (like ChatGPT) to clarify issues and find solutions.
   - The use of AI tools like ChatGPT and GitHub Copilot accelerates development and debugging.
   - The importance of understanding code sufficiently to troubleshoot even without deep coding expertise, especially for students and team members collaborating with developers.

5. **Broader Reflections**:
   - The value of side projects or “Friday night experiments” to explore new ideas without pressure, which can lead to unexpected breakthroughs (e.g., Nobel Prize-winning discoveries).
   - Encouragement to persist with experiments and secondary projects as they can yield significant innovations.
   - Recognition that sometimes experiments may be initially dismissed (e.g., Ignoble Prize) but later gain high recognition.

Overall, the project demonstrated how quickly a semantic search capability could be developed and deployed using web scraping, caching, HTML parsing, and AI-assisted development, alongside practical debugging strategies and the value of exploratory side projects for innovation.</youtube_summary>
)

You'll learn:

- **Scraping**: How to extract data from web pages, including constructing URLs, fetching page content, and parsing HTML using packages like [`lxml`](https://lxml.de/) and [`httpx`](https://www.python-httpx.org/).
- **Caching**: Implementing a caching strategy to avoid redundant data fetching for efficiency and reliability.
- **Error Handling and Debugging**: Practical tips for troubleshooting, such as using liberal print statements, breakpoints for in-depth debugging, and the concept of "rubber duck debugging" to clarify problems.
- **LLMs**: Benefits of Gemini / ChatGPT for code suggestions and troubleshooting.
- **Real-World Application**: How quick proofs of concept to showcase capabilities to clients, emphasizing practice over theory.
