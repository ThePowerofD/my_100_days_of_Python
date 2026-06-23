student_dict = {
    "student": ['Angela','James', 'Lily'],
    "score:": [56,76,98]
}

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop thorugh a data frame
print('\nLooping through values')
for (key,value) in student_data_frame.items():
    print(value)
print('\nLooping through key')
for (key,value) in student_data_frame.items():
    print(key)

#Looping through rows of data frames
print('\nLooping through rows by index')
for (index,row) in student_data_frame.iterrows():
    print(index)
print('\nLooping through rows')
for (index,row) in student_data_frame.iterrows():
    print(row)