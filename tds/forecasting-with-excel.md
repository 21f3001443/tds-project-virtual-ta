## Forecasting with Excel

[![Forecasting with Excel](https://i.ytimg.com/vi_webp/QrTimmxwZw4/sddefault.webp)](https://youtu.be/QrTimmxwZw4
<youtube_summary>The text explains how to use Excel's FORECAST function, which performs linear regression to predict values based on known data. The FORECAST and FORECAST.LINEAR functions are synonymous. Using a sample dataset of 1,000 rows of height (in inches) and weight (in pounds) from Kaggle, the author converts these to metric units (height in cm by multiplying by 2.54; weight in kg by dividing by 2.204). A scatter plot shows a positive correlation between height and weight. Using FORECAST.LINEAR, one can predict weight for a given height (e.g., 170 cm corresponds to ~56 kg) or height for a given weight (e.g., 75 kg corresponds to ~180 cm). For predicting multiple values at once, the TREND function is more efficient as it computes the regression once and returns an array of predicted values. These functions also work in Google Sheets.

However, linear regression is not suitable for all data types. For example, traffic data with hourly vehicle counts at junctions shows seasonal and daily patterns that linear regression cannot capture effectively. A line chart of the raw data reveals spikes and weekly seasonality, such as lower traffic on weekends and holidays.

Applying the TREND function for linear prediction on this traffic data produces a nearly flat line that fails to capture the variability and seasonality in traffic volume. To better model cyclical data, Excel’s FORECAST.ETS function can be used, which accounts for seasonality by specifying a seasonality parameter (e.g., 24 hours for hourly traffic data). FORECAST.ETS also handles missing data via interpolation by default.

Plotting the ETS forecast against actual traffic data shows improvement over linear forecasting, capturing seasonal fluctuations better, though it is not perfect. Thus, FORECAST.ETS is recommended for cyclical time series data, while linear regression works well for simpler linear relationships like height and weight.</youtube_summary>
)

Here are links used in the video:

- [FORECAST reference](https://support.microsoft.com/en-us/office/forecast-and-forecast-linear-functions-50ca49c9-7b40-4892-94e4-7ad38bbeda99)
- [FORECAST.ETS reference](https://support.microsoft.com/en-us/office/forecast-ets-function-15389b8b-677e-4fbd-bd95-21d464333f41)
- [Height-weight dataset](https://docs.google.com/spreadsheets/d/1iMFVPh8q9KgnfLwBeBMmX1GaFabP02FK/view) from [Kaggle](https://www.kaggle.com/datasets/burnoutminer/heights-and-weights-dataset)
- [Traffic dataset](https://docs.google.com/spreadsheets/d/1w2R0fHdLG5ZGW-papaK7wzWq_-WDArKC/view) from [Kaggle](https://www.kaggle.com/datasets/fedesoriano/traffic-prediction-dataset)
