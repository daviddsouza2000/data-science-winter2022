import country_script

country = country_script.getCountryList()

countries = ["Canada", "United States", "United Kingdom", "France", "Germany", "Sweden", "Australia", "Denmark", "Belgium"]

data = []

for i in range(2005, 2021):
    for j in countries:
        data_row = [None, None, None, None, None, None, None, None, None]
        for k in country:
            if i == int(k[13]) and j == k[1]:
                data_row[1] = k[0];
                data.append(data_row)

for i in data:
    print(i)