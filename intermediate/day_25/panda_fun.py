import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)

# get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# create dataframe from scratch
data_dict = {
    "students": ["amy", "james", "angela", "tupelo", "elvis"],
    "scores": [76, 56, 65, 89, 100],
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
