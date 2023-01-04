from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage
from pathlib import Path

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)

image_path = Path(
    Path(__file__).parent.resolve(),
    'logo.png'
).resolve()
photo = PhotoImage(file=image_path)
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW", pady=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW", pady=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW", pady=2)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="EW", padx=2)

add_entry_button = Button(text="Add")
add_entry_button.grid(column=1, row=4, columnspan=2, sticky="EW", pady=2)

window.mainloop()
