-- Subqueries
-- 1. Result types

-- 1a. Scalar subquery (single value)
SELECT
	AVG(sales)
FROM sales.orders;

-- 1b. Row subquery (single column, multiple rows)
SELECT
	customerid
FROM sales.orders;

-- 1c. Table subquery (multiple columns, multiple rows)
SELECT
	customerid,
	orderid
FROM sales.orders;


-- 2. Location | Clauses
-- 2a. FROM subquery

-- Task: Find the products that have a price
-- higher than the average price of all products
SELECT
	*
FROM (
	SELECT
		productid,
		price,
		AVG(price) OVER() AS avgprice
	FROM sales.products
) AS t
WHERE price > avgprice;

-- Rank the customers based on their total amount of sales
SELECT
	*,
	RANK() OVER(ORDER BY totalsales DESC) AS customerrank
FROM (
	SELECT
		customerid,
		SUM(sales) AS totalsales
	FROM sales.orders
	GROUP BY customerid
) AS t;

-- Show the product ids, product names, price and total number of orders
SELECT 
	productid,
	product,
	price,
	(SELECT 
		COUNT(*) 
	FROM sales.orders) AS totalorders
FROM sales.products;

-- Show all customer details and find the total orders of each customer
SELECT
	c.*,
	o.count
FROM sales.customers AS c
LEFT JOIN (
	SELECT
		customerid,
		COUNT(*)
	FROM sales.orders
	GROUP BY customerid
) AS o
ON c.customerid = o.customerid;

-- Find the products that have a price higher than the average price of all products
SELECT 
	productid,
	price
FROM sales.products
WHERE price > (SELECT AVG(price) FROM sales.products);

-- Show the details of orders made by customers in Germany
SELECT
	*
FROM sales.orders
WHERE customerid IN (
	SELECT 
		customerid 
	FROM sales.customers 
	WHERE country = 'Germany'
);

-- Find female employees whose salaries are greater
-- than the salaries of any male employees
SELECT
	employeeid,
	firstname,
	gender,
	salary
FROM sales.employees
WHERE gender = 'F' 
AND salary > ANY (SELECT salary FROM sales.employees WHERE gender = 'M');

-- Find female employees whose salaries are greater
-- than the salaries of all male employees
SELECT
	employeeid,
	firstname,
	gender,
	salary
FROM sales.employees
WHERE gender = 'F' 
AND salary > ALL (SELECT salary FROM sales.employees WHERE gender = 'M');

-- Show all customer details and find the total orders of each customer
SELECT
	*,
	(SELECT COUNT(*) FROM sales.orders o WHERE o.customerid = c.customerid) AS totalsales
FROM sales.customers c;

-- Show the details of orders made by customers in Germany
SELECT 
	*
FROM sales.orders o
WHERE EXISTS (
	SELECT 1
	FROM sales.customers c
	WHERE c.country = 'Germany'
	AND o.customerid = c.customerid
);
