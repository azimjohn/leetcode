SELECT t1.id as id
FROM (
    SELECT * FROM weather
) as t1
INNER JOIN (
    SELECT * FROM weather
) as t2
ON t1.recorddate - INTERVAL 1 DAY = t2.recorddate
WHERE t1.temperature > t2.temperature;
