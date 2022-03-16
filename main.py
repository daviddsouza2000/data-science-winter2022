import country_script
import education_script

country = country_script.getCountryList()
education = education_script.getEducationList()

countries = ["Canada", "United States", "United Kingdom", "France", "Germany", "Sweden", "Australia", "Denmark", "Belgium"]

data = []

for i in range(2005, 2021):
    for j in countries:
        data_row = [None, None, None, None, None, None, None, None, None]
        for k in country:
            if i == int(k[13]) and j == k[1]:
                data_row[1] = k[0]
                break
        for p,k in enumerate(education.values):
            if i == int(k[1]) and j == k[0]:
                data_row[2] = p
                break
        data.append(data_row)


for i in data:
    print(i)