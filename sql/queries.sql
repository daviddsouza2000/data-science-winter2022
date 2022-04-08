SELECT "Continent", "Region", "Name", sum("TotalPopulation") FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
WHERE "Year" = 2010
GROUP BY ROLLUP("Continent", "Region", "Name")

SELECT "Continent", "Region", "Name", sum("TotalPopulation") FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
WHERE "Year" = 2010
GROUP BY ROLLUP("Name", "Region", "Continent")

SELECT "Name", AVG("InfantMortality") FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
LEFT JOIN jwadi014.data_mart."Health" ON "FactTable"."HealthKey" = "Health"."HealthKey"
GROUP BY "Name"

SELECT "Name", AVG("InfantMortality") FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
LEFT JOIN jwadi014.data_mart."Health" ON "FactTable"."HealthKey" = "Health"."HealthKey"
WHERE "Name" = 'United States' OR "Name" = 'Canada'
GROUP BY "Name"

SELECT "Name", AVG("SchoolEnrollmentSecondary") FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
LEFT JOIN jwadi014.data_mart."Education" ON "FactTable"."EducationKey" = "Education"."EducationKey"
WHERE "Name" = 'United States' OR "Name" = 'Canada'
GROUP BY "Name"

SELECT "Continent", "Region", "Name", AVG("UnemploymentTotal") as "Average Unemployment" FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
LEFT JOIN jwadi014.data_mart."QualityOfLife" ON "FactTable"."QualityOfLifeKey" = data_mart."QualityOfLife"."QualityOfLifeKey"
WHERE "Year" BETWEEN 2008 AND 2012
GROUP BY ROLLUP("Continent", "Region", "Name")

SELECT "Continent", "Region", "Name", AVG("UnemploymentTotal") as "Average Unemployment" FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
LEFT JOIN jwadi014.data_mart."QualityOfLife" ON "FactTable"."QualityOfLifeKey" = data_mart."QualityOfLife"."QualityOfLifeKey"
WHERE "Name" = 'United States' OR "Name" = 'Denmark'
GROUP BY ROLLUP("Continent", "Region", "Name")

SELECT "Year", "Name", "InfantMortality" FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
LEFT JOIN jwadi014.data_mart."Health" ON "FactTable"."HealthKey" = "Health"."HealthKey"
WHERE "Year"."Year" = 2010 OR "Year"."Year" = 2020
GROUP BY "Name", "Year"."Year", "InfantMortality" ORDER BY "Year", "Name" ASC

SELECT "Year", "Continent", "Region", "Name", sum("TotalPopulation") FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
WHERE "Year"."Year" = 2010 OR "Year"."Year" = 2020
GROUP BY ROLLUP("Continent", "Region", "Name"), "Name", "Year"."Year", "TotalPopulation" ORDER BY "Year", "Name" ASC

SELECT "Name", "Year", "PopulationGrowth" FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
LEFT JOIN jwadi014.data_mart."Population" ON "FactTable"."HealthKey" = "Population"."PopulationKey"
WHERE "Country"."Name" = 'United States' AND "PopulationGrowth" IS NOT NULL
ORDER BY "PopulationGrowth" DESC LIMIT 5

SELECT "Name", AVG("QualityOfLife"."AccessToDrinkingWater") as "DrinkingWater", RANK() OVER (ORDER BY AVG("QualityOfLife"."AccessToDrinkingWater") DESC) FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
LEFT JOIN jwadi014.data_mart."QualityOfLife" ON "FactTable"."QualityOfLifeKey" = "QualityOfLife"."QualityOfLifeKey"
WHERE "Year"."Year" BETWEEN 2015 AND 2020
group by "Name"

SELECT "Name", "Year", AVG("TotalPopulation") OVER W AS movavg FROM jwadi014.data_mart."FactTable"
LEFT JOIN jwadi014.data_mart."Country" ON "FactTable"."CountryKey" = "Country"."CountryKey"
LEFT JOIN jwadi014.data_mart."Year" ON "FactTable"."YearKey" = "Year"."YearKey"
WINDOW W AS (PARTITION BY "Name" ORDER BY "Year"."Year" RANGE BETWEEN 5 PRECEDING AND CURRENT ROW)