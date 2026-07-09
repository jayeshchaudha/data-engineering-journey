-- rounding 3.516 to different decimal places
SELECT
    3.516,
    ROUND(3.516, 2) AS round_2,
    ROUND(3.516, 1) AS round_1,
    ROUND(3.516, 0) AS round_0;

-- absolute value turns negatives positive, positives stay the same
SELECT
    -10,
    ABS(-10),
    ABS(10);
