-- =========================================================
-- PART 1: Customer Sales Summary
-- Goal: For each customer, get total sales, last order date,
-- their sales rank, and a High/Medium/Low segment label
-- =========================================================

-- Step 1: Find the total sales per customer
WITH CTE_Total_sales AS 
(
    SELECT
        customerid,
        SUM(sales) AS totalsales
    FROM sales.orders
    GROUP BY customerid
)

-- Step 2: Find the last order date for each customer
, CTE_last_order AS
(
    SELECT 
        customerid,
        MAX(orderdate) AS lastorder
    FROM sales.orders
    GROUP BY customerid
)

-- Step 3: Rank customers based on total sales
-- RANK() gives the same rank to ties, and skips the next number
-- (e.g. 1, 2, 2, 4 instead of 1, 2, 2, 3)
, CTE_Customer_rank AS
(
    SELECT
        customerid,
        totalsales,
        RANK() OVER (ORDER BY totalsales DESC) AS customerrank
    FROM CTE_Total_sales
)

-- Step 4: Segment customers based on their total sales
-- CASE WHEN works like if/elif/else - checked top to bottom,
-- first matching condition wins
, CTE_customer_segment AS
(
    SELECT 
        customerid,
        CASE 
            WHEN totalsales > 100 THEN 'High'
            WHEN totalsales > 50 THEN 'Medium'
            ELSE 'Low'
        END AS customersegment
    FROM CTE_Total_sales
)

-- Main query: bring everything together using the customer table as the base
-- LEFT JOIN is used so customers with no orders still show up (with NULLs)
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
LEFT JOIN CTE_Customer_rank AS ccr
    ON ccr.customerid = c.customerid
LEFT JOIN CTE_customer_segment AS ccs
    ON ccs.customerid = c.customerid;


-- =========================================================
-- PART 2: Generate a Number Sequence (Recursive CTE Basics)
-- Goal: Generate a sequence of numbers from 1 to 20
-- This is the classic "hello world" of recursive CTEs
-- =========================================================

WITH RECURSIVE series AS (

    -- Anchor query: this is the starting point of the recursion
    -- Runs ONCE, produces the first row
    SELECT 1 AS mynumber

    UNION ALL

    -- Recursive query: this runs repeatedly, each time referencing
    -- the CTE's own previous output (series), until the WHERE
    -- condition is no longer true
    SELECT mynumber + 1
    FROM series
    WHERE mynumber < 20
)
SELECT *
FROM series;


-- =========================================================
-- PART 3: Employee Hierarchy (Recursive CTE on Real Data)
-- Goal: Show each employee's level in the org chart
-- Level 1 = top of the hierarchy (no manager)
-- Level 2 = reports directly to a Level 1 person, and so on
-- =========================================================

WITH RECURSIVE CTE_Emp_hierarchy AS (

    -- Anchor query: find the top of the hierarchy
    -- (employees with no manager = the CEO / root)
    SELECT
        employeeid,
        firstname,
        managerid,
        1 AS level
    FROM sales.employees
    WHERE managerid IS NULL

    UNION ALL

    -- Recursive query: for each employee found so far,
    -- find the people who report to them (managerid = their employeeid)
    -- and increase the level by 1 each time we go one step down
    SELECT
        e.employeeid,
        e.firstname,
        e.managerid,
        ceh.level + 1
    FROM sales.employees AS e 
    INNER JOIN CTE_Emp_hierarchy ceh
        ON e.managerid = ceh.employeeid
)

-- Main query: show results ordered by level so it reads top-down
-- like an org chart, grouped by manager within each level
SELECT *
FROM CTE_Emp_hierarchy
ORDER BY level, managerid;