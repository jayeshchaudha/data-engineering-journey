-- combine employees and customers into one list, duplicates removed automatically
SELECT
    firstname,
    lastname
FROM sales.customers
UNION
SELECT
    firstname,
    lastname
FROM sales.employees;

-- same combo but keep duplicates this time
SELECT
    firstname,
    lastname
FROM sales.customers
UNION ALL
SELECT
    firstname,
    lastname
FROM sales.employees;

-- employees who are NOT also customers
SELECT
    firstname,
    lastname
FROM sales.employees
EXCEPT
SELECT
    firstname,
    lastname
FROM sales.customers;

-- employees who ARE also customers
SELECT
    firstname,
    lastname
FROM sales.employees
INTERSECT
SELECT
    firstname,
    lastname
FROM sales.customers;

-- orders live in two separate tables (orders + ordersarchive) --
-- combine them into one report, no duplicates, and tag which table each row came from
SELECT
    'orders' AS source_table,
    orderid,
    productid,
    customerid,
    salespersonid,
    orderdate,
    shipdate,
    orderstatus,
    shipaddress,
    billaddress,
    quantity,
    sales,
    creationtime
FROM sales.orders
UNION
SELECT
    'ordersarchive' AS source_table,
    orderid,
    productid,
    customerid,
    salespersonid,
    orderdate,
    shipdate,
    orderstatus,
    shipaddress,
    billaddress,
    quantity,
    sales,
    creationtime
FROM sales.ordersarchive
ORDER BY orderid;
