### List Comprehension

## We are doing this to create lists easier
## new_list =[new_item for item in list]

numbers = [1,2,3]
new_list = [n + 1 for n in numbers]

#expected result is [2,3,4]


###
#Now we try it out other sequences like strings
name = "Angela"
new_list_name = [letter for letter in name]

print(new_list_name)

#expected: gives us a list with each letter in list
#This stuff is called sequences

#excersice challenge: take range (1,5) create a list where each of the numbers is doubled answer should be [2,4,6,8]

ex = range(1,5)
ex_list = [s * 2 for s in ex] 
print(ex_list)

#Now lets add conditions to get a short name list

example_1 = ["alex", 'beth', 'caroline', 'dave', 'ealonor', 'freddie']
short_names = [name for name in example_1 if len(name) <5] 
print(short_names)
long_names_upper = [name.upper() for name in example_1 if len(name) >5]
print(long_names_upper)


list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n%2 == 0]
print(result)