-- 19. Temperatures #1
-- this script displays the top 3 cities by temperature
-- ordered by temperature (descending)

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3
