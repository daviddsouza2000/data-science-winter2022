import pandas as pd

def getYearList():
    count = 0
    data = []
    for i in range(2005, 2021):
        data.append([count, i, i % 4 == 0])
        count += 1

    df = pd.DataFrame(data, columns=["YearKey", "Year", "IsLeapYear"])
    df.to_csv('output/year.csv', index=False)

    return data