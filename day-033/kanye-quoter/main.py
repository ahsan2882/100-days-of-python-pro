from tkinter import Tk, Button, Canvas, PhotoImage
from pathlib import Path
import requests

BACKGROUND_IMAGE_PATH = Path(
    Path(__file__).parent.resolve(),
    'background.png'
).resolve()

KANYE_IMAGE_PATH = Path(
    Path(__file__).parent.resolve(),
    'kanye.png'
).resolve()


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    quote = response.json()['quote']
    canvas.itemconfig(quote_text, text=quote)
    # Write your code here.


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=BACKGROUND_IMAGE_PATH)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=(
    "Arial", 18, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=KANYE_IMAGE_PATH)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
get_quote()

window.mainloop()
