import csv
import pandas

with open("weather_data.csv") as data_file:
    data2 = csv.reader(data_file)
    temperatures = []
    for row in data2:
        if row[1] != "temp":
                temperatures.append(int(row[1]))
    print(temperatures)

data = pandas.read_csv("weather_data.csv")
#print(data2) # to print the whole table (a dataframe)
print(data["temp"]) # to print column temp (a series)
type(data) # checks data also checks if it is a dataframe or a series
#series is a list columns in this case are series and the whole table is a dataframe
print(type(data["temp"]))

# get data to_dict() to convert to dictionary
data_dict = data.to_dict()
print("/n dictionary form")
print(data_dict)
temp_list = data["temp"].to_list()
print("/n List form:")
print(temp_list)

# calculation average temperature
avg_temp = sum(temp_list) / len(temp_list) # normal way [trataste de usar un for por menso] you can use mean operation from PANDAS
print(data["temp"].mean())
print(data["temp"].max())

#Get data in Columns:
print(data.condition) # column name is case sensitive

#Get data in Row
print(data[data.day == "Monday"])

#excersie figuring out day of the month with highest temperature:
print(f"\n Max temp info:\n")
max_temp = data["temp"].max()
print(data[data.temp == max_temp])

#create dataframe from python info being created

data_dict = {
     "students": ["Amy", "James", "Angela"],
     "scores": [76,56,65]
}
dataframe_student_data = pandas.DataFrame(data_dict)
print(dataframe_student_data)
dataframe_student_data.to_csv("new_data_students.csv")