-- Script that displays the average temparature
-- Query to display the average temparature by city ordered by temparature
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
