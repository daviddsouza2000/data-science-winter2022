import pandas as pd
import numpy as np

def getHealthList():

  health_df = pd.read_csv("./resources/Health.csv")

  countries = ["Canada", "United States", "United Kingdom", "France", "Germany", "Sweden", "Australia", "Denmark", "Belgium"]

  health_indicators = set(health_df["Series Name"])
  health_indicators.discard('nan')
  indicators = list(health_indicators)
  indicators

  health_df[(health_df['Country Name'] == 'Canada') & (health_df["Series Name"] == 'Domestic general government health expenditure (% of GDP)')]["2005"].item()

  list(map(str, range(2005,2021)))

  res = []
  for year in list(map(str, range(2005,2021))):
    for country in countries:
      output = [country, year]
      for indicator in indicators:
        if indicator in health_indicators:
          output.append(health_df[(health_df['Country Name'] == country) & (health_df["Series Name"] == indicator)][year].item())
      res.append(output.copy())
  res = np.array(res)

  columns = ["Country Name", "Year"] + indicators
  health_dimension = pd.DataFrame(res, columns=columns)

  health_dimension[indicators].to_csv('output/health.csv', index=True, index_label="Health_key")

  return health_dimension