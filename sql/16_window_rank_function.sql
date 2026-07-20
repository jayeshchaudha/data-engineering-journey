-- Rank the orders based on their sales from highest to lowest
SELECT
	orderid,
	productid,
	sales,
	ROW_NUMBER() OVER(ORDER BY sales DESC) AS salesrank_row,
	RANK() 		 OVER(ORDER BY sales DESC) AS salesrank_rank,
	DENSE_RANK() OVER(ORDER BY sales DESC) AS salesrank_denserank
FROM sales.orders;

-- Find the top higest sales for each product
SELECT
	*
FROM 
	(SELECT
		orderid,
		productid,
		sales,
		ROW_NUMBER() OVER(PARTITION BY productid ORDER BY sales DESC) AS rn
	FROM sales.orders) AS t
WHERE rn = 1;

-- Find the lowest 2 customer based on their total sales
SELECT
	*
FROM(
	SELECT
		customerid,
		SUM(sales),
		ROW_NUMBER() OVER(ORDER BY SUM(sales)) AS rankcustomer
	FROM sales.orders
	GROUP BY customerid) AS t
WHERE rankcustomer <= 2;

--ASsign unique ids to the rows of the 'orders archieve' table
SELECT
	ROW_NUMBER () OVER (ORDER BY orderid, orderdate) AS uniqueid,
	*
FROM sales.ordersarchive;

-- Identify duplicate rows in the table 'order archive'
-- and return a clean result without any duplicates
SELECT
	*
FROM(
SELECT
	ROW_NUMBER() OVER(PARTITION BY orderid ORDER BY creationtime DESC) AS rn,
	*
FROM sales.ordersarchive) AS t
WHERE rn = 1;

SELECT
	orderid,
	sales,
	NTILE(4) OVER (ORDER BY sales DESC) fourbucket,
	NTILE(3) OVER (ORDER BY sales DESC) threebucket,
	NTILE(2) OVER (ORDER BY sales DESC) twobucket,
	NTILE(1) OVER (ORDER BY sales DESC) onebucket
FROM sales.orders;

-- Segment all order into 3 categories: high, medium and low sales
SELECT
*,
CASE WHEN buckets = 1 THEN 'High'
	WHEN buckets = 2 THEN 'Medium'
	WHEN buckets = 3 THEN 'Low'
END salesegmentation
FROM(
	SELECT
		orderid,
		sales,
		NTILE(3) OVER(ORDER BY sales DESC) AS buckets
	FROM sales.orders ) AS t;

-- In order to export the data, divide the orders into 2 groups.
SELECT
	NTILE(2) OVER(ORDER BY orderid) AS buckets,
	*
FROM sales.orders;

-- fIND THE PRODUct that fall within the highest 40% of the prices
SELECT
	*,
	(DISTrank * 100):: text || '%' AS percentage
FROM(
	SELECT
		product,
		price,
		CUME_DIST() OVER(ORDER BY price DESC) AS distrank
	FROM sales.products) AS t
WHERE distrank <=0.4;
