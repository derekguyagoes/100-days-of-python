from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("i got cliecked")


window = Tk()
window.title("my first gui")
window.minsize(500, 300)
window.config(padx=20, pady=20)

# label
my_label = Label(text="i'm a label", font=("Arial", 24, "bold"))
my_label["text"] = "new text"
my_label.config(text="newer text")
my_label.grid(column=0, row=0)
my_label.config(padx=5, pady=5)

# button
button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="new button")
new_button.grid(column=2, row=1)
# entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
