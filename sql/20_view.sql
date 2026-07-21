-- ===================================================
-- VIEWS SCRIPT — sales schema
-- Run once. If a view already exists, use CREATE OR REPLACE
-- or DROP VIEW first (see notes at bottom).
-- ===================================================

-- 1. Monthly summary view (central aggregation logic)
CREATE OR REPLACE VIEW sales.monthly_summary AS
SELECT
    DATE_TRUNC('month', orderdate) AS order_month,
    SUM(sales) AS total_sales,
    COUNT(orderid) AS total_orders,
    SUM(quantity) AS total_quantities
FROM sales.orders
GROUP BY DATE_TRUNC('month', orderdate);

-- Test: running total on top of the view
SELECT
    order_month,
    SUM(total_sales) OVER(ORDER BY order_month) AS running_total
FROM sales.monthly_summary;


-- 2. Combined order details view (hides complexity of 4-table join)
CREATE OR REPLACE VIEW sales.order_details AS
SELECT
    o.orderid,
    p.product,
    p.category,
    COALESCE(c.firstname, '') || ' ' || COALESCE(c.lastname, '') AS customer_name,
    c.country AS customer_country,
    e.firstname || ' ' || e.lastname AS sales_name,
    e.department,
    o.orderdate,
    o.sales,
    o.quantity
FROM sales.orders o
LEFT JOIN sales.products p ON p.productid = o.productid
LEFT JOIN sales.customers c ON c.customerid = o.customerid
LEFT JOIN sales.employees e ON e.employeeid = o.salespersonid;

-- Test
SELECT * FROM sales.order_details;


-- 3. EU-only view (row-level security, excludes USA)
CREATE OR REPLACE VIEW sales.order_details_eu AS
SELECT *
FROM sales.order_details
WHERE customer_country != 'USA';

-- Test
SELECT * FROM sales.order_details_eu;

DROP VIEW sales.monthly_summary;