from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage, messagebox
from pathlib import Path
import password_generator as pg
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pwd():
    generated_password = pg.genrate_password(random.randint(8, 16))
    password_entry.delete(0, 'end')
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


FILE_PATH = Path(
    Path(__file__).parent.resolve(),
    'data.txt'
).resolve()


def getDataFromForm():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    return (website, username, password)


def getDataAndSave():
    website, username, password = getDataFromForm()
    if website == "" or username == "" or password == "":
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        confirm = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")
    if confirm:
        with open(FILE_PATH, 'a') as secure_file:
            secure_file.write(f"{website} | {username} | {password}\n")
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #


def show_password():
    password_entry.config(show="")
    show_password_button.config(text="Hide", command=hide_password)


def hide_password():
    password_entry.config(show="*")
    show_password_button.config(text="Show", command=show_password)


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
website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW", pady=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW", pady=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(show="*")
password_entry.grid(column=1, row=3, sticky="EW", pady=2)

show_password_button = Button(text="Show", command=show_password)
show_password_button.grid(column=2, row=3, sticky="EW", padx=2)

generate_password_button = Button(
    text="Generate Password", command=generate_pwd)
generate_password_button.grid(
    column=1, row=4, columnspan=2, sticky="EW", padx=2)

add_entry_button = Button(text="Add", command=getDataAndSave)
add_entry_button.grid(column=1, row=5, columnspan=2, sticky="EW", pady=2)

window.mainloop()
