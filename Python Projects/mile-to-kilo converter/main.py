from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=2, row=1)

is_equal_to_label = Label(text="is_equal_to", font=("Arial", 12))
is_equal_to_label.grid(column=1, row=2)


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")


calculate_button = Button(text="Button", command=miles_to_km)
calculate_button.grid(column=2, row=3)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=3, row=1)

kilometer_label = Label(text="Km", font=("Arial", 12))
kilometer_label.grid(column=3, row=2)

kilometer_result_label = Label(text="0", font=("Arial", 12))
kilometer_result_label.grid(column=2, row=2)


window.mainloop()
