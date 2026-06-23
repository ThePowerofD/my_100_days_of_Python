import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

# print(data)


# print('////////////////////////////////////////\n')
# dcit = {new_key:new_value for (index, row) in dataFrame.iterrows()}
phone_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phone_dict)

word = input("enter a word ").upper()
print("your letter")

phone_list = [phone_dict[letter] for letter in word]
print(phone_list)
