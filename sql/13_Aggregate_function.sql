SELECT * FROM sales.orders;

-- Find the total number of orders
SELECT
	COUNT(*) AS total_no_orders
FROM sales.orders;

-- Find the total sales of all orders
SELECT
	COUNT(*) AS total_no_orders,
	SUM(sales) AS total_sales
FROM sales.orders;

-- Find the average sales of all orders
SELECT
	COUNT(*) AS total_no_orders,
	SUM(sales) AS total_sales,
	AVG(sales) AS total_avg
FROM sales.orders;

-- Find the highest sales of all orders
SELECT
	COUNT(*) AS total_no_orders,
	SUM(sales) AS total_sales,
	AVG(sales) AS total_avg,
	MAX(sales) AS highest_sale
FROM sales.orders;

-- Find the lowest sales of all orders
SELECT
	COUNT(*) AS total_no_orders,
	SUM(sales) AS total_sales,
	AVG(sales) AS total_avg,
	MAX(sales) AS highest_sale,
	MIN(sales) AS lowest_sale
FROM sales.orders;

-- Find the lowest sales of all orders, broken down by customer
SELECT
	customerid,
	COUNT(*) AS total_no_orders,
	SUM(sales) AS total_sales,
	AVG(sales) AS total_avg,
	MAX(sales) AS highest_sale,
	MIN(sales) AS lowest_sale
FROM sales.orders
GROUP BY customerid;
