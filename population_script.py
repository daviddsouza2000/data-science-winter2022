import pandas as pd
import numpy as np

def getPopulationList():
  population_df = pd.read_csv("./resources//Population.csv")

  countries = ["Canada", "United States", "United Kingdom", "France", "Germany", "Sweden", "Australia", "Denmark", "Belgium"]

  indicators = set(population_df["Series Name"])
  indicators.discard('nan')
  indicators = list(indicators)

  res = []
  for year in list(map(str, range(2005,2021))):
    for country in countries:
      output = [country, year]
      for indicator in indicators:
        output.append(population_df[(population_df['Country Name'] == country) & (population_df["Series Name"] == indicator)][year].item())
      res.append(output.copy())
  res = np.array(res)

  columns = ["Country Name", "Year"] + indicators
  population_dimension = pd.DataFrame(res, columns=columns)

  population_dimension[indicators].to_csv('output/education', index_label="Education Key", index=True)
  return population_dimension