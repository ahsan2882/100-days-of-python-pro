import tkinter as tk


def button_clicked():
    miles = float(text_input.get())
    km = miles * 1.609
    km_label.config(text=f"{round(km, 3)}")


window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)

text_input = tk.Entry(width=10)
text_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = tk.Label(text="0")
km_label.grid(column=1, row=1)

km_unit_label = tk.Label(text="Km")
km_unit_label.grid(column=2, row=1)

button = tk.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
