# ApexPlanet Task 1: Data Immersion & Wrangling

## Project Overview

This project is completed as part of the ApexPlanet 60 Days Data Analytics Internship.

The objective of Task 1 is to understand the dataset, identify data-quality issues, clean and transform the data, and prepare a final analysis-ready dataset.

## Tools & Technologies

- Python
- Pandas
- Jupyter Notebook
- Microsoft Excel
- VS Code

## Dataset

The dataset contains 1000 sales transaction records with information about:

- Order ID
- Order Date
- Customer ID
- Customer Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit Price
- Total Sales

## Data Cleaning Performed

The following data-quality checks and transformations were performed:

1. Checked missing values.
2. Checked complete duplicate records.
3. Checked duplicate Order IDs.
4. Checked inconsistent data types and date formatting.
5. Detected Total Sales outliers using the IQR method.
6. Filled missing Age values using the median.
7. Filled missing City values using the mode.
8. Converted Order Date to datetime format.
9. Created Month, Year, and Month_Name features.
10. Validated the final cleaned dataset.

## Data Quality Findings

- Missing Age values: 20
- Missing City values: 13
- Complete duplicate rows: 0
- Duplicate Order ID occurrences: 8
- Total Sales statistical outliers: 19

The Total Sales outliers were inspected and retained because their values were consistent with Quantity × Unit Price and may represent valid high-value transactions.

Nine records share the same Order ID (`ORD100050`) but contain different transaction details. These records were retained because the available data does not provide enough information to determine the correct unique IDs.

## Final Dataset

- Rows: 1000
- Columns: 15
- Missing values: 0
- Complete duplicate rows: 0

## Project Outcome

The final dataset is cleaned, validated, and prepared for further data analysis and visualization.
