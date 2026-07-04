from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    window.after_cancel(timer)
    title_label.config(text="Pomo Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS +=1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        #print("long long break")
        title_label.config(text="Long Break", fg=RED)
        timer_countdown(long_break_seconds)
    elif REPS % 2 == 0:
        #print("short break")
        title_label.config(text="Short Break", fg=PINK) 
        timer_countdown(short_break_seconds)
    else:
        #print("WORK")
        title_label.config(text="Work Time", fg=GREEN)
        timer_countdown(work_seconds)
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer_countdown(count):

    count_minute= math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10 :
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(50,timer_countdown, count - 1)
    else:
        start_timer()
        marks=""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks+= "v/"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

#Labels
title_label = Label(text="Pomo Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1,row=0)

check_mark = Label(fg=GREEN , bg = YELLOW)
check_mark.grid(column = 1,row=3)

#Buttons
start_button = Button(text="Start", font="Arial", command=start_timer)
start_button.grid(column=0,row=3)

finish_button = Button(text="Finish", font="Arial", command=timer_reset)
finish_button.grid(column=2,row=3)


#Canvases
canvas = Canvas(width="200", height="224", bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png") ## we need to save the image in a variable using the PhotoImage command we would need the complete path if you need
canvas.create_image(100,112, image=tomato_img) ## We need a x and y position of the image
timer_text = canvas.create_text(100,122, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=2)


window.mainloop()
