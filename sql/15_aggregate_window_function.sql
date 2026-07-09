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
	COUNT(*) OVER() AS totalcustomers,
	COUNT(score) OVER() AS totalscores
FROM sales.customers;