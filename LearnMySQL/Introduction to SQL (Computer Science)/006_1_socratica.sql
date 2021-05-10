SELECT place,magnitude, occurred_on
FROM earthquake
WHERE cause = 'nuclear explosion'
ORDER BY
occurred_on DESC
LIMIT 1;

SELECT place,magnitude, occurred_on
FROM earthquake
WHERE occurred_on>='1969-01-01' AND occurred_on <'2019-01-01'
ORDER BY magnitude DESC
LIMIT 10;


SELECT COUNT(*)
FROM earthquake
WHERE place like '%Honshu%Japan%'
    AND occurred_on BETWEEN '2011-03-11' AND '2011-03-18';