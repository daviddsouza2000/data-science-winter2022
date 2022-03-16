import csv

data = []

countries = ["CAN", "USA", "GBR", "FRA", "DEU", "SWE", "AUS", "DNK", "BEL"]

with open('resources/Country_Population.csv') as csv_file:
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
                data_row = [row[0], row[1], None, None, None, None, None, row[i], None, None, None, None, None, headers[i]]
                data.append(data_row)
        line_count+=1

with open('resources/Country_Region.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            for i in range(len(data)):
                if data[i][1] == row[11]:
                    data[i][2] = row[10]
                    data[i][4] = row[3]
                    data[i][3] = row[5]

        line_count += 1


with open('resources/Country_Area.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            for i in range(len(data)):
                if data[i][2] == row[0]:
                    data[i][9] = row[13]

        line_count+=1

with open('resources/Country_Currency.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            for i in range(len(data)):
                if data[i][2] == row[1]:
                    data[i][5] = row[3]

        line_count+=1

with open('resources/Country_Capitals.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        for i in range(len(data)):
            if data[i][2] == row[0]:
                data[i][6] = row[1]

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
        if data[i][1] == gdp[j][0] and data[i][13] == gdp[j][2]:
            data[i][10] = gdp[j][1]

for i in data:
    print(i)