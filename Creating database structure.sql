SHOW COLUMNS FROM  happiness_2015;
create table econony(country varchar (15), GDP_per_capita decimal (15, 2));
create table famliy(country varchar (15), family decimal (15, 2));
create table health(country varchar (15), health decimal (15, 2));
create table freedom(country varchar (15), freedom decimal (15, 2));
create table Trust_corupption(country varchar (15), trust_corruptoin decimal (15, 2));
create table generosity(country varchar (15), generosity decimal (15, 2));


drop table happiness_ranking;



CREATE TABLE Trust_corruption (
    Country VARCHAR(255),
    Trust_corruption FLOAT
);

select * from economy;

use hapiness_indicators;
SHOW TABLES;



CREATE TABLE family(
    country VARCHAR(255),
    family FLOAT);
    
use hapiness_indicators;
SHOW TABLES;

INSERT INTO economy (Country,gdp_per_capita)
SELECT Country, `Economy (GDP per Capita)`
FROM happiness_2015;

INSERT INTO family (Country,family)
SELECT Country, Family
FROM happiness_2015;


ALTER TABLE freedom MODIFY COLUMN Country VARCHAR(255);

INSERT INTO freedom (Country,freedom)
SELECT Country, Freedom
FROM happiness_2015;

INSERT INTO generosity (Country,generosity)
SELECT Country, Generosity
FROM happiness_2015;


ALTER TABLE Trust_corruption ADD COLUMN Trust_corruption FLOAT;

INSERT INTO Trust_corruption (Country, Trust_corruption)
SELECT Country, `Trust (Government Corruption)`
FROM happiness_2015;


SELECT * from economy;
SELECT * from family;
SELECT * from freedom;
SELECT * from generosity;
SELECT * from happines_ranking;
SELECT * from health;
SELECT * from Trust_corruption;


SELECT * from world_happiness_ranking2015;


ALTER TABLE economy DROP COLUMN year;



ALTER TABLE happiness_2015
 DROP COLUMN `Standard Error` ;
 
 ALTER TABLE happiness_2015
 DROP COLUMN `Dystopia Residual` ;

drop table world_happiness_ranking;



INSERT INTO happines_ranking (country, happiness_rank,Happiness_score)
SELECT country, `Happiness Rank`,`Happiness Score`
FROM happiness_2015;

ALTER TABLE happines_ranking
MODIFY COLUMN country VARCHAR(100);

describe happines_ranking;


select * from happiness_2015;
ALTER TABLE happines_ranking
MODIFY COLUMN happiness_score DECIMAL(5, 2);

ALTER TABLE happines_ranking
MODIFY COLUMN happiness_score DECIMAL(5,2);


select * from happines_ranking;


-- Step 1: Truncate the table to delete all rows
TRUNCATE TABLE happines_ranking;

-- Step 2: Insert data again from the source table
INSERT INTO happines_ranking (country, happiness_rank, happiness_score)
SELECT country, `Happiness Rank`, `Happiness Score`
FROM happiness_2015;
	


