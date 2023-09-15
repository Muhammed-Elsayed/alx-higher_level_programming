-- a script that lists all cities contained
SELECT cities.id, cities.name, states.name
FROM cities, states
ORDER BY cities.id ASC;
