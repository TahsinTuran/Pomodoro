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
reps = 0
timer1 = None

# ---------------------------- TIMER RESET ------------------------------- # 
def resettimer():
    global reps
    reps = 0
    window.after_cancel(timer1)
    canvas.itemconfig(timer, text="00:00")
    title_text.config(text="TIMER", fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer():
    global reps
    reps += 1
    WORK_MIN = 25 * 60

    if reps % 2 == 1:
        countdown(WORK_MIN)
        title_text.config(text="YES, WORK", fg=GREEN)
    elif reps % 2 == 0 and reps != 8:
        title_text.config(text="SHOWDY BREAK", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        title_text.config(text="LONG BREAK", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer1
        timer1 = window.after(1, countdown, count-1)
    else:
        starttimer()
        marks = ""
        work_done = math.floor(reps/2)
        for _ in range(work_done):
            marks += "🗹"
        check_marks.config(text=marks)

    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 122, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_text = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_text.grid(row=0, column=1)

start_button = Button(highlightthickness=0, text="Start", command=starttimer)
start_button.grid(column=0, row=3)

reset_button = Button(highlightthickness=0, text="Reset", command=resettimer)
reset_button.grid(column=2, row=3)

check_marks = Label(text="", bg=YELLOW, highlightthickness=0)
check_marks.grid(column=1, row=3)

window.mainloop()