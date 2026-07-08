import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

# # print(data)


# # print('////////////////////////////////////////\n')
# # dcit = {new_key:new_value for (index, row) in dataFrame.iterrows()}
phone_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# # print(phone_dict)


def converting_nato(phone_dict):
    while True:
        word = input("Enter a word: ").upper()
        try:
            phone_list = [phone_dict[letter] for letter in word]
            print(phone_list)
            break  # valid word entered, exit the loop
        except KeyError:
            print("Sorry, only letters in the alphabet please.")

converting_nato(phone_dict)
### --- Previosu attempt without try/except/else/loop ---- ###

# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# # print(data.to_dict())

# # print(data)


# # print('////////////////////////////////////////\n')
# # dcit = {new_key:new_value for (index, row) in dataFrame.iterrows()}
# phone_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# # print(phone_dict)

# def converting_nato(phone_dict):
#     word = input("enter a word ").upper()
#     print("your letter")

#     try:
#         phone_list = [phone_dict[letter] for letter in word]
#         print(phone_list)
#     except KeyError:
#         print("Sorry, only letters in the alphabet please")
#         converting_nato(phone_dict)
# converting_nato(phone_dict)