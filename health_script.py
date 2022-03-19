import pandas as pd
import numpy as np

def getHealthList():

  health_df = pd.read_csv("./resources/Health.csv")

  countries = ["Canada", "United States", "United Kingdom", "France", "Germany", "Sweden", "Australia", "Denmark", "Belgium"]

  health_indicators = set(health_df["Series Name"])
  health_indicators.discard('nan')
  indicators = list(health_indicators)
  indicators = [
       'Domestic general government health expenditure (% of GDP)',
       'Hospital beds (per 1,000 people)',
       'Immunization, HepB3 (% of one-year-old children)',
       'Immunization, DPT (% of children ages 12-23 months)',
       'Immunization, measles (% of children ages 12-23 months)',
       'Immunization, Pol3 (% of one-year-old children)',
       'Mortality rate, infant (per 1,000 live births)',
       'Stillbirth rate (per 1,000 total births)',
       'Nurses and midwives (per 1,000 people)',
       'Physicians (per 1,000 people)',
       'Diabetes prevalence (% of population ages 20 to 79)',
       'Prevalence of HIV, total (% of population ages 15-49)',
       'Prevalence of current tobacco use (% of adults)',
       'Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)',
       'Mortality rate, adult, male (per 1,000 male adults)',
       'Mortality rate, adult, female (per 1,000 female adults)',
  ]

  res = []
  for year in list(map(str, range(2005,2021))):
    for country in countries:
      output = [country, year]
      for indicator in indicators:
        if indicator in health_indicators:
          output.append((health_df[(health_df['Country Name'] == country) & (health_df["Series Name"] == indicator)][year]).item())
      res.append(output.copy())
  res = np.array(res)

  columns = ["Country Name", "Year"] + indicators
  health_dimension = pd.DataFrame(res, columns=columns)
  health_dimension = health_dimension.replace(to_replace='..', value='')
  health_dimension[indicators].to_csv('output/health.csv', index=True, index_label="Health_key")

  return health_dimension