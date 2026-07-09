/* Create report showing total sales for each of the following categories:
 * High (sales over 50), Medium (Sales 21 - 50), and Low (sales 20 or less)
 * Sort the categories from highest sales to lowest */
SELECT 
    categories,
    SUM(sales) AS totalsales
FROM (
    SELECT 
        orderid,
        sales,
        CASE 
            WHEN sales > 50 THEN 'High'
            WHEN sales > 20 THEN 'Medium'
            ELSE 'Low'
        END AS categories
    FROM sales.orders
) AS ordered_categories  
GROUP BY categories
ORDER BY totalsales DESC;

-- Retrieve employee details with gender displayed as full text
SELECT 
	employeeid,
	firstname,
	lastname,
	gender,
	CASE 
		WHEN gender = 'M' THEN 'Male'
		WHEN gender = 'F' THEN 'Female'
		ELSE 'Not Available'
	END AS gender_full	
FROM sales.employees;

-- Retrieve customers details with abbreviated country code
SELECT
	customerid,
	firstname,
	lastname,
	country,
	CASE
		WHEN country = 'Germany' THEN 'DE'
		WHEN country = 'USA' THEN 'US'
		ELSE 'Not available'
	END AS countrycode
FROM sales.customers;

-- quick format
SELECT
	customerid,
	firstname,
	lastname,
	country,
	CASE country
		WHEN 'Germany' THEN 'DE'
		WHEN 'USA' THEN 'US'
		ELSE 'Not available'
	END AS countrycode
FROM sales.customers;

-- Find the average scores of customers and treat nulls as 0
-- Additionally provide details such as customerID and LastName
SELECT 
	customerid,
	lastname,
	score,
	AVG(CASE
		WHEN score IS NULL THEN 0
		ELSE score
		END) OVER () AS avgcustomerclean,
	CASE
		WHEN score IS NULL THEN 0
		ELSE score
	END AS scoreclean,
	AVG(score) OVER() AS avgcustomers
FROM sales.customers;

-- Count how many times each customer has made an order with sales greater than 30
SELECT 
    customerid,
    SUM(CASE 
            WHEN sales > 30 THEN 1
            ELSE 0
        END) AS totalhighvalueorders,
	COUNT(*) AS totalorders
FROM sales.orders
GROUP BY customerid;