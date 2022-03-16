import csv
import pandas as pd

def getCountryList():
    data = []

    countries = ["CAN", "USA", "GBR", "FRA", "DEU", "SWE", "AUS", "DNK", "BEL"]

    with open('resources/Country_Population.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        index = 0
        for row in csv_reader:
            if line_count == 4:
                headers = row
                start_index = 0
                end_index = 0
                for i in range(len(row)):
                    if i > 3 and i < len(row)-1:
                        if int(row[i]) == 2005:
                            start_index = i
                        if int(row[i]) == 2020:
                            end_index = i
            if line_count > 4 and row[1] in countries:
                for i in range(start_index, end_index+1):
                    data_row = [index, row[0], row[1], None, None, None, None, None, row[i], None, None, None, None, headers[i]]
                    index+=1
                    data.append(data_row)
            line_count+=1

    with open('resources/Country_Region.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                for i in range(len(data)):
                    if data[i][2] == row[11]:
                        data[i][3] = row[10]
                        data[i][5] = row[3]
                        data[i][4] = row[5]

            line_count += 1


    with open('resources/Country_Area.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                for i in range(len(data)):
                    if data[i][3] == row[0]:
                        data[i][10] = row[13]

            line_count+=1

    with open('resources/Country_Currency.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                for i in range(len(data)):
                    if data[i][3] == row[1]:
                        data[i][6] = row[3]

            line_count+=1

    with open('resources/Country_Capitals.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for i in range(len(data)):
                if data[i][3] == row[0]:
                    data[i][7] = row[1]

            line_count += 1

    gdp = []

    with open('resources/Country_GDP.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 4:
                headers = row
                start_index = 0
                end_index = 0
                for i in range(len(row)):
                    if i > 3 and i < len(row)-1:
                        if int(row[i]) == 2005:
                            start_index = i
                        if int(row[i]) == 2020:
                            end_index = i
            if line_count > 4 and row[1] in countries:
                for i in range(start_index, end_index+1):
                    gdp_row = [row[1], row[i], headers[i]]
                    gdp.append(gdp_row)
            line_count+=1

    for i in range(len(data)):
        for j in range(len(gdp)):
            if data[i][2] == gdp[j][0] and data[i][13] == gdp[j][2]:
                data[i][11] = gdp[j][1]


    density = []

    with open('resources/Country_Density.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 4:
                headers = row
                start_index = 0
                end_index = 0
                for i in range(len(row)):
                    if i > 3 and i < len(row)-1:
                        if int(row[i]) == 2005:
                            start_index = i
                        if int(row[i]) == 2020:
                            end_index = i
            if line_count > 4 and row[1] in countries:
                for i in range(start_index, end_index+1):
                    density_row = [row[1], row[i], headers[i]]
                    density.append(density_row)
            line_count+=1

    for i in range(len(data)):
        for j in range(len(density)):
            if data[i][2] == density[j][0] and data[i][13] == density[j][2]:
                data[i][12] = density[j][1]


    fertility = []

    with open('resources/Country_Density.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 4:
                headers = row
                start_index = 0
                end_index = 0
                for i in range(len(row)):
                    if i > 3 and i < len(row)-1:
                        if int(row[i]) == 2005:
                            start_index = i
                        if int(row[i]) == 2020:
                            end_index = i
            if line_count > 4 and row[1] in countries:
                for i in range(start_index, end_index+1):
                    fertility_row = [row[1], row[i], headers[i]]
                    fertility.append(fertility_row)
            line_count+=1

    for i in range(len(data)):
        for j in range(len(fertility)):
            if data[i][2] == fertility[j][0] and data[i][13] == fertility[j][2]:
                data[i][9] = fertility[j][1]

    output_data = []

    for i in data:
        output_data.append(i[:-1])

    df = pd.DataFrame(output_data, columns=["CountryKey", "Name", "ALPHA-3", "ALPHA-2", "Region", "Continent", "Currency", "Capital", "TotalPopulation", "Birthrate", "Size", "GDP", "PopulationDensity"])
    df.to_csv('output/country.csv', index=False)

    return data