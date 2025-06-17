## Visualizing Forecasts with Excel

[![Visualizing forecasts with Excel](https://i.ytimg.com/vi_webp/judFpVgfsV4/sddefault.webp)](https://youtu.be/judFpVgfsV4
<youtube_summary>This session demonstrates how to use Excel for exploratory data visualization and analysis of time series data involving various securities, including currencies (e.g., Australian Dollar, Canadian Dollar, Swiss franc), indices (FTSE, S&P, NASDAQ), and commodities (silver, gold, platinum) over a 90-day period from early August to early September.

Key objectives include identifying trends, forecasting future values, comparing fluctuations, and understanding relationships between securities. Visualizations such as sparklines and pivot tables help reveal patterns—for example, indices like FTSE, S&P, and NASDAQ show similar trends, while currencies exhibit more varied behaviors. The Brazilian Riyal shows the highest forecasted growth and fluctuation, while the Hong Kong Dollar shows minimal fluctuation.

To create these visuals, one starts by making a pivot table with securities and dates, adds sparklines to show trends, calculates averages, and uses Excel’s GROWTH formula to forecast next-day values. Conditional formatting highlights securities with the largest predicted increases or volatility. Variation is measured via standard deviation expressed as a percentage of the mean, providing insight into fluctuations.

Further analysis explores correlations between securities to quantify how closely their values move together. Scatterplots with linear trendlines and R² values illustrate relationships—for instance, the Brazilian Riyal and Australian Dollar have about 82-83% shared variance, whereas the Canadian Dollar correlates less strongly. The CORREL function calculates correlation coefficients quickly, with conditional formatting used to identify strongly correlated pairs. Notably, neighboring countries' currencies (e.g., Malaysian Ringgit and Singapore Dollar, Australian Dollar and New Zealand Dollar) show very high correlations (~95-97%), suggesting geographic influence.

A correlation matrix is created using Excel’s Data Analysis ToolPak to systematically compare all securities. This matrix, color-coded for easy interpretation, reveals patterns such as anti-correlations (e.g., Pakistani Rupee with many securities) and strong positive correlations (e.g., Singapore Dollar with Malaysian Ringgit). If the ToolPak is unavailable, correlations can be computed manually using the CORREL formula.

In summary, the process involves:
1. Importing raw time series data into Excel.
2. Creating pivot tables and sparklines for initial trend visualization.
3. Calculating averages, forecasting values, and measuring variability.
4. Analyzing pairwise correlations using scatterplots and correlation coefficients.
5. Constructing a correlation matrix to identify broader patterns and outliers.
6. Using conditional formatting for intuitive visualization of trends and relationships.

This approach showcases Excel as a powerful tool for exploratory data analysis and visualization, enabling users to extract meaningful insights from complex financial time series data efficiently.</youtube_summary>
)

- [Excel File](https://docs.google.com/spreadsheets/d/1a6cSbmZKjX_ZzBsWWrPQwU_4KgRNMwc0/view#gid=1138079165)
