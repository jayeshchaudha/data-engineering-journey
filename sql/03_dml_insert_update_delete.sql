-- add two new customers
INSERT INTO customers (id, first_name, country, score)
VALUES
    (6, 'Anna', 'USA',  NULL),
    (7, 'Sam',  NULL,   100);

SELECT *
FROM customers;

-- messed up the column order here (country/first_name swapped) but SQL just
-- inserts it anyway since it doesn't check that kind of thing for you
INSERT INTO customers (id, first_name, country, score)
VALUES
    (8, 'USA', 'Max', NULL);

-- skipping column names works too, as long as values are in table order
INSERT INTO customers
VALUES
    (9, 'Andreas', 'Germany', NULL);

-- only filling in some columns, rest will default to NULL
INSERT INTO customers (id, first_name)
VALUES
    (10, 'SAhara');

-- copy customer data into persons table
INSERT INTO persons (id, person_name, birth_date, phone)
SELECT
    id,
    first_name,
    NULL,
    'Unknown'
FROM customers;

-- set customer 6's score to 0
UPDATE customers
SET score = 0
WHERE id = 6;

-- fixing the typo from the earlier insert (SAhara -> Sahara)
UPDATE customers
SET first_name = 'Sahara'
WHERE id = 10;

-- reset customer 10's score to 0 and fix their country to UK
UPDATE customers
SET score = 0,
    country = 'UK'
WHERE id = 10;

-- any customer with a NULL score gets set to 0
UPDATE customers
SET score = 0
WHERE score IS NULL;

-- delete all customers with id greater than 5
DELETE FROM customers
WHERE id > 5;

-- double check the delete actually worked (should return nothing)
SELECT *
FROM customers
WHERE id > 5;

-- wipe all rows out of persons but keep the table structure
TRUNCATE TABLE persons;
