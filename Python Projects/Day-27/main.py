from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Input Entry

user_input = Entry(width=10)
user_input.grid(column=4, row=3)
# print(user_input.get())

# Button
new_button = Button(text="New Button")
new_button.grid(column=3, row=0)


def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)



button = Button(text="click me", command=button_clicked)
button.grid(column=2, row=2)

window.mainloop()
