import csv

data = []

with open('resources/County_Population.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        data_row = [None, None, None, None, None, None, None, None, None, None, None]
        if line_count > 0 and int(row[4]) >= 2005 and int(row[4]) <= 2020 and row[3] == "Medium":
            data_row[0] = row[1]
            data_row[5] = row[8]
            data_row[9] = row[9]
            data.append(data_row)
        line_count+=1;

with open('resources/Country_Area.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            for i in range(len(data)):
                if data[i][0] == row[1]:
                    data[i][7] = row[13]

        line_count+=1;

print(data)