import tkinter as tk


def on_click(btn):
    # print(btn)  # error handling

    if btn == "=":
        try:
            # print('1= ', btn)

            formula = display.get().replace('^', '**')
            # print('2= ', formula)

            result = formula.replace('%', '/100*')
            # print('3= ', result)

            display.set(eval(result))
        except Exception:
            display.set('Error')
        # print(display.get(), result)

    elif btn == "%":
        display.set(display.get() + '%')

    elif btn == "C":
        display.set('')

    else:
        display.set(display.get() + btn)

app = tk.Tk()
app.title("Premium Deluxe Calculator")

display = tk.StringVar()    # main window


vis_display = tk.Entry(app, textvariable=display , font=("Times New Roman", 16), justify='center')   # input window
vis_display.grid(row=0, column=0, columnspan=4, ipadx=12, ipady=12)   # item holding place

buttons = [
    ('1', '2', '3', '+', '-'),
    ('4', '5', '6', '*', '/'),
    ('7', '8', '9', '^', '%'),
    ('C', '0', '.', '=')
]

# text display on btn place
for i, row in enumerate(buttons):
    # print('i and r', i, row)
    for j, btn_text in enumerate(row):
        # print('J IN loop',j, btn_text)

        if btn_text == '=':
            btn = tk.Button(app, text=btn_text, font=("Times New Roman", 18), command=lambda text=btn_text: on_click(text))
            btn.grid(row=i + 1, column=j, columnspan=2 , ipadx=20, ipady=20, sticky='nsew') # north-south ew
        else:
            btn = tk.Button(app, text=btn_text, font=("Times New Roman", 18), command=lambda text=btn_text: on_click(text))
            btn.grid(row=i + 1, column=j, ipadx=20, ipady=20, sticky='nsew')

app.mainloop()
