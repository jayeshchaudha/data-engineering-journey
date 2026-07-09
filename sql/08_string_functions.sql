-- combine first name and country into a single column
SELECT
    first_name,
    country,
    CONCAT(first_name, ' ', country) AS name_country
FROM customers;

-- lowercase version of first name
SELECT
    first_name,
    LOWER(first_name) AS low_name
FROM customers;

-- uppercase version of first name
SELECT
    first_name,
    UPPER(first_name) AS up_name
FROM customers;

-- find names that have leading/trailing spaces (compare to trimmed version)
SELECT
    first_name
FROM customers
WHERE first_name != TRIM(first_name);

-- strip the dashes out of a phone number
SELECT
    '123-456-789' AS phone,
    REPLACE('123-456-789', '-', '') AS clean_phone;

-- how many characters are in each first name
SELECT
    first_name,
    LENGTH(first_name) AS len_name
FROM customers;

-- first 2 characters of each name (trim first in case of stray spaces)
SELECT
    first_name,
    LEFT(TRIM(first_name), 2) AS first_2_char
FROM customers;

-- last 2 characters of each name
SELECT
    first_name,
    RIGHT(TRIM(first_name), 2) AS last_2_char
FROM customers;

-- drop the first character off each name
SELECT
    first_name,
    SUBSTRING(TRIM(first_name), 2, LENGTH(first_name)) AS sub_name
FROM customers;
