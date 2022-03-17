import pandas as pd
import numpy as np

def getQualityOfLifeList():

  quality_of_life_df = pd.read_csv("./resources/QualityOfLife.csv")

  countries = ["Canada", "United States", "United Kingdom", "France", "Germany", "Sweden", "Australia", "Denmark", "Belgium"]

  quality_of_life_indicators = set(quality_of_life_df["Series Name"])
  quality_of_life_indicators.discard('nan')
  indicators = list(quality_of_life_indicators)

  quality_of_life_df[(quality_of_life_df['Country Name'] == 'Canada') & (quality_of_life_df["Series Name"] == 'People using at least basic drinking water services (% of population)')]["2005"].item()

  list(map(str, range(2005,2021)))

  res = []
  for year in list(map(str, range(2005,2021))):
    for country in countries:
      output = [country, year]
      for indicator in indicators:
        if indicator in quality_of_life_indicators:
          output.append(quality_of_life_df[(quality_of_life_df['Country Name'] == country) & (quality_of_life_df["Series Name"] == indicator)][year].item())
      res.append(output.copy())
  res = np.array(res)

  columns = ["Country Name", "Year"] + indicators
  quality_of_life_dimension = pd.DataFrame(res, columns=columns)

  quality_of_life_dimension[indicators].to_csv(index=True, index_label="QualityOfLife_key")

  return quality_of_life_dimension