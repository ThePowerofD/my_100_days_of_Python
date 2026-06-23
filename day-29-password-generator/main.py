from tkinter import *
from tkinter import messagebox # it is not a tkinter class it is another code module
import pyperclip
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

    #messagebox.showinfo(title="",text="")
    

    if website_entry.get() == "" or email_username_entry.get() == "" or password_entry.get()=="":
        messagebox.showwarning(title="Empty input error", message="Please do not leave any fields empty ")
        return
    
    is_ok = messagebox.askokcancel(title=f"{website_entry.get()}", message=f"This are the details entered: \nEmail:{email_username_entry.get()}" f"\nPassword: {password_entry.get()} \nIs it ok to save?")

    if is_ok:   

        with open("data.txt", "a") as data_file:
            data_file.write(f"{website_entry.get()} | {email_username_entry.get()} | {password_entry.get()}\n")
            website_entry.delete(0, END)
            email_username_entry.delete(0,END)
            password_entry.delete(0,END)
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

#----ENTRYS----#

website_entry = Entry(width = 35)
website_entry.grid(row=1,column=1, columnspan=2, sticky="ew")
website_entry.focus()

email_username_entry = Entry(width = 35)
email_username_entry.grid(row=2,column=1, columnspan=2, sticky="ew")
email_username_entry.insert(0, "medinacoll97@gmail.com") #END instead of 0 inserts at the end of entry

password_entry = Entry(width = 30)
password_entry.grid(row=3,column=1, sticky="w")


window.mainloop()