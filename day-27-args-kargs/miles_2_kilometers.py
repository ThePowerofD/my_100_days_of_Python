from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
#window.minsize(width=500, height=200)
window.config(padx=150, pady=50)
# code starts here

def calculate():
    miles = float(input.get())
    km = miles * 1.609
    km_answer.config(text= km)
    #return km_answer.config(text=km)

#Entries
input = Entry(width=15)
input.grid(row=0, column=1)

#Labels
miles_label = Label(text="Miles", font="Arial")
miles_label.grid(row=0, column=2)

km_answer = Label(text=" " , font="Arial")
km_answer.grid(row=1, column=1)

is_equal_label = Label(text="is equal to", font="Arial")
is_equal_label.grid(row=1, column=0)

km_label = Label(text="Km", font="Arial")
km_label.grid(row=1, column=2)


#Buttons
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

#code ends here
window.mainloop()