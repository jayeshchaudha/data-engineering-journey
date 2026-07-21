-- ===================================================
-- CTAS SCRIPT — sales schema
-- Run once. Tables created with CTAS need to be dropped
-- before re-running, or use DROP TABLE IF EXISTS first.
-- ===================================================

CREATE TABLE IF NOT EXISTS sales.monthlyorders AS( 
	SELECT
		TO_CHAR(orderdate, 'FMMonth') AS ordermonth,
		COUNT(orderid) AS totalorders
	FROM sales.orders
	GROUP BY TO_CHAR(orderdate, 'FMMonth')
);

SELECT * FROM sales.monthlyorders;

DROP TABLE sales.monthlyorders;

CREATE TEMP TABLE allorders AS
SELECT 
	*
FROM sales.orders;

SELECT * FROM allorders;

DELETE FROM allorders
WHERE orderstatus = 'Delivered';

SELECT * FROM allorders;

CREATE TABLE sales.orderstest AS
SELECT * FROM allorders;
