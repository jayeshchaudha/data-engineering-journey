-- retrieve all customer data
SELECT *
FROM customers;

-- retrieve all order data
SELECT *
FROM orders;

-- just the columns i actually need: name, country, score
SELECT
    first_name,
    country,
    score
FROM customers;

-- customers with a score not equal to 0
SELECT *
FROM customers
WHERE score != 0;

-- customers from Germany
SELECT *
FROM customers
WHERE country = 'Germany';

-- same filter but only pulling the columns i care about
SELECT
    first_name,
    country
FROM customers
WHERE country = 'Germany';

-- sort by score, highest first
SELECT *
FROM customers
ORDER BY score DESC;

-- sort by score, lowest first
SELECT *
FROM customers
ORDER BY score ASC;

-- sort by country first, then by score (highest to lowest) within each country
SELECT *
FROM customers
ORDER BY country ASC, score DESC;

-- total score per country
SELECT
    country,
    SUM(score) AS total_score
FROM customers
GROUP BY country;

-- total score AND number of customers per country
SELECT
    country,
    SUM(score)  AS total_score,
    COUNT(id)   AS total_customer
FROM customers
GROUP BY country;

-- average score per country, ignoring customers with score = 0,
-- and only keeping countries where the average ends up above 430
SELECT
    country,
    AVG(score) AS average_score
FROM customers
WHERE score != 0
GROUP BY country
HAVING AVG(score) > 430;

-- unique list of countries (no repeats)
SELECT DISTINCT country
FROM customers;

-- just grab 3 customers, don't care which ones
SELECT *
FROM customers
LIMIT 3;

-- top 3 customers by score
SELECT *
FROM customers
ORDER BY score DESC
LIMIT 3;

-- bottom 2 customers by score
SELECT *
FROM customers
ORDER BY score ASC
LIMIT 2;

-- 2 most recent orders
SELECT *
FROM orders
ORDER BY order_date DESC
LIMIT 2;