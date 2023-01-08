from tkinter import Tk, Label, Button, Entry, Canvas, PhotoImage, messagebox
from pathlib import Path
import password_generator as pg
import random
import os
import io
import json
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pwd():
    generated_password = pg.genrate_password(random.randint(8, 16))
    password_entry.delete(0, 'end')
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


# store secure file in this path
# change this path to your own path
FILE_PATH = Path(
    Path.home(),
    'secure',
    'passwords.json'
).resolve()
try:
    os.mkdir(Path(FILE_PATH).parent.resolve())
except FileExistsError:
    pass


def getDataAndSave():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': username,
            'password': password
        }
    }
    if website == "" or username == "" or password == "":
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        confirm = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?\n(Password copied to clipboard!)")
    if confirm:
        try:
            with open(FILE_PATH, 'r') as secure_file:
                secure_file_data = json.load(secure_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open(FILE_PATH, 'w') as secure_file:
                data = json.dumps(new_data, indent=4)
                secure_file.write(f'[{data}]')
        else:
            with open(FILE_PATH, 'w') as secure_file:
                secure_file_data.append(new_data)
                data = json.dumps(secure_file_data, indent=4)
                secure_file.write(data)
        finally:
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()


def search_password():
    site = website_entry.get()
    if site == "":
        messagebox.showerror(
            title="Oops", message="Please enter the website name to search!")
    else:
        with open(FILE_PATH, 'r') as secure_file:
            secure_file_data = json.load(secure_file)
            try:
                for data in secure_file_data:
                    if site in data:
                        username = data[site]['email']
                        password = data[site]['password']
                        option = messagebox.askyesno(
                            title=site, message=f"Email: {username} \nPassword: {password}\nDo you want to update this data?")
                        if option:
                            email_entry.delete(0, 'end')
                            email_entry.insert(0, data[site]['email'])
                            password_entry.delete(0, 'end')
                            password_entry.insert(0, data[site]['password'])
                            website_entry.config(state="disabled")
                            add_entry_button.config(
                                text="Update", command=updateData)
                        else:
                            pyperclip.copy(data[site]['password'])
                        break
                    else:
                        raise KeyError("No details for the website exists!")
            except KeyError as error:
                print(error)
                messagebox.showerror(
                    title="Oops", message="No details for the website exists!")


def updateData():
    username = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()

    if username == "" or password == "":
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        with open(FILE_PATH, 'r') as secure_file:
            secure_file_data = json.load(secure_file)
            for data in secure_file_data:
                if website in data:
                    data[website]['email'] = username
                    data[website]['password'] = password
                    break
        with open(FILE_PATH, 'w') as secure_file:
            data = json.dumps(secure_file_data, indent=4)
            secure_file.write(data)

    website_entry.config(state="normal")
    add_entry_button.config(text="Add", command=getDataAndSave)

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
website_entry.grid(column=1, row=1, sticky="EW", pady=2)
search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(column=2, row=1, padx=2, sticky="EW")

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
