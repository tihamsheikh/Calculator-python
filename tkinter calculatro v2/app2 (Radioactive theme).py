import tkinter as tk
import math



# window init
app = tk.Tk()
app.title("Calculator")
app.resizable(False, False)

# window style and font
app.config(bg="black")

# button action
def click(btn):
    # error time disabling input block (error hand)
    if input_display.get() == "Error " and btn != "AC":
        return


    if input_display.get() == "" and btn == "=":    # empty submit (error hand)
        input_display.set("")

    elif btn == "=":                # submission
        try:
            exp = input_display.get().replace("^", "**")
            res = exp.replace("%", "/100 *")
            input_display.set(eval(res))

        except Exception:
            input_display.set("Error ")

    elif btn == "log":              # value for log10
        print(input_display.get())
        try:
            res = math.log10(float(input_display.get()))
            input_display.set(str(res))

        except Exception:
            input_display.set("Error ")
        
    elif btn == "π":                # value for pi
        try:
            input_display.set(input_display.get() + str(math.pi))
        except Exception:
            input_display.set("Error ")

    elif btn == "√":                # exponential
        try:
            res = math.sqrt(float(input_display.get()))
            input_display.set(str(res))
        except Exception:
            input_display.set("Error ")

    elif btn == "Exp":              # value for e
        try:
            input_display.set(input_display.get() + str(math.e))
        except Exception:
            input_display.set("Error ")

    elif btn == "sin":              # sin/cos/tan
        try:
            res = math.sin(math.radians(float(input_display.get())))
            input_display.set((str(res)))

        except Exception:
            input_display.set("Error ")

    elif btn == "cos":
        try:
            res = math.cos(math.radians(float(input_display.get())))
            input_display.set((str(res)))
        except Exception:
            input_display.set("Error ")

    elif btn == "tan":
        try:
            res = math.tan(math.radians(float(input_display.get())))
            input_display.set((str(res)))
        except Exception:
            input_display.set("Error ")

    elif btn == "x!":               # factorial
        try:                    
            exp = input_display.get().replace("x!", "")
            res = math.factorial(int(exp))
            input_display.set(str(res))
        except Exception:
            input_display.set("Error ")

    elif btn == "del":
        thing = input_display.get()           # single delete
        input_display.set(thing[:len(thing)-1])   

    elif btn == "AC":
        input_display.set("")                 # total clearing

    else:
         input_display.set(input_display.get() + btn)   # value adding

# input box
input_display = tk.StringVar()

# input init and design
visual_display = tk.Entry(master=app, textvariable=input_display, font="Arial 22", bd=7, bg="lime", justify="right")
visual_display.grid(row=0, column=0, columnspan=4, ipadx= 23, ipady=18, padx=3, pady=4)

button = [
    ("π","Exp","log","x!"),
    ("sin", "cos", "tan", "del"),
    ("√", "^", "%", "/"),
    ("1", "2", "3", "*"),
    ("4", "5", "6", "-"),
    ("7", "8", "9", "+"),
    (".", "0", "AC", "="),
]

# button placement
for i, row in enumerate(button):
    for j, btn_text in enumerate(row):
        btn = tk.Button(master=app, text=btn_text, font="Arial 20 bold", bd=6, bg="green", command= lambda text=btn_text: click(text))
        btn.grid(row=i+1, column=j, ipadx= 8, ipady=6, columnspan=1, padx=3, pady=3,sticky="nsew")


# app run
app.mainloop()






















