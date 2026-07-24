BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd

from tkinter import *
from tkinter import messagebox # it is not a tkinter class it is another code module

data = pd.read_csv("data/flashcard_german_clean.csv")

####------------------ UI Setup --------------------------------#####
window = Tk()
window.title("Deutsch Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#----Images----#

#Lock Image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_image = PhotoImage(file ="images/card_front.png")
canvas.create_image(400, 263, image=card_image)

canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text= "Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(highlightthickness=0)



#----Labels----#


#website_text.grid(row=1,column=0, sticky="e")


#email_username_text = Label(text="Email/Username:")
#email_username_text.grid(row=2,column=0, sticky="e")

#password_text = Label(text="Password")
#password_text.grid(row=3,column=0, sticky="e")

#----Buttons----#



right_check = PhotoImage(file="images/right.png")
right_button = Button(image=right_check, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=1,column=1)

wrong_cross = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_cross, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

#search_button = Button(text="Search", command=search_password)
#search_button.grid(row=1,column=2, sticky="ew")

#----ENTRYS----#


window.mainloop()