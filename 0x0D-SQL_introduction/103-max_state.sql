-- Script that displays the max temparature of each state
-- Query to display the max temparature of each state
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC
LIMIT 3;
