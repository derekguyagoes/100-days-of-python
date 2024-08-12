from tkinter import *

KM_VALUE = 1.609344


def calculate():
    miles = int(input.get())
    calculated_value.config(text=miles * KM_VALUE)


window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=500, height=250)
window.config(padx=10, pady=10)

# row 0
# null, textbox label
input = Entry(width=5)
input.grid(row=0, column=1)
input_label = Label(text="Miles:")
input_label.grid(row=0, column=2)

# row 1
# label, valuefromtb, label
words = Label(text="is equal to:")
words.grid(row=1, column=0)

calculated_value = Label(text="0")
calculated_value.grid(row=1, column=1)

km = Label(text="Km")
km.grid(row=1, column=2)

# row 2
# null, button, null
calculate = Button(text="Calculate", command=calculate)
calculate.grid(row=2, column=1)
window.mainloop()
