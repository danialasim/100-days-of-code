import pandas

data = pandas.read_csv("day_25_2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
print(data.head())
print(data.shape)
print(data.describe())
print(data.groupby("Primary Fur Color").count())

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)

df.to_csv("day_25_squirrel_count.csv")