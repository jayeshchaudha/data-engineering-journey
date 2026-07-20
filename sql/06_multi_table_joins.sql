-- task: pull a full list of orders with the related customer, product, and
-- employee info -- need order id, customer name, sales, price, and salesperson name

-- peek at each table first to see what i'm working with
SELECT * FROM sales.customers;
SELECT * FROM sales.employees;
SELECT * FROM sales.orders;
SELECT * FROM sales.ordersarchive;
SELECT * FROM sales.products;

SELECT
    o.orderid,
    o.sales,
    c.firstname AS customer_first_name,
    c.lastname  AS customer_last_name,
    p.product   AS product_name,
    p.price,
    e.firstname AS employee_first_name,
    e.lastname  AS employee_last_name
FROM sales.orders AS o
LEFT JOIN sales.customers AS c
    ON o.customerid = c.customerid
LEFT JOIN sales.products AS p
    ON o.productid = p.productid
LEFT JOIN sales.employees AS e
    ON o.salespersonid = e.employeeid
ORDER BY o.orderid ASC;
