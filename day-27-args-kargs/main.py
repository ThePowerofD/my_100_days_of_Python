from tkinter import *

window = Tk()
#code goes here

window.title("GUI program Title")
window.minsize(width = 500, height= 300)

#Label (component for window)
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
#my_label.pack(side = "left") ## makes my label go to the left also can go to the right or bottom there are others like expand ehich makes it center and try to fill the screen

my_label["text"] = "New Text"
my_label.config(text="New Text")


#Button

def button_clicked():
    if my_label["text"] == "I am a label":
        my_label.config(text="Button Got Clicked")
    else:
        my_label.config(text="I am a label")

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = Entry()
input.pack()


#Entry excrecise

def button_entry():
    #new_text = input2.get()
    my_label.config(text=input2.get())

input2 = Entry(width=10)
input2.pack()

button2 = Button(text="Change the label", command=button_entry)
button2.pack()

#code ends here
window.mainloop()


