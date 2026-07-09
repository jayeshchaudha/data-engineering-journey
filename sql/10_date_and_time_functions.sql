-- =========================================================
-- STEP 0: Look at the raw data first
-- =========================================================
SELECT 
	orderid, 
	orderdate,
	shipdate,
	creationtime
FROM sales.orders;


-- =========================================================
-- STEP 1: NOW() and hardcoded dates
-- =========================================================
SELECT 
    orderid, 
    creationtime,
    '2025-08-20'::date AS hardcoded,   -- fixed date, written as text then cast to date
    NOW() AS today                     -- current date + time
FROM sales.orders;


-- =========================================================
-- STEP 2: PART EXTRACTION - EXTRACT()
-- Syntax: EXTRACT(part FROM column)
-- Always returns a NUMBER, never text
-- =========================================================
SELECT
    orderid,
    creationtime,
    EXTRACT(YEAR FROM creationtime)         AS year_dp,
    EXTRACT(QUARTER FROM creationtime)      AS quarter_dp,
    EXTRACT(MONTH FROM creationtime)        AS month_dp,
    EXTRACT(WEEK FROM creationtime)         AS week_dp,
    EXTRACT(DAY FROM creationtime)          AS day_dp,
    EXTRACT(DOW FROM creationtime)          AS dow_dp,        -- 0=Sunday, 1=Monday ... 6=Saturday
    EXTRACT(HOUR FROM creationtime)         AS hour_dp,
    EXTRACT(MINUTE FROM creationtime)       AS minute_dp,
    EXTRACT(SECOND FROM creationtime)       AS second_dp,
    EXTRACT(MILLISECONDS FROM creationtime) AS millisec_dp,
    EXTRACT(EPOCH FROM creationtime)        AS epoch_dp        -- seconds since 1970-01-01
FROM sales.orders;


-- =========================================================
-- STEP 3: PART EXTRACTION - DATE_PART()
-- Syntax: DATE_PART('part', column)
-- Same result as EXTRACT() above, just different syntax style
-- =========================================================
SELECT
    orderid,
    creationtime,
    DATE_PART('year', creationtime)         AS year_dp,
    DATE_PART('quarter', creationtime)      AS quarter_dp,
    DATE_PART('month', creationtime)        AS month_dp,
    DATE_PART('week', creationtime)         AS week_dp,
    DATE_PART('day', creationtime)          AS day_dp,
    DATE_PART('dow', creationtime)          AS dow_dp,        -- 0=Sunday, 1=Monday ... 6=Saturday
    DATE_PART('hour', creationtime)         AS hour_dp,
    DATE_PART('minute', creationtime)       AS minute_dp,
    DATE_PART('second', creationtime)       AS second_dp,
    DATE_PART('milliseconds', creationtime) AS millisec_dp,
    DATE_PART('epoch', creationtime)        AS epoch_dp        -- seconds since 1970-01-01
FROM sales.orders;


-- =========================================================
-- STEP 4: FORMATTING - TO_CHAR()
-- Syntax: TO_CHAR(column, 'format_string')
-- Always returns TEXT, built from format codes
-- This is Postgres's version of DATENAME() / FORMAT() / CONVERT() style codes combined
-- =========================================================

-- 4a) Default output vs FM (fill mode) - side by side so you SEE the difference
SELECT
    orderid,
    creationtime,
    TO_CHAR(creationtime, 'Month')   AS month_padded,     -- 'January  ' (padded with spaces)
    TO_CHAR(creationtime, 'FMMonth') AS month_trimmed,     -- 'January'   (no padding)
    TO_CHAR(creationtime, 'Day')     AS weekday_padded,    -- 'Wednesday ' (padded)
    TO_CHAR(creationtime, 'FMDay')   AS weekday_trimmed,   -- 'Wednesday'  (no padding)
    TO_CHAR(creationtime, 'DD')      AS day_padded,        -- '02' (2-digit)
    TO_CHAR(creationtime, 'FMDD')    AS day_trimmed        -- '2'  (no leading zero)
FROM sales.orders;

-- 4b) Full cheat-sheet of common TO_CHAR() format codes
SELECT 
    orderid,
    -- day
    TO_CHAR(creationtime, 'DD')          AS dd,           -- 2-digit day (e.g. '02')
    TO_CHAR(creationtime, 'Dy')          AS ddd,          -- 3-letter day (e.g. 'Thu')
    TO_CHAR(creationtime, 'FMDay')       AS dddd,         -- full day name (e.g. 'Sunday')
    -- month
    TO_CHAR(creationtime, 'MM')          AS mm,           -- 2-digit month (e.g. '01')
    TO_CHAR(creationtime, 'FMMon')       AS mmm,          -- 3-letter month (e.g. 'Jan')
    TO_CHAR(creationtime, 'FMMonth')     AS mmmm,         -- full month name (e.g. 'January')
    -- year
    TO_CHAR(creationtime, 'YY')          AS yy,           -- 2-digit year
    TO_CHAR(creationtime, 'YYYY')        AS yyyy,         -- 4-digit year
    -- quarter
    TO_CHAR(creationtime, 'Q')           AS quarter,      -- 1 to 4
    -- 24-hour clock
    TO_CHAR(creationtime, 'HH24:MI:SS')  AS time_24hr,
    -- 12-hour clock with AM/PM
    TO_CHAR(creationtime, 'HH12:MI:SS AM') AS time_12hr,  -- e.g. '02:34:59 PM'
    -- common date layouts
    TO_CHAR(creationtime, 'MM-DD-YYYY')  AS usa_format,
    TO_CHAR(creationtime, 'DD-MM-YYYY')  AS euro_format,
    TO_CHAR(creationtime, 'YYYY-MM-DD')  AS iso_format
FROM sales.orders;

-- 4c) Build a fully custom format string
-- Target: Day Wed Q3 2025 12:34:59 pm
SELECT 
    orderid,
    creationtime,
    'Day ' || TO_CHAR(creationtime, 'Dy FMMon') ||
    ' Q'   || EXTRACT(QUARTER FROM creationtime) ||
    ' '    || EXTRACT(YEAR FROM creationtime) ||
    ' '    || TO_CHAR(creationtime, 'HH12:MI:SS am') AS customformat
FROM sales.orders;


-- =========================================================
-- STEP 5: DATE_TRUNC() - rounding a date DOWN to a given precision
-- Syntax: DATE_TRUNC('precision', column)
-- Returns a real date/timestamp, not text
-- =========================================================
SELECT
    orderid,
    creationtime,
    DATE_TRUNC('day', creationtime)    AS day_dt,     -- keeps date, zeroes out the time
    DATE_TRUNC('month', creationtime)  AS month_dt,   -- rounds down to 1st of that month
    DATE_TRUNC('quarter', creationtime) AS quarter_dt, -- rounds down to start of that quarter
    DATE_TRUNC('year', creationtime)   AS year_dt,    -- rounds down to Jan 1st of that year
    DATE_TRUNC('hour', creationtime)   AS hour_dt,    -- keeps date+hour, zeroes minutes/seconds
    DATE_TRUNC('minute', creationtime) AS minute_dt   -- keeps hour:minute, zeroes seconds
FROM sales.orders;

-- Group orders by month using DATE_TRUNC()
SELECT 
    DATE_TRUNC('month', creationtime) AS creation_month,
    COUNT(*) AS total_orders
FROM sales.orders 
GROUP BY DATE_TRUNC('month', creationtime);

-- Get the LAST day of the month (end of month)
SELECT 
    orderid,
    creationtime,
    (DATE_TRUNC('month', creationtime) + INTERVAL '1 month' - INTERVAL '1 day')::date AS end_of_month
FROM sales.orders;

-- Get the FIRST day of the month (start of month)
SELECT
    orderid,
    creationtime,
    DATE_TRUNC('month', creationtime)::date AS start_of_current_month
FROM sales.orders;


-- =========================================================
-- STEP 6: Practice questions using what we just learned
-- =========================================================

-- How many orders were placed each year?
SELECT 
    EXTRACT(YEAR FROM orderdate) AS order_year,
    COUNT(*) AS NoOfOrders
FROM sales.orders
GROUP BY EXTRACT(YEAR FROM orderdate);

-- How many orders were placed each month?
SELECT 
    TO_CHAR(orderdate, 'FMMonth') AS order_month,
    COUNT(*) AS NoOfOrders
FROM sales.orders
GROUP BY TO_CHAR(orderdate, 'FMMonth');

-- Show all orders that were placed during the month of February
SELECT 
    *
FROM sales.orders 
WHERE EXTRACT(MONTH FROM orderdate) = 2;


-- =========================================================
-- STEP 7: CAST - converting between data types
-- Syntax: CAST(value AS type)   or shorthand   value::type
-- (Postgres has no CONVERT() like T-SQL - CAST covers all of it)
-- =========================================================
SELECT 
    CAST('123' AS INT)              AS string_to_int,
    CAST(123 AS VARCHAR)            AS int_to_string,
    CAST('2025-08-20' AS DATE)      AS string_to_date,
    CAST('2025-08-20' AS TIMESTAMP) AS string_to_datetime,
    creationtime,
    CAST(creationtime AS DATE)      AS datetime_to_date
FROM sales.orders;

-- Shorthand version using :: instead of CAST()
SELECT 
    '123'::INT              AS string_to_int,
    creationtime::DATE       AS datetime_to_date
FROM sales.orders;

-- USA vs EURO style output - done with TO_CHAR since CONVERT() doesn't exist here
SELECT 
    creationtime,
    TO_CHAR(creationtime, 'MM/DD/YYYY') AS usa_std_style,
    TO_CHAR(creationtime, 'DD.MM.YYYY') AS euro_std_style
FROM sales.orders;


-- =========================================================
-- STEP 8: Date arithmetic - INTERVAL
-- Syntax: column +/- INTERVAL 'number unit'
-- Works on both the DATE part and the TIME part
-- (Postgres has no DATEADD() - you add an INTERVAL directly)
-- =========================================================
SELECT 
    orderid,
    orderdate,
    orderdate - INTERVAL '10 days'  AS tendaysbefore,
    orderdate + INTERVAL '3 months' AS threemonthslater,
    orderdate + INTERVAL '2 years'  AS twoyearslater
FROM sales.orders;

-- INTERVAL also works on time components, not just dates
SELECT 
    creationtime,
    creationtime + INTERVAL '2 hours'    AS plus_two_hours,
    creationtime - INTERVAL '30 minutes' AS minus_30_min,
    creationtime + INTERVAL '1 day 3 hours 15 minutes' AS combined_shift
FROM sales.orders;

-- AGE() on its own - returns an INTERVAL like '30 years 2 mons 5 days'
-- (Postgres has no DATEDIFF() - AGE() is the tool used instead)
SELECT 
    employeeid,
    birthdate,
    AGE(birthdate) AS raw_age_interval        -- e.g. '30 years 2 mons 5 days'
FROM sales.employees;

-- Calculate age of employee in whole years
-- pull just the 'year' part out of the AGE() interval using DATE_PART()
SELECT 
    employeeid,
    birthdate,
    DATE_PART('year', AGE(birthdate)) AS age
FROM sales.employees;

-- Find the average shipping duration in days for each month
-- (subtracting two DATE values in Postgres directly gives number of days)
SELECT 
    EXTRACT(MONTH FROM orderdate) AS order_month,
    AVG(shipdate - orderdate) AS avgship
FROM sales.orders
GROUP BY EXTRACT(MONTH FROM orderdate);


-- =========================================================
-- STEP 9: Time gap analysis
-- find the number of days between each order and the previous order
-- Needs LAG() - a window function that looks at the PREVIOUS row's value
-- Syntax: LAG(column) OVER (ORDER BY column)
-- =========================================================
SELECT 
    orderid,
    orderdate,
    LAG(orderdate) OVER (ORDER BY orderdate) AS previous_orderdate,
    orderdate - LAG(orderdate) OVER (ORDER BY orderdate) AS days_since_previous_order
FROM sales.orders;


-- =========================================================
-- STEP 10: ISDATE()
-- (Postgres has no ISDATE() - a regex check on the pattern is the common workaround)
-- =========================================================
SELECT '2025-08-20' ~ '^\d{4}-\d{2}-\d{2}$' AS datecheck1;
