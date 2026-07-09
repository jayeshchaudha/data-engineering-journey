-- Find the total sales across all orders
SELECT 
	SUM(sales) AS totalsales
FROM sales.orders;

-- Find the total sales for each product
SELECT 
	productid,
	SUM(sales) AS totalsales
FROM sales.orders
GROUP BY productid;

/* Find the total sales for each product
additionally provide details such as orderid, orderdate */
SELECT 
	orderid,
	orderdate,
	productid,
	SUM(sales) AS totalsales
FROM sales.orders
GROUP BY 
	orderid,
	orderdate,
	productid;
-- Does not give correct result - GROUP BY collapses rows instead of keeping each order visible

SELECT 
	orderid,
	orderdate,
	productid,
	SUM(sales) OVER(PARTITION BY productid) AS totalsales
FROM sales.orders;

-- Find the total sales across all orders
-- Additionally provide details such as orderid, orderdate
SELECT
	orderid,
	orderdate,
	SUM(sales) OVER() AS totalsales
FROM sales.orders;

-- Find the total sales for each order
-- Additionally provide details such as orderid, orderdate
SELECT
	orderid,
	orderdate,
	productid,
	SUM(sales) OVER(PARTITION BY productid) AS totalsales
FROM sales.orders;

-- Find the total sales across all orders
-- Find the total sales for each order
-- Additionally provide details such as orderid, orderdate
SELECT
	orderid,
	orderdate,
	productid,
	sales,
	SUM(sales) OVER() AS totalsales,
	SUM(sales) OVER(PARTITION BY productid) AS totalsalesbyproductid
FROM sales.orders;

-- Find the total sales across all orders
-- Find the total sales for each order
-- Find the total sales for each combination of product and order status
-- Additionally provide details such as orderid, orderdate
SELECT
	orderid,
	orderdate,
	productid,
	orderstatus,
	sales,
	SUM(sales) OVER() AS totalsales,
	SUM(sales) OVER(PARTITION BY productid) AS totalsalesbyproductid,
	SUM(sales) OVER(PARTITION BY productid, orderstatus) AS salesbyproductandstatus
FROM sales.orders;

-- Rank each order based on their sales from highest to lowest
-- Additionally provide details such as orderid, orderdate
SELECT
	orderid,
	orderdate,
	sales,
	RANK() OVER(ORDER BY sales DESC) AS ranksale
FROM sales.orders;

SELECT
    orderid,
    orderdate,
    orderstatus,
    sales,
    SUM(sales) OVER(
        PARTITION BY orderstatus 
        ORDER BY orderdate
        ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING
    ) AS totalsales
FROM sales.orders;

SELECT
    orderid,
    orderdate,
    orderstatus,
    productid,
    sales,
    SUM(sales) OVER(PARTITION BY orderstatus) AS totalsales
FROM sales.orders
WHERE productid IN (101, 102);

-- Rank customers based on their total sales
SELECT
	customerid,
    SUM(sales) AS totalsales,
    RANK() OVER (ORDER BY SUM(sales) DESC) AS rankcustomers
FROM sales.orders
GROUP BY customerid;

SELECT * FROM sales.orders;
