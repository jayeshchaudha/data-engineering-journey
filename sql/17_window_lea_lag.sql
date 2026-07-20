-- Analyze the month-over-month performance by finding the percetage change
-- in sales between the current and previous months
SELECT
	*,
	(currentmonthsale - previousmonthsales) AS MOMcchange,
	ROUND((currentmonthsale - previousmonthsales)::numeric / NULLIF(previousmonthsales, 0) * 100, 2) AS percentage
FROM (
	SELECT
		EXTRACT(MONTH FROM orderdate) AS ordermonth,
		SUM(sales) AS currentmonthsale,
		LAG(SUM(sales)) OVER(ORDER BY EXTRACT(MONTH FROM orderdate)) AS previousmonthsales
	FROM sales.orders
	GROUP BY EXTRACT(MONTH FROM orderdate)
) AS t;

-- In order to analyze customer loyalty,
-- rank customers based on the average days between their orders
SELECT
    customerid,
    AVG(Daysuntilnextorder) AS avgdays,
    RANK() OVER(ORDER BY COALESCE(AVG(Daysuntilnextorder), 999999) ASC) AS rankavg
FROM (
    SELECT
        orderid,
        customerid,
        orderdate AS currentorder,
        LEAD(orderdate) OVER(PARTITION BY customerid ORDER BY orderdate) AS nextorder,
        (LEAD(orderdate) OVER(PARTITION BY customerid ORDER BY orderdate) - orderdate) AS Daysuntilnextorder
    FROM sales.orders
) AS t
GROUP BY customerid;

-- Find the highest and lowest sales for each product
-- FIND the difference in sales between the current and the lowest sales
SELECT
	orderid,
	productid,
	sales,
	FIRST_VALUE(sales) OVER(PARTITION BY productid ORDER BY sales) AS lowestsales,
	LAST_VALUE(sales) OVER(
		PARTITION BY productid ORDER BY sales
		ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING
	) AS highestsale,
	FIRST_VALUE(sales) OVER(PARTITION BY productid ORDER BY sales DESC) AS highsales2,
	MIN(sales) OVER(PARTITION BY productid) AS lowestsales2,
	MAX(sales) OVER(PARTITION BY productid) AS highestsales3,
	sales - FIRST_VALUE(sales) OVER(PARTITION BY productid ORDER BY sales) AS salesdifference
FROM sales.orders;
