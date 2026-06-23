import random
##Dictionary comprehension has the following form:
## new_dict = {new_key:new_value for item in list}


## new_dict = {new_key:new_value for (key,value) in dict.items()}


## new_dict = {new_key:new_value for (key,value) in dict.items() id test}

#example of looping through list:
print("ex 1:")
student_score = {
    "Alex":98,
    "Beth":78,
    "Caroline" :70,
    "Dave": 60,
    "Eleanor": 99,
    "Freddie": 86
}

names =['Alex', 'Beth','Caroline','Dave', 'Eleanor', 'Freddie']
ex1_dict_student_scores ={student:random.randint(1,100) for student in names}
print(ex1_dict_student_scores)

##Example 2 show as loop of students who passed.
## new_dict = {new_key:new_value for (key,value) in dict.items() id test}
print("ex 2:")

passed_students_ex = {student:score for (student, score) in student_score.items() if score >= 70}

print(passed_students_ex)