-- Find the total number of orders
SELECT
	COUNT(*) AS totalorders
FROM sales.orders;

-- Find the total number of orders
-- Additionally provide details such as orderid, orderdate
SELECT
	orderid,
	orderdate,
	COUNT(*) OVER() AS totalorders
FROM sales.orders;

-- Find the total number of orders
-- Find the total number of orders for each customer
-- Additionally provide details such as orderid, orderdate
SELECT
	orderid,
	orderdate,
	customerid,
	COUNT(*) OVER() AS totalorders,
	COUNT(*) OVER(PARTITION BY customerid) AS ordersbycustomers
FROM sales.orders;

-- Find the total number of customers
-- Additionally provide all customer details
SELECT 
	*,
	COUNT(*) OVER() AS totalcustomers
FROM sales.customers;

-- Find the total number of customers
-- Find the total number of scores for the customers
-- Additionally provide all customer details
SELECT 
	*,
	COUNT(*) OVER() AS totalcustomersstar,
	COUNT(1) OVER() AS totalcustomersone, -- we can use 1 instead of *
	COUNT(score) OVER() AS totalscores
FROM sales.customers;

-- Check whather the table 'orders' contains any duplicate rows
SELECT
	*
FROM(
	SELECT
		orderid,
		COUNT(*) OVER(PARTITION BY orderid) AS checkpk
	FROM sales.ordersarchive
	) AS t
WHERE checkpk > 1;

-- Find the total sales across all orders
-- And the total sales for each product
-- Additionally provide details such orderid, order date
SELECT
	orderid,
	orderdate,
	sales,
	productid,
	SUM(sales) OVER() AS totalsales,
	SUM(sales) OVER(PARTITION BY productid) AS salesbyproducts
FROM sales.orders;

-- Find the percentage contribution of each product's sales to the total sales
SELECT 
	orderid,
	productid,
	sales,
	ROUND((sales :: numeric /(SUM(sales) OVER())*100), 2) :: text || '%' AS percentage
FROM sales.orders;

-- Find the average sales across all orders
-- And find the average sales for each product
-- additionally provide details such orderid, order date

SELECT
	orderid,
	orderdate,
	sales,
	productid,
	AVG(sales) OVER() AS avgsales,
	AVG(sales) OVER(PARTITION BY productid) AS avgsalesbyproduct
FROM sales.orders;

-- Find the avergae scores of customers
-- Additionally provide details such customerid and lastname
SELECT
	customerid,
	lastname,
	score,
	AVG(score) OVER() AS avgscore,
	AVG(COALESCE (score,0)) OVER() AS avgscorewithoutnull
FROM sales.customers;

-- Find all orders where sales are higher than the average sales across all orders
SELECT 
	*
FROM(
	SELECT
		orderid,
		productid,
		sales,
		AVG(sales) OVER() AS averagesale
	FROM sales.orders
	) AS t
WHERE sales > averagesale;

-- Find the hifhest and lowest sales of all orders
-- Find the highest and lowest sales for each product
-- Additionally provide details such orderid, order date

SELECT
	orderid,
	orderdate,
	productid,
	sales,
	MIN(sales) OVER () AS minsales,
	MAX(sales) OVER() AS maxsales,
	MIN(sales) OVER(PARTITION BY productid) AS minsalesbyproduct,
	MAX(sales) OVER(PARTITION BY productid) AS maxsalesbyproduct
FROM sales.orders;

-- Show the employees who have the highest salaries
SELECT
*
FROM(
	SELECT
	*,
	MAX(salary) OVER() AS highestsalary
	FROM sales.employees
	) AS t
WHERE salary = highestsalary;

-- Find the deviation of each sales from the minimum and maximum sales amounts
SELECT
	orderid,
	orderdate,
	productid,
	sales,
	MIN(sales) OVER () AS minsales,
	MAX(sales) OVER() AS maxsales,
	sales - MIN(sales) OVER () AS deviationfrommin,
	MAX(sales) OVER() - sales AS deviationfrommax
FROM sales.orders;

-- Calculate moving average of sales for each product over time
SELECT
	orderid,
	productid,
	orderdate,
	sales,
	AVG(sales) OVER(PARTITION BY productid) AS avgbyproduct,
	AVG(sales) OVER(PARTITION BY productid ORDER BY orderdate) AS movingavg
FROM sales.orders;

-- Calculate moving avrage of sales for each product overtime, including only the nxt order
SELECT
	orderid,
	productid,
	orderdate,
	sales,
	AVG(sales) OVER(PARTITION BY productid) AS avgbyproduct,
	AVG(sales) OVER(PARTITION BY productid ORDER BY orderdate) AS movingavg,
	AVG(sales) OVER(PARTITION BY productid ORDER BY orderdate ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) AS rollingavg
FROM sales.orders;
