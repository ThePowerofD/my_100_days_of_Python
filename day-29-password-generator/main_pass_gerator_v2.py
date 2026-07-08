from tkinter import *
from tkinter import messagebox # it is not a tkinter class it is another code module
import pyperclip
import json
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    g_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0 ,g_password)
    pyperclip.copy(g_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    #messagebox.showinfo(title="",message="")
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {"email":email, "password":password,}
        

    }

    if website == "" or email == "" or password =="":
        messagebox.showwarning(title="Empty input error", message="Please do not leave any fields empty ")
        return
    
    is_ok = messagebox.askokcancel(title=f"{website}", message=f"This are the details entered: \nEmail:{email}" f"\nPassword: {password} \nIs it ok to save?")

    if is_ok:   
        try:
            with open("data.json", "r") as data_file_json:

                #Reading old data
                data = json.load(data_file_json)
                #Updating old Data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data    

        with open("data.json", "w") as data_file_json:    
            #saving updated data
            json.dump(data, data_file_json, indent=4)
            
            website_entry.delete(0, END)
            password_entry.delete(0,END)

def search_password():

    website = website_entry.get()
    #email = email_username_entry.get()
    #password = password_entry.get()


    try:
        with open("data.json", "r") as data:

            web_data = json.load(data)
            if website in web_data:
                messagebox.showinfo(title=f"{website}",message=f"Website:{website}\nEmail:{web_data[website]['email']}\nPassword:{web_data[website]['password']}")
            else:
                messagebox.showinfo(title="Error" ,message="Please input valid webisite name")
            
    except FileNotFoundError:
        messagebox.showinfo(title="Error" ,message="No Data File Found")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#----Images----#

#Lock Image
canvas = Canvas(width=200, height=200)
my_image = PhotoImage(file="logo.png")  # your image file
canvas.create_image(100, 100, image=my_image)  # x, y = center point
canvas.grid(row=0,column=1)
canvas.config(highlightthickness=0)



#----Labels----#
website_text = Label(text="Website:")
website_text.grid(row=1,column=0, sticky="e")

email_username_text = Label(text="Email/Username:")
email_username_text.grid(row=2,column=0, sticky="e")

password_text = Label(text="Password")
password_text.grid(row=3,column=0, sticky="e")

#----Buttons----#
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36, command=save)
add_button.grid(row=4,column=1, columnspan=2, sticky="ew")

search_button = Button(text="Search", command=search_password)
search_button.grid(row=1,column=2, sticky="ew")

#----ENTRYS----#

website_entry = Entry(width = 32)
website_entry.grid(row=1,column=1, columnspan=1, sticky="w")
website_entry.focus()

email_username_entry = Entry(width = 35)
email_username_entry.grid(row=2,column=1, columnspan=2, sticky="ew")
email_username_entry.insert(0, "medinacoll97@gmail.com") #END instead of 0 inserts at the end of entry

password_entry = Entry(width = 30)
password_entry.grid(row=3,column=1, sticky="ew")


window.mainloop()