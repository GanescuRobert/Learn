SELECT * 
FROM earthquake
WHERE occurred_on >= '2000-01-01';


SELECT *
FROM earthquake
WHERE occurred_on>='2010-01-01' AND occurred_on <'2011-01-01'
ORDER BY magnitude DESC
LIMIT 1;