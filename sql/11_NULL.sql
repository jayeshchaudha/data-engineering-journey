-- SORT the customers from lowest to highest scores,
-- with nulls appearing last
SELECT
	customerid,
	score,
	CASE WHEN score IS NULL THEN 1 ELSE 0 END AS flag
FROM sales.customers 
ORDER BY CASE WHEN score IS NULL THEN 1 ELSE 0 END, score;

-- Find the sales price for each order by dividing sales by quantity
SELECT 
	orderid,
	sales,
	quantity,
	sales / NULLIF(quantity, 0) AS price
FROM sales.orders;

-- Identify the customers who has no scores
SELECT *
FROM sales.customers 
WHERE score IS NULL;

-- List all customers who has scores
SELECT *
FROM sales.customers 
WHERE score IS NOT NULL;

-- List all details for customers who have not placed any orders
SELECT 
	c.*
FROM sales.customers c
LEFT JOIN sales.orders o
	ON c.customerid = o.customerid 
WHERE o.customerid IS NULL;

WITH orders AS (
    SELECT 1 AS id, 'A'::text AS category UNION ALL
    SELECT 2, NULL UNION ALL
    SELECT 3, '' UNION ALL
    SELECT 4, '  '
)
SELECT *,
       OCTET_LENGTH(category) AS categorylen
FROM orders;
