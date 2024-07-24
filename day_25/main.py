# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#
#     for t in temps:
#         print(t)

import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"])
