-- create the persons table: id, name, birth date, phone
CREATE TABLE IF NOT EXISTS persons (
    id          INT         NOT NULL,
    person_name VARCHAR(50) NOT NULL,
    birth_date  DATE,
    phone       VARCHAR(15) NOT NULL,
    CONSTRAINT pk_person PRIMARY KEY (id)
);

SELECT *
FROM persons;

-- add an email column
ALTER TABLE persons
ADD email VARCHAR(50) NOT NULL;

-- don't need phone anymore, drop it
ALTER TABLE persons
DROP COLUMN phone;

-- wipe the whole table from the database
DROP TABLE persons;
