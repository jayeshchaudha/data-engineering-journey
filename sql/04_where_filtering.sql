-- all customers from Germany
SELECT *
FROM customers
WHERE country = 'Germany';

-- all customers NOT from Germany (two ways to write "not equal")
SELECT *
FROM customers
WHERE country != 'Germany';

SELECT *
FROM customers
WHERE country <> 'Germany';

-- score greater than 500
SELECT *
FROM customers
WHERE score > 500;

-- score 500 or more
SELECT *
FROM customers
WHERE score >= 500;

-- score less than 500
SELECT *
FROM customers
WHERE score < 500;

-- score 500 or less
SELECT *
FROM customers
WHERE score <= 500;

-- from USA AND score above 500 (both conditions must be true)
SELECT *
FROM customers
WHERE country = 'USA' AND score > 500;

-- from USA OR score above 500 (either condition is enough)
SELECT *
FROM customers
WHERE country = 'USA' OR score > 500;

-- everyone except USA customers, using NOT instead of !=
SELECT *
FROM customers
WHERE NOT (country = 'USA');

-- score somewhere between 100 and 500 (inclusive)
SELECT *
FROM customers
WHERE score BETWEEN 100 AND 500;

-- customers from either Germany or USA
SELECT *
FROM customers
WHERE country IN ('Germany', 'USA');

-- first name starts with M
SELECT *
FROM customers
WHERE first_name LIKE 'M%';

-- first name ends with n
SELECT *
FROM customers
WHERE first_name LIKE '%n';

-- first name contains r anywhere
SELECT *
FROM customers
WHERE first_name LIKE '%r%';

-- first name has r as the 3rd character
SELECT *
FROM customers
WHERE first_name LIKE '__r%';
