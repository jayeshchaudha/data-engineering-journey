-- pulling both tables separately first, no join yet
SELECT *
FROM customers;

SELECT *
FROM orders;

-- customers with their orders, but only the ones who actually placed an order
SELECT
    c.id,
    c.first_name,
    o.order_id,
    o.sales
FROM customers AS c
INNER JOIN orders AS o
    ON c.id = o.customer_id;

-- all customers with their orders, including customers who never ordered
SELECT
    c.id,
    c.first_name,
    o.order_id,
    o.sales
FROM customers AS c
LEFT JOIN orders AS o
    ON c.id = o.customer_id;

-- all customers with their orders, including orders that don't match a customer
SELECT
    c.id,
    c.first_name,
    o.order_id,
    o.sales
FROM customers AS c
RIGHT JOIN orders AS o
    ON c.id = o.customer_id;

-- same result as above but written as a LEFT JOIN by flipping the table order
SELECT
    c.id,
    c.first_name,
    o.order_id,
    o.sales
FROM orders AS o
LEFT JOIN customers AS c
    ON c.id = o.customer_id;

-- everything from both tables, matched where possible
SELECT
    c.id,
    c.first_name,
    o.order_id,
    o.sales
FROM customers AS c
FULL JOIN orders AS o
    ON c.id = o.customer_id;

-- customers who haven't placed any order
SELECT *
FROM customers AS c
LEFT JOIN orders AS o
    ON c.id = o.customer_id
WHERE o.customer_id IS NULL;

-- orders that don't have a matching customer
SELECT *
FROM customers AS c
RIGHT JOIN orders AS o
    ON c.id = o.customer_id
WHERE c.id IS NULL;

-- same idea, written with LEFT JOIN instead of RIGHT
SELECT *
FROM orders AS o
LEFT JOIN customers AS c
    ON c.id = o.customer_id
WHERE c.id IS NULL;

-- customers with no orders AND orders with no customer, both at once
SELECT *
FROM customers AS c
FULL JOIN orders AS o
    ON c.id = o.customer_id
WHERE c.id IS NULL OR o.customer_id IS NULL;

-- customers who have placed an order, done without using INNER JOIN directly
SELECT *
FROM customers AS c
LEFT JOIN orders AS o
    ON c.id = o.customer_id
WHERE o.customer_id IS NOT NULL;

-- every possible combination of customers x orders
SELECT *
FROM customers
CROSS JOIN orders;
