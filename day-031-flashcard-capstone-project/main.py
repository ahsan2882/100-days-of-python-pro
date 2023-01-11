from tkinter import Tk, Canvas, PhotoImage, Button, Entry, Label
from pathlib import Path


BACKGROUND_COLOR = "#B1DDC6"
ITALIC_FONT = ("Arial", 40, "italic")
BOLD_FONT = ("Arial", 60, "bold")

CARD_BACK_PATH = Path(
    Path(__file__).parent.resolve(),
    'images',
    'card_back.png'
).resolve()


CARD_FRONT_PATH = Path(
    Path(__file__).parent.resolve(),
    'images',
    'card_front.png'
).resolve()


RIGHT_PATH = Path(
    Path(__file__).parent.resolve(),
    'images',
    'right.png'
).resolve()


WRONG_PATH = Path(
    Path(__file__).parent.resolve(),
    'images',
    'wrong.png'
).resolve()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back_photo = PhotoImage(file=CARD_BACK_PATH)
card_front_photo = PhotoImage(file=CARD_FRONT_PATH)
right_photo = PhotoImage(file=RIGHT_PATH)
wrong_photo = PhotoImage(file=WRONG_PATH)

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_photo)
canvas.create_text(400, 150, text="French", font=ITALIC_FONT)
canvas.create_text(400, 263, text="Bonjour", font=BOLD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

button_right = Button(image=right_photo, highlightthickness=0)
button_right.grid(column=1, row=1)

button_wrong = Button(image=wrong_photo, highlightthickness=0)
button_wrong.grid(column=0, row=1)

window.mainloop()
