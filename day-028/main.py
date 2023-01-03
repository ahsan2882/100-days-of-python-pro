
from tkinter import Tk, Canvas, PhotoImage, Label, Button
from pathlib import Path
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None
marks = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    start_button.config(command=start_timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    check_marks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #


work_sec = WORK_MIN*1
short_break_sec = SHORT_BREAK_MIN*1
long_break_sec = LONG_BREAK_MIN*1


def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.lift()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)


def start_timer():
    global reps
    start_button.config(command='')
    reps += 1
    title_label.config(text='Work', fg=GREEN)
    count_down(work_sec, False)


def next_timer(reps):
    global marks
    if reps % 8 == 0:
        marks += '✔'
        count_down(long_break_sec, True)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        marks += '✔'
        count_down(short_break_sec, True)
        title_label.config(text='Break', fg=PINK)
    elif reps % 2 != 0:
        count_down(work_sec, False)
        title_label.config(text='Work', fg=GREEN)
    check_marks.config(text=marks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count, show):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f'0{count_min}'
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if show:
        focus_window("on")
    else:
        focus_window("off")
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1, show)
    elif count == 0:
        reps += 1
        if reps > 8:
            reps = 0
            reset_timer()
        else:
            next_timer(reps)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
ws = window.winfo_screenwidth()  # width of the screen
hs = window.winfo_screenheight()  # height of the screen
x = (ws/2) - (200)
y = (hs/2) - (324/2)
window.config(padx=100, pady=50, bg=YELLOW)
window.geometry('%dx%d+%d+%d' % (450, 400, x, y))
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


image_path = Path(
    Path(__file__).parent.resolve(),
    'tomato.png'
).resolve()

photo = PhotoImage(file=image_path)
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 112, text='00:00', fill="white",
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.config(command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.config(command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
