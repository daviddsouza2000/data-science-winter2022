import pandas as pd
import numpy as np

def getQualityOfLifeList():

  quality_of_life_df = pd.read_csv("./resources/QualityOfLife.csv")

  countries = ["Canada", "United States", "United Kingdom", "France", "Germany", "Sweden", "Australia", "Denmark", "Belgium"]

  quality_of_life_indicators = set(quality_of_life_df["Series Name"])
  quality_of_life_indicators.discard('nan')
  indicators = list(quality_of_life_indicators)
  indicators = [
              'People using at least basic drinking water services (% of population)',
              'People using at least basic sanitation services (% of population)',
              'People with basic handwashing facilities including soap and water (% of population)',
              'Unemployment, female (% of female labor force)',
              'Unemployment, male (% of male labor force)',
              'Unemployment, total (% of total labor force)',
              'Pregnant women receiving prenatal care (%)',
              'Age dependency ratio (% of working-age population)',
              'Births attended by skilled health staff (% of total)',
              'Community health workers (per 1,000 people)',
              'Consumption of iodized salt (% of households)',
  ]
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
  quality_of_life_dimension = quality_of_life_dimension.replace(to_replace='..', value='')
  quality_of_life_dimension[indicators].to_csv('output/quality_of_life.csv', index=True, index_label="QualityOfLife_key")

  return quality_of_life_dimension