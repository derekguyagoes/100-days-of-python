from tkinter import *

KM_VALUE = 1.609


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * KM_VALUE
    calculated_value.config(text=f"{km}")


window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

# row 0
# null, textbox label
miles_input = Entry(width=5)
miles_input.grid(row=0, column=1)

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
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(row=2, column=1)

window.mainloop()
