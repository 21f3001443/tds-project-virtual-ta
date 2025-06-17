## Regression with Excel

[![Regression with Excel](https://i.ytimg.com/vi_webp/AERQBMIHwXA/sddefault.webp)](https://youtu.be/AERQBMIHwXA
<youtube_summary>This tutorial explains how to perform multiple linear regression analysis in Excel using a cleaned COVID-19 dataset. The goal is to model the relationship between new deaths (dependent variable) and four independent variables: new cases, new tests, new vaccinations, and stringency index. The regression is conducted via Excel's Data Analysis Toolpak, which must be enabled beforehand.

Key steps include:

- Using columns for new cases, new tests, and new vaccinations per 1000 population to simplify coefficient interpretation.
- Selecting new deaths as the Y range (dependent variable) and the four independent variables as the X range.
- Running the regression to produce output in a new worksheet.

Key findings from the regression output:

- Adjusted R-squared is 0.816, indicating that 81% of the variation in new deaths is explained by the independent variables.
- The overall model is statistically significant (F-test p-value < 0.05).
- Among independent variables, new cases, new tests, and new vaccinations are statistically significant (p-values < 0.05), but the stringency index is not (p-value = 0.11 > 0.05), so it should be excluded from the model.
- Interpretation of coefficients:
  - For every 1000 new cases, deaths increase by 7.
  - For every 1000 new tests, deaths increase by 0.69.
  - For every 1000 new vaccinations, deaths decrease slightly by 0.07, though this small effect should be interpreted cautiously and requires further analysis.
  - The positive coefficient for stringency index (2.71) suggests deaths increase with more stringent policies, which is counterintuitive, but since it is not statistically significant, no firm conclusion is drawn.

Overall, the tutorial demonstrates how to run and interpret multiple linear regression in Excel for COVID-19 data, highlighting significant predictors of new deaths while noting the need for further investigation regarding vaccination effects and stringency index.</youtube_summary>
)

You'll learn to perform regression analysis using Excel, covering:

- **Data Preparation**: Understanding the cleaned dataset and necessary columns for analysis.
- **Enabling the Tool**: How to enable the Data Analysis Tool Pack in Excel.
- **Types of Regression**: Differences between simple and multiple linear regression.
- **Setting Up Regression**: Steps to input dependent (new deaths) and independent variables (new cases, new tests, new vaccinations, stringency index) for the analysis.
- **Interpreting Output**: Reading the regression output, focusing on adjusted R-squared, significance value (F-test), and P-values.
- **Coefficient Interpretation**: Understanding the impact of each independent variable on the dependent variable, including scaling factors (per 1000 units).
- **Model Evaluation**: Evaluating the model based on significance values and understanding the implications of unexpected results (e.g., stringency index).
- **Further Analysis**: Recognizing the need for additional analysis when encountering unexpected or inconclusive results.

Here are the links used in the video:

- [Understand regression](https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/least-squares-regression/v/calculating-the-equation-of-a-regression-line)
- [COVID-19 vaccinations - Regression Excel file](https://docs.google.com/spreadsheets/d/1YZLb9ozhmc-8KQ7EaaTgs57QT6dHju5u/view#gid=242862119)
- [COVID-19 vaccinations - Regression Model 2 Excel file](https://docs.google.com/spreadsheets/d/1KAolaOQC-P_6gXaw3jgUc7GWKAHfOrsi/view#gid=824457557)
