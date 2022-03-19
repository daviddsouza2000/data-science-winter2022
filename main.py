import country_script
import education_script
import events_script
import health_script

import pandas as pd

import human_capital_script
import population_script
import quality_of_life_script
import year_script

pd.set_option('display.expand_frame_repr', False)

country = country_script.getCountryList()
education = education_script.getEducationList()
health = health_script.getHealthList()
year = year_script.getYearList()
quality = quality_of_life_script.getQualityOfLifeList()
population = population_script.getPopulationList()
human = human_capital_script.getHumanCapitalList()
events = events_script.getEventList()

countries = ["Canada", "United States", "United Kingdom", "France", "Germany", "Sweden", "Australia", "Denmark", "Belgium"]

data = []

for i in range(2005, 2021):
    for j in countries:
        data_row = [None, None, None, None, None, None, None, None, None]
        for k in year:
            if i == k[1]:
                data_row[0] = k[0]
                break
        for k in country:
            if i == int(k[13]) and j == k[1]:
                data_row[1] = k[0]
                break
        for p,k in enumerate(education.values):
            if i == int(k[1]) and j == k[0]:
                data_row[2] = p
                break
        for p,k in enumerate(quality.values):
            if i == int(k[1]) and j == k[0]:
                data_row[3] = p
                break
        for p,k in enumerate(health.values):
            if i == int(k[1]) and j == k[0]:
                data_row[4] = p
                break
        for p,k in enumerate(population.values):
            if i == int(k[1]) and j == k[0]:
                data_row[5] = p
                break
        for k in human:
            if k[1] == i and k[0] == j:
                data_row[8] = int(k[2]*5)
                if k[2] >= 0.8:
                    data_row[7] = 1
                else:
                    data_row[7] = 2
        data.append(data_row)

for i in range(len(data)):
    if data[i][8] is None:
        data[i][8] = 5

df = pd.DataFrame(data, columns=["YearKey", "CountryKey", "EducationKey", "QualityOfLifeKey", "HealthKey", "PopulationKey", "QualityOfLife", "DevelopmentIndex", "HumanDevelopmentIndex"])
df.to_csv('output/fact_table.csv', index=False)