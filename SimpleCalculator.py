# Created with tkinter lib

import tkinter as tk

# window init
app = tk.Tk()
app.title("Simple Calculator")
app.resizable(False, False)

# window style and font
app.config(bg="lightblue")


# button action
def click(btn):

    if input_display.get() == "" and btn == "=":  # empty submit
        input_display.set("")

    elif btn == "=":  # submission
        try:
            exp = input_display.get().replace("^", "**")    # exponential
            res = exp.replace("%", "/100 *")    # for percentage
            input_display.set(eval(res))

        except Exception:
            input_display.set("Error ")

    elif btn == "√":  # exponential
        try:
            res = math.sqrt(float(input_display.get()))
            input_display.set(str(res))
        except Exception:
            input_display.set("Error ")

    elif btn == "C":
        input_display.set("")  # total clearing

    else:
        input_display.set(input_display.get() + btn)  # value adding

# main function
# input box
input_display = tk.StringVar()

# input init and design
visual_display = tk.Entry(master=app, textvariable=input_display, font="Arial 22", bd=7, bg="white", justify="right")
visual_display.grid(row=0, column=0, columnspan=4, ipadx=23, ipady=18, padx=3, pady=4)

button = [
    ("C", "^", "%", "/"),
    ("1", "2", "3", "*"),
    ("4", "5", "6", "-"),
    ("7", "8", "9", "+"),
    (".", "0", "√", "="),
]

# button placement
for i, row in enumerate(button):
    for j, btn_text in enumerate(row):
        btn = tk.Button(master=app, text=btn_text, font="Arial 20 bold", bd=3, bg="gray",
                        command=lambda text=btn_text: click(text))
        btn.grid(row=i + 1, column=j, ipadx=8, ipady=6, columnspan=1, padx=3, pady=3, sticky="nsew")

# app run
app.mainloop()





















