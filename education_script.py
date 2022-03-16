import pandas as pd
import numpy as np

def getEducationList():
  education_df = pd.read_csv("./resources/Education.csv")
  health_df = pd.read_csv("./resources/Education_Health.csv")

  countries = ["Canada", "United States", "United Kingdom",
              "France", "Germany", "Sweden", "Australia", "Denmark", "Belgium"]

  health_indicators = set(health_df["Series Name"])
  health_indicators.discard('nan')
  education_indicators = set(education_df["Series"])
  education_indicators.discard('nan')
  indicators = health_indicators.union(education_indicators)
  indicators.discard('nan')
  indicators = list(indicators)

  res = []
  for year in list(map(str, range(2005, 2021))):
    for country in countries:
      output = [country, year]
      for indicator in indicators:
        if indicator in education_indicators:
          output.append(education_df[(education_df['Country Name'] == country) & (
              education_df["Series"] == indicator)][year].item())
        elif indicator in health_indicators:
          output.append(health_df[(health_df['Country Name'] == country) & (
              health_df["Series Name"] == indicator)][year].item())
      res.append(output.copy())
  res = np.array(res)

  columns = ["Country Name", "Year"] + indicators
  education_dimension = pd.DataFrame(res, columns=columns)

  education_dimension[indicators].to_csv('output/education.csv', index=True, index_label="EducationKey")
  return education_dimension