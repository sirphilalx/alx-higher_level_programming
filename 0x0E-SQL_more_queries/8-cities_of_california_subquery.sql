-- a script that lists all cities in California listed in a database
SELECT id, name
FROM cities
WHERE state_id IN
	(SELECT id
		FROM states
		WHERE name = 'California')
ORDER BY id;
