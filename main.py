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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    window.after_cancel(timer)
    Timerlabel.config(text="Timer", fg=GREEN)
    canvas.itemconfig(Timertext, text="00:00")
    Checkmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        Timerlabel.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Timerlabel.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        Timerlabel.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    else:
        count_sec = f"{count_sec}"

    canvas.itemconfig(Timertext, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        work_sessions = reps // 2
        marks = "✓" * work_sessions
        Checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=110, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
Timertext = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

Timerlabel = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
Timerlabel.grid(column=1, row=0)

Startbutton = Button(text="Start", command=start)
Startbutton.grid(column=0, row=2)

Checkmark = Label(text="", fg=GREEN, bg=YELLOW)
Checkmark.grid(column=1, row=3)

Resetbutton = Button(text="Reset", command=reset)
Resetbutton.grid(column=2, row=2)

window.mainloop()

