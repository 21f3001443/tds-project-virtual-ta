## Web Scraping with Playwright in Python

Scrape JavaScript‑heavy sites effortlessly with Playwright.

[![🤖 Playwright: Advanced Web Scraping in Python (14 min)](https://i.ytimg.com/vi_webp/biFzRHk4xpY/sddefault.webp)](https://youtu.be/biFzRHk4xpY
<youtube_summary>The video from Vincent Codes Finance demonstrates how to use Python and Playwright to scrape a webpage and convert the data into a pandas dataframe, even when the webpage’s source code lacks the actual table data. Playwright, a Microsoft web testing framework, provides a headless browser (Chromium, Firefox, or WebKit) controlled by code, which can execute JavaScript and render modern webpages that dynamically load data, making it suitable for scraping dynamic content. It also supports features like authentication and form interactions.

The tutorial first attempts scraping using the simpler requests package but encounters issues because the data (e.g., stock quotes from the NASDAQ 100 on the NASDAQ website) is loaded dynamically via JavaScript and not present in the HTML source. Adding a user agent header resolves initial request blocking but does not reveal the data since it isn’t in the static source.

Next, the video covers installing Playwright (via pip or poetry) along with browser dependencies using `playwright install`. Using the synchronous API (`sync_playwright`), the script launches a Firefox browser, creates a browser context with a user agent, opens a page, navigates to the URL, and retrieves the fully rendered HTML content with `page.content()`. This content includes the desired data (e.g., “Airbnb” found in the page source), which was missing in the requests attempt.

The rendered HTML is saved to a file, then loaded with pandas’ `read_html` method (requiring the lxml package) to parse tables into a list of dataframes. Selecting the first dataframe gives a complete and structured dataset from the webpage.

Additional Playwright features demonstrated include:

- Taking full-page screenshots with `page.screenshot()`, useful for capturing the entire webpage view.
- Waiting for the page to fully load using `page.wait_for_timeout()` instead of `time.sleep()` for better control over scraping timing.
- Other capabilities such as clicking buttons, filling forms, handling authentication, managing downloads, and even video recording of browsing sessions, all documented in Playwright’s API.

The video emphasizes checking website policies before scraping and compares Playwright favorably against Selenium (outdated) and Puppeteer (lacks official Python bindings). The code is available on GitHub and can be run in a pre-configured dev container for ease of setup.

Viewers are encouraged to like and subscribe for more tutorials.</youtube_summary>
) ([youtube.com](https://www.youtube.com/watch?v=biFzRHk4xpY&utm_source=chatgpt
<youtube_summary>The video from Vincent Codes Finance demonstrates how to scrape a webpage using Python and Playwright, converting the data into a pandas DataFrame, even when the webpage’s source code lacks the actual table data. Playwright, a Microsoft web testing framework, is used here for scraping because it offers a headless browser (Chromium, Firefox, or WebKit) capable of executing JavaScript, which is essential for modern websites that load data dynamically via JavaScript rather than embedding it in the HTML source.

The presenter explains that while Playwright is mainly for testing, it supports features useful for scraping, such as handling authentication, interacting with page elements (clicking buttons, filling forms), and waiting for page loads. He advises checking a website’s scraping policy before proceeding. Compared to alternatives, Selenium feels outdated, and Puppeteer lacks official Python support, making Playwright the preferred modern tool.

The video walks through an example of scraping a NASDAQ webpage listing NASDAQ 100 stock quotes. Initially, using the simpler Python requests package fails because the data (e.g., “Airbnb”) isn’t present in the static page source and because the site blocks requests without a proper user agent header. Adding a user agent helps get the HTML but still lacks the dynamic data.

Playwright is then installed (via pip or poetry) along with browser dependencies using `playwright install`. The synchronous Playwright API is used in a Python script (preferred over Jupyter due to async issues) to launch a Firefox headless browser with a specified user agent, create a context and page, navigate to the URL with an increased timeout, and retrieve the fully rendered page content. This content includes the previously missing data.

The retrieved HTML is saved to a file and then loaded into pandas using `pandas.read_html()`, which returns a list of DataFrames (one per table). Selecting the first DataFrame provides a complete, usable table of the stock quotes.

Additional Playwright features shown include:
- Taking full-page screenshots with `page.screenshot()`, saving an image of the entire webpage.
- Waiting for page loads explicitly with `page.wait_for_timeout()` (preferred over `time.sleep()`).
- The API also supports actions like clicking buttons, filling forms, handling authentication, managing downloads, and even recording browsing sessions as videos.

The presenter encourages viewers to explore Playwright’s documentation for more advanced features and reminds to like and subscribe for future videos. The code used is available on GitHub, configured to run in a dev container for easy setup.</youtube_summary>
.com))

Playwright offers:

- **JavaScript rendering**: Executes page scripts so you scrape only after content appears. ([playwright.dev](https://playwright.dev/python/docs/intro))
- **Headless & headed modes**: Run without UI or in a real browser for debugging. ([playwright.dev](https://playwright.dev/python/docs/intro))
- **Auto‑waiting & retry**: Built‑in locators reduce flakiness. ([playwright.dev](https://playwright.dev/python/docs/locators))
- **Multi‑browser support**: Chromium, Firefox, WebKit—all from one API. ([playwright.dev](https://playwright.dev/python/docs/intro))

### Example: Scraping a JS‑Rendered Site

We’ll scrape [Quotes to Scrape (JS)](https://quotes.toscrape.com/js/)—a site that loads quotes via JavaScript, so a simple `requests` call gets only an empty shell ([quotes.toscrape.com](https://quotes.toscrape.com/js/)). Playwright runs the scripts and gives us the real content:

```python
# /// script
# dependencies = ["playwright"]
# ///

from playwright.sync_api import sync_playwright

def scrape_quotes():
    with sync_playwright() as p:
        # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
        browser = p.chromium.launch(headless=True, channel="chrome")
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/js/")
        quotes = page.query_selector_all(".quote")
        for q in quotes:
            text = q.query_selector(".text").inner_text()
            author = q.query_selector(".author").inner_text()
            print(f"{text} — {author}")
        browser.close()

if __name__ == "__main__":
    scrape_quotes()
```

Save as `scraper.py` and run:

```bash
uv run scraper.py
```

You’ll see each quote plus author printed—fetched only after the JS executes.
