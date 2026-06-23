#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# for line in names_text:
    #append in list

with open("Input/Names/invited_names.txt", "r") as names_file:
    names_list = names_file.readlines()


# with open("Input/Letters/starting_letter.txt", "r") as letter_file:
#     content = str(letter_file.read90())
# print(content)

for name in names_list:
    name = name.strip()
    with open("Input/Letters/starting_letter.txt", "r") as letter_file:
        content = str(letter_file.read())
    content = content.replace("[name]", name)
    with open(f"Output/ReadyToSend/invitation_{name}.txt", "w") as file:
           file.write(content)

#   print(f"Document created successfully for ", name,"is: \n", content)



#with open("Output/Names/invitation_{name}.txt", "w") as file:
#           file.write(content)
#with open ("./Letters/starting_letter.txt",mode = "r") as letter_file:
#    pre_letter = letter_file
#print(pre_letter)