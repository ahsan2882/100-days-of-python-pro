import tkinter as tk


def button_clicked():
    my_label["text"] = input.get()


windows = tk.Tk()
windows.title("My first GUI")
windows.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New text"
my_label.config(text="New text")
# my_label.pack()
my_label.grid(column=0, row=0)

# Input
input = tk.Entry(width=10)
# input.pack()
input.grid(column=4, row=3)

# Button
button = tk.Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = tk.Button(text="Click me", command=button_clicked)
# button.pack()
new_button.grid(column=2, row=0)


# def sum(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total


# print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(n=2, add=3, multiply=5)


# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seats = kw.get("seats")


# my_car = Car(make="Nissan", color="Black", seats=4)
# print(my_car.model)

windows.mainloop()
