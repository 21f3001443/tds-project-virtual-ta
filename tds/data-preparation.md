# Data Preparation

Data preparation is crucial because raw data is rarely perfect.

It often contains errors, inconsistencies, or missing values. For example, marks data may have 'NA' or 'absent' for non-attendees, which you need to handle.

This section teaches you how to clean up data, convert it to different formats, aggregate it if required, and get a feel for the data before you analyze.

Here are links used in the video:

- [Presentation used in the video](https://docs.google.com/presentation/d/1Gb0QnPUN1YOwM_O5EqDdXUdL-5Azp1Tf/view)
- [Scraping assembly elections - Notebook](https://colab.research.google.com/drive/1SP8yVxzmofQO48-yXF3rujqWk2iM0KSl)
- [Assembly election results (CSV)](https://github.com/datameet/india-election-data/blob/master/assembly-elections/assembly.csv)
- [`pdftotext` software](https://www.xpdfreader.com/pdftotext-man.html)
- [OpenRefine software](https://openrefine.org)
- [The most persistent party](https://gramener.com/election/parliament#story.ddp)
- [TN assembly election cartogram](https://gramener.com/election/cartogram?ST_NAME=Tamil%20Nadu)

[![Data Preparation - Introduction](https://i.ytimg.com/vi_webp/dF3zchJJKqk/sddefault.webp)](https://youtu.be/dF3zchJJKqk
<youtube_summary>The text outlines the crucial steps involved in transforming and cleaning raw data to make it suitable for analysis, illustrated through a detailed case study of election data processing from India's 2014 general elections.

Initially, it emphasizes the importance of previewing, transforming, and cleaning data, noting that real-world data often contain imperfections such as missing values or inconsistent formats. For example, student marks data might have 'NA' or 'absent' entries that need handling.

The case study involves converting election result PDFs from the Election Commission website, spanning multiple years and states, into structured, analyzable formats. The process involved:
- Downloading hundreds of PDF files containing election data.
- Using tools like the xpdf command-line utility to convert PDFs to text while preserving layout.
- Parsing the text files to extract structured data such as constituency details, candidate names, votes, and party affiliations.
- Handling inconsistencies in PDF structures, such as missing headers or additional sections, by implementing conditional parsing logic.
- Extracting and cleaning constituency names, including removing extraneous text and identifying special constituency categories (e.g., SC or ST).
- Parsing candidate details with tailored parsing to accommodate exceptions.

The text highlights challenges such as:
- Constituency name variations and spelling errors over time, requiring consolidation. For instance, names like "Aland" and "Alland" or "Arabhavi" and "Arbhavi" needed to be merged.
- Phonetic similarity matching was employed using tools like OpenRefine to identify and merge similar names systematically.
- Renamed constituencies and party names—such as "Bandar" renamed to "Machilipatnam" or "MADMK" variants—required manual and heuristic approaches to unify data.
- Tracking party name changes over time, including splits and mergers, to maintain consistency.

The cleaned data resulted in a large, structured CSV file with around 400,000 rows containing detailed election results across years and states.

Further, the text shares insights gained from the cleaned data, such as:
- The "Doordarshi" party's record of contesting hundreds of seats over several elections without winning any.
- Analysis of the number of candidates per constituency across years, noting extraordinary cases like 1033 candidates contesting in Modakkurichi in 1996.
- Observations of candidate name duplications, often leading to zero votes for many candidates due to confusion.

Finally, the module described will teach tools and techniques to:
- Load and preview data using Excel and pandas profiling.
- Create derived metrics and transform data via Google Sheets, Excel, and Trifacta Wrangler.
- Transform image data using Python libraries like Pillow.
- Extract tables from PDFs using Tabula.
- Clean data and correct errors using OpenRefine.
- Label images with simple tools like Excel.

In summary, the module equips learners with practical skills and tools to convert raw, messy data into clean, analyzable formats, thus providing a competitive edge in data analysis.</youtube_summary>
)
