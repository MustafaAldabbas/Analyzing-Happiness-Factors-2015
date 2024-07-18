
-- Use the hapiness_indicators database
USE hapiness_indicators;

-- Show all tables in the database
SHOW TABLES;

-- Drop the world_happiness_ranking table if it exists to avoid conflicts
DROP TABLE IF EXISTS world_happiness_ranking;

-- Drop the happiness_ranking table if it exists to avoid conflicts
DROP TABLE IF EXISTS happiness_ranking;

-- Create the economy table
CREATE TABLE economy (
    country VARCHAR(255),
    gdp_per_capita DECIMAL(15, 2)
);

-- Create the family table
CREATE TABLE family (
    country VARCHAR(255),
    family FLOAT
);

-- Create the health table
CREATE TABLE health (
    country VARCHAR(255),
    health FLOAT
);

-- Create the freedom table
CREATE TABLE freedom (
    country VARCHAR(255),
    freedom FLOAT
);

-- Create the Trust_corruption table
CREATE TABLE Trust_corruption (
    country VARCHAR(255),
    trust_corruption FLOAT
);

-- Create the generosity table
CREATE TABLE generosity (
    country VARCHAR(255),
    generosity FLOAT
);

-- Create the happiness_ranking table
CREATE TABLE happiness_ranking (
    country VARCHAR(255) PRIMARY KEY,
    happiness_score FLOAT,
    happiness_rank INT
);

-- Insert data into the economy table from happiness_2015
INSERT INTO economy (country, gdp_per_capita)
SELECT country, `Economy (GDP per Capita)`
FROM happiness_2015;

-- Insert data into the family table from happiness_2015
INSERT INTO family (country, family)
SELECT country, family
FROM happiness_2015;

-- Insert data into the freedom table from happiness_2015
INSERT INTO freedom (country, freedom)
SELECT country, freedom
FROM happiness_2015;

-- Insert data into the generosity table from happiness_2015
INSERT INTO generosity (country, generosity)
SELECT country, generosity
FROM happiness_2015;

-- Insert data into the health table from happiness_2015
INSERT INTO health (country, health)
SELECT country, health
FROM happiness_2015;

-- Insert data into the Trust_corruption table from happiness_2015
INSERT INTO Trust_corruption (country, trust_corruption)
SELECT country, `Trust (Government Corruption)`
FROM happiness_2015;

-- Create the world_happiness_ranking2015 table
CREATE TABLE world_happiness_ranking2015 (
    country VARCHAR(255) PRIMARY KEY,
    gdp_per_capita FLOAT,
    family FLOAT,
    freedom FLOAT,
    generosity FLOAT,
    health FLOAT,
    trust_corruption FLOAT,
    happiness_score FLOAT,
    happiness_rank INT,
    FOREIGN KEY (country) REFERENCES happiness_ranking(country)
);

-- Update world_happiness_ranking table with data from other tables
UPDATE world_happiness_ranking2015 whr
JOIN economy e ON whr.country = e.country
SET whr.gdp_per_capita = e.gdp_per_capita;

UPDATE world_happiness_ranking2015 whr
JOIN family f ON whr.country = f.country
SET whr.family = f.family;

UPDATE world_happiness_ranking2015 whr
JOIN freedom fr ON whr.country = fr.country
SET whr.freedom = fr.freedom;

UPDATE world_happiness_ranking2015 whr
JOIN generosity g ON whr.country = g.country
SET whr.generosity = g.generosity;

UPDATE world_happiness_ranking2015 whr
JOIN health h ON whr.country = h.country
SET whr.health = h.health;

UPDATE world_happiness_ranking2015 whr
JOIN Trust_corruption tc ON whr.country = tc.country
SET whr.trust_corruption = tc.trust_corruption;

UPDATE world_happiness_ranking2015 whr
JOIN happines_ranking hr ON whr.country = hr.country
SET whr.happiness_score = hr.happiness_score, whr.happiness_rank = hr.happiness_rank;

-- Verify the data in each table
SELECT * FROM economy;
SELECT * FROM family;
SELECT * FROM freedom;
SELECT * FROM generosity;
SELECT * FROM health;
SELECT * FROM Trust_corruption;
SELECT * FROM happines_ranking;



);

-- Step 2: Insert data into the new table by joining existing tables with the specified order
INSERT INTO world_happiness_ranking2015 (country, happiness_rank, happiness_score, gdp_per_capita, family, freedom, generosity, trust_corruption, health)
SELECT
    e.country,
    hr.happiness_rank,
    hr.happiness_score,
    e.gdp_per_capita,
    f.family,
    fr.freedom,
    g.generosity,
    t.Trust_corruption,
    h.health
FROM
    economy e
JOIN
    family f ON e.country = f.country
JOIN
    freedom fr ON e.country = fr.country
JOIN
    generosity g ON e.country = g.country
JOIN
    Trust_corruption t ON e.country = t.country
JOIN
    happines_ranking hr ON e.country = hr.country
JOIN
    health h ON e.country = h.country;
    
select * from world_happiness_ranking2015;


#1- Top 10 Happiest Countries:
SELECT country, happiness_score, happiness_rank
FROM world_happiness_ranking2015
ORDER BY happiness_rank ASC
LIMIT 10;

#2- Bottom 10 Happiest Countries:
SELECT country, happiness_score, happiness_rank
FROM world_happiness_ranking2015
ORDER BY happiness_rank DESC
LIMIT 10;

#3- Top 10 Countries with Highest Trust in Government:
SELECT country, trust_corruption
FROM world_happiness_ranking2015
ORDER BY trust_corruption DESC
LIMIT 10;

#4- Top 10 Countries with Highest GDP per Capita:
SELECT country, gdp_per_capita
FROM world_happiness_ranking2015
ORDER BY gdp_per_capita DESC
LIMIT 10;


#5- Top 10 Countries with Highest Freedom:
sELECT country, freedom
FROM world_happiness_ranking2015
ORDER BY freedom DESC
LIMIT 10;

#6-Top 10 Countries with Highest Generosity:
SELECT country, generosity
FROM world_happiness_ranking2015
ORDER BY generosity DESC
LIMIT 10;

#7-Top 10 Countries with Most Family Support:
SELECT country, family
FROM world_happiness_ranking2015
ORDER BY family DESC
LIMIT 10;




# Hypothesis 1: Higher GDP per capita leads to higher happiness rank and score
-- GDP per capita vs. Happiness Score
SELECT country, gdp_per_capita, happiness_score, happiness_rank
FROM world_happiness_ranking2015
ORDER BY gdp_per_capita DESC;


#2- Hypothesis 2: Better health conditions (life expectancy) are positively correlated with happiness score and rank
-- Life Expectancy vs. Happiness Score
SELECT country, health, happiness_score, happiness_rank
FROM world_happiness_ranking2015
ORDER BY health DESC;

#3- Hypothesis 3: Countries with higher freedom scores have higher happiness rank and score
SELECT country, freedom, happiness_score, happiness_rank
FROM world_happiness_ranking2015
ORDER BY freedom DESC;

#4- Hypothesis 4: Trust in government corruption negatively affects happiness rank and scores
SELECT country, trust_corruption, happiness_score, happiness_rank
FROM world_happiness_ranking2015
ORDER BY trust_corruption DESC;

#5- Hypothesis 5: People who have more family support have higher happiness rank and score
SELECT country, family, happiness_score, happiness_rank
FROM world_happiness_ranking2015
ORDER BY family DESC;

#6- Hypothesis 6: Countries with a high level of generosity have better happiness rank
-- Generosity vs. Happiness Score
SELECT country, generosity, happiness_score
FROM world_happiness_ranking2015
ORDER BY generosity DESC;








