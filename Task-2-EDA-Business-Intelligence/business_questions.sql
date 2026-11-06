USE apexplanet_task2;

-- Question 1: Total Revenue
SELECT
    SUM(Total_Sales) AS Total_Revenue
FROM sales_full;


-- Q2: Top 5 Products by Revenue

SELECT
    Product,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_full
GROUP BY Product
ORDER BY Total_Revenue DESC
LIMIT 5;


-- Q3: Revenue by City

SELECT
    City,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_full
GROUP BY City
ORDER BY Total_Revenue DESC;


-- Q4: Monthly Revenue Trend

SELECT
    Year,
    Month,
    Month_Name,
    SUM(Total_Sales) AS Monthly_Revenue
FROM sales_full
GROUP BY Year, Month, Month_Name
ORDER BY Year, Month;


-- Q5: Revenue by Product Category

SELECT
    Category,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_full
GROUP BY Category
ORDER BY Total_Revenue DESC;


-- Q6: Average Sales per Record

SELECT
    AVG(Total_Sales) AS Average_Sales_Per_Record
FROM sales_full;


-- Q7: Revenue by gender
SELECT
    Gender,
    SUM(Total_Sales) AS Total_Revenue
FROM sales_full
GROUP BY Gender
ORDER BY Total_Revenue DESC;
