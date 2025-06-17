## Google Charts

- [Google Chart 1](https://youtu.be/-DQP4fpmJpc): How To Create Chart Or Graph On HTML CSS Website | Google Charts Tutorial
- [Google Chart 2](https://youtu.be/6tx58ZZGxrI
<youtube_summary>The talk titled "Using Google Charts with Google Viz" provides an introduction to Google Charts, a JavaScript library accessible via the Google Viz API from R, allowing data manipulation in R and visualization through Google Charts, including integration with R Markdown and Shiny. The speaker highlights pros of Google Charts such as Google’s maintenance ensuring good software and API quality, numerous chart options, interactivity with mouse-over tooltips, customization, and Shiny support. Cons include dependency on Google’s continued support, complexity from many chart types causing inconsistent visuals, poor print quality, and the requirement for an internet connection to access the API.

Documentation for Google Viz is comprehensive, including a PDF with extensive examples. The package uses a naming convention (jiva’s followed by chart type) and supports combining multiple charts into dashboards. The speaker demonstrates two chart types: Sankey diagrams (used to track YouTube user journeys with customized HTML tooltips showing impressions, clicks, and click-through rates) and motion charts (using World Development Indicators/GAPMINDER data). The motion charts require Flash enabled in the browser, which can cause confusion when charts fail to load.

The motion charts visualize country data over time, showing life expectancy versus GDP per capita with options to change scales (e.g., log scale), variables, bubble size, and color. Features include selecting countries, adjusting opacity, and showing trails of data movement over time, demonstrating socio-economic progress worldwide. The speaker references Hans Rosling’s popularization of these charts and recommends his videos.

Integration with Shiny allows interactive filtering and dynamic visualization within R Markdown slides. Alternative JavaScript visualization libraries for R mentioned include the DataTables package (distinct from data.table), Highcharts (commercial license needed for government/commercial use), Leaflet for mapping, R2D3, and NetworkD3 for Sankey and network graphs, as well as Plotly.

The entire presentation, including all code and slides, will be available on GitHub and YouTube. The speaker thanks the organizers, venue, and contributors, including Marcus Guzman from Google Viz, who requested formal citation.</youtube_summary>
): Using Google Charts with googleVis
