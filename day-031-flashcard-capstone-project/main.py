from tkinter import Tk, Canvas, PhotoImage, Button, Entry, Label
from pathlib import Path
import pandas as pd
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
ITALIC_FONT = ("Arial", 40, "italic")
BOLD_FONT = ("Arial", 60, "bold")

DATA_FILE_PATH = Path(
    Path(__file__).parent.resolve(),
    'data',
    'french_words.csv'
).resolve()

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

CORRECT_ANSWER_BUTTON_IMAGE_PATH = Path(
    Path(__file__).parent.resolve(),
    'images',
    'right.png'
).resolve()

UNKNOWN_ANSWER_BUTTON_IMAGE_PATH = Path(
    Path(__file__).parent.resolve(),
    'images',
    'wrong.png'
).resolve()

df = pd.read_csv(DATA_FILE_PATH)
words_to_learn = df.to_dict(orient="records")


def pick_word():
    new_word = choice(words_to_learn)
    new_word_french = new_word["French"]
    new_word_english = new_word["English"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_word_french, fill="black")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back_photo = PhotoImage(file=CARD_BACK_PATH)
card_front_photo = PhotoImage(file=CARD_FRONT_PATH)
correct_answer_icon = PhotoImage(file=CORRECT_ANSWER_BUTTON_IMAGE_PATH)
unknown_answer_icon = PhotoImage(file=UNKNOWN_ANSWER_BUTTON_IMAGE_PATH)

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front_photo)
card_title = canvas.create_text(400, 150, text="", font=ITALIC_FONT)
card_word = canvas.create_text(400, 263, text="", font=BOLD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

button_right = Button(image=correct_answer_icon,
                      highlightthickness=0, command=pick_word)
button_right.grid(column=1, row=1)

button_wrong = Button(image=unknown_answer_icon,
                      highlightthickness=0, command=pick_word)
button_wrong.grid(column=0, row=1)

pick_word()

window.mainloop()
