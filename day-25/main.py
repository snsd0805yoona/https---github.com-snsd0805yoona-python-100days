# with open("weather_data.csv") as data:
#     content = data.readlines()

# print(content)

# import csv

# with open("weather_data.csv") as data:
#     content = csv.reader(data)
#     temperature =[]
#     for row in content:
#         if row[1]!="temp":
#             temperature.append(int(row[1]))

#     print(temperature)

import pandas

# df = pandas.read_csv("weather_data.csv")
# sum=0
# temp_list = df["temp"].to_list()
# for i in range(len(temp_list)):
#     sum+=temp_list[i]
# #df["temp"].mean()

# # avg = sum/len(temp_list)
# # print(df[df.temp==df.temp.max()])

# monday = df[df.day=="Monday"]
# print(int(monday["temp"])*9/5+32)

# #create a dataframe from scratch

# data_dict = {
#     "students": ["Grace", "Yoona", "Jessica"],
#     "Scores": [87, 88, 89]
# }

# data = pandas.DataFrame(data_dict)

# print(data)

df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(df[df["Primary Fur Color"] == "Gray"])
red_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_count = len(df[df["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}


data = pandas.DataFrame(data_dict)

print(data)