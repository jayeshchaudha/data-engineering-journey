-- Step 1 :Find the totak sales per customer
WITH CTE_Total_sales AS 
(
	SELECT
		customerid,
		SUM(sales) AS totalsales
	FROM sales.orders
	GROUP BY customerid
)
-- Step 2: find the last order date for each customer
, CTE_last_order AS
(
	SELECT 
		customerid,
		MAX(orderdate) AS lastorder
	FROM sales.orders
	GROUP BY customerid
)
-- Step 3 : Rank customers based on total sales per customer
, CTE_Customer_rank AS
(
	SELECT
	customerid,
	Totalsales,
	RANK() OVER (ORDER BY totalsales DESC) AS customerrank
	FROM CTE_Total_sales
)
-- Step 4 : segment customers based on their total sales
, CTE_customer_segment AS
(
	SELECT 
		customerid,
		CASE 
			WHEN totalsales > 100 THEN 'High'
			WHEN totalsales > 50 THEN 'Medium'
			ELSE 'Low'
		END AS customersegment
	FROM CTE_total_sales
)			

-- main query
SELECT
c.customerid,
c.firstname,
c.lastname,
cts.totalsales,
clo.lastorder,
ccr.customerrank,
ccs.customersegment
FROM sales.customers AS c
LEFT JOIN CTE_Total_sales AS cts
ON cts.customerid = c.customerid
LEFT JOIN CTE_last_order AS clo
ON clo.customerid = c.customerid
LEFT JOIN CTE_Customer_rank AS CCR
ON CCR.customerid = c.customerid
LEFT JOIN CTE_customer_segment AS CCS
ON ccs.customerid = c.customerid

-- Generate a sequence of numbers from 1 to 20
WITH RECURSIVE series AS (
    -- Anchor query
    SELECT 1 AS MyNumber
    UNION ALL
    -- Recursive query
    SELECT MyNumber + 1
    FROM series
    WHERE MyNumber < 20
)
SELECT *
FROM series;

--  TAsk: Show the employee hierarchy by displaying each employee's level within the organisation
WITH RECURSIVE CTE_Emp_hierarchy AS (
    SELECT
        employeeid,
        firstname,
        managerid, -- Fixed typo and added missing comma
        1 AS Level
    FROM sales.employees
    WHERE managerid IS NULL
    
    UNION ALL
    
    SELECT
        e.employeeid,
        e.firstname,
        e.managerid,
        ceh.Level + 1 -- Explicitly referencing the CTE's level
    FROM sales.employees AS e 
    INNER JOIN CTE_Emp_hierarchy ceh
    ON e.managerid = ceh.employeeid
)
-- Main query
SELECT *
FROM CTE_Emp_hierarchy
ORDER BY Level, managerid; -- Optional: keeps the CEO at the top and groups teams together