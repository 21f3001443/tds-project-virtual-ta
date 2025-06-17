## Outlier Detection with Excel

[![Outlier detection with Excel](https://i.ytimg.com/vi_webp/sUTJb0F9eBw/sddefault.webp)](https://youtu.be/sUTJb0F9eBw
<youtube_summary>This tutorial explains how to identify outliers in data using Excel. An outlier is a data point significantly different from others, which may be due to measurement variability or experimental error. Outliers can distort statistical analysis but may also provide valuable insights, so they are not always removed.

To find outliers, the tutorial uses a COVID-19 dataset focusing on the "new cases" column. The steps include calculating quartiles (Q1 and Q3) using Excel's QUARTILE.EXC function, determining the interquartile range (IQR = Q3 - Q1), and then calculating the lower bound (Q1 - 1.5*IQR) and upper bound (Q3 + 1.5*IQR). Any data point below the lower bound or above the upper bound is considered an outlier. Since new cases cannot be negative, the lower bound is set to zero if negative.

To identify outliers, an Excel OR function checks if values are greater than the upper bound or less than the lower bound. Filtering the results shows the outliers. Additionally, a box plot can be created via Excel’s Insert > Recommended Charts > All Charts > Box and Whisker to visualize quartiles, median, bounds, and outliers.

Once outliers are identified, you can decide to keep or remove them depending on whether they would skew the analysis or provide useful information.</youtube_summary>
)

You'll learn how to identify and handle outliers in data using Excel, covering:

- **Understanding Outliers**: Definition of outliers and their impact on statistical analysis.
- **Calculating Quartiles**: Using Excel formulas to calculate Q1 (first quartile) and Q3 (third quartile).
- **Interquartile Range (IQR)**: Finding the IQR by subtracting Q1 from Q3.
- **Determining Bounds**: Calculating lower and upper bounds using 1.5 times the IQR.
- **Identifying Outliers**: Using Excel functions to determine if data points fall outside the calculated bounds.
- **Visualizing Data**: Creating box plots to visualize outliers and data distribution.
- **Handling Outliers**: Deciding whether to exclude or keep outliers based on their impact on analysis.

Here are the links used in the video:

- [Understand distributions and outliers](https://www.khanacademy.org/math/ap-statistics/quantitative-data-ap/xfb5d8e68:describing-distribution-quant/v/classifying-distributions)
- [COVID-19 vaccinations data - Excel](https://docs.google.com/spreadsheets/d/1_vQF2i5ubKmHQMBqoTwsu6AlevWsQtTD/view#gid=790744269)
