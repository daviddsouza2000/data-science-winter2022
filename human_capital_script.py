import csv

def getHumanCapitalList():
    data = []

    countries = ["CAN", "USA", "GBR", "FRA", "DEU", "SWE", "AUS", "DNK", "BEL"]

    with open('resources/Human_Capital.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if row[1] in countries and int(row[2]) >= 2005 and int(row[2]) <= 2020:
                data.append([row[0], int(row[2]), float(row[3])])

    return data