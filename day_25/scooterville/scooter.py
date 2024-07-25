# how many of each color, sorted by highest to lowers
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240724.csv")
grays_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [grays_count, red_count, black_count],
}

df = pandas.DataFrame(data_dict)

df.to_csv("scooter_count.csv")
