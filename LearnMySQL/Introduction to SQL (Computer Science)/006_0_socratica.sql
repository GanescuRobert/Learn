SELECT 
    MIN(occurred_on) as "MIN Date",
    MAX(occurred_on) as "MAX Date",
    MIN(magnitude) as "MIN Magnitude",
    MAX(magnitude) as "MAX Magnitude",
    AVG(magnitude) as "AVG Magnitude"
FROM earthquake
LIMIT 1;
