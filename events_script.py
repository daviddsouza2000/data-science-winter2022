import csv
import pandas as pd

import year_script


def getEventList():
    data = []

    year = year_script.getYearList()

    countries = ["Canada", "United States", "United Kingdom", "France", "Germany", "Sweden", "Australia", "Denmark", "Belgium"]

    with open('resources/Events.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        index = 0
        for row in csv_reader:
            if line_count > 0 and row[1] in countries and ";" not in row[2]:
                for k in year:
                    if int(row[2]) == k[1]:
                        data_row = [index, k[0], row[4], row[5], row[3]]
                        data.append(data_row)
                        index += 1
                        break
            line_count+=1

    df = pd.DataFrame(data, columns=["EventKey", "YearKey", "Name", "Description", "Type"])
    df.to_csv('output/events.csv', index=False)