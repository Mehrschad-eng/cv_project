import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("calculator")
root.geometry("300x400")
display_var = tk.StringVar()
display_var.set("0")
is_calculated = False
display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), justify="right", bd=10, insertwidth=4, width=15)
display.grid(row=0, column=0, columnspan=4, pady=10)
def button_click(number):
    global is_calculated
    concurrent = display_var.get()
    if is_calculated:
        if number in "0123456789":
            display_var.set(number)
            is_calculated = False
            return
        elif number == ".":
            display_var.set("0.")
            is_calculated = False
            return
        if number == ".":
            if not current or current[-1] in "+-*/":
                display_var.set(current + "0.")
            else:
                parts = [part for part in current.replace("+", " ").replace("-", " ").replace("*", " ").replace("/", " ").split if part]
                if parts and "." in parts[-1]:
                    return
                display_var.set(current + ".")
        else:
            if current == "0":
                display_var.set(number)
            else:
                display_var.set(current + number)
        is_calculated = False
def clear():
    display_var.set("0")
    global is_calculated
    is_calculated = False
def calculate():
    global is_calculated
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
        is_calculated = True
    except:
        messagebox.showerror("Error", "Invalid input")
def add_operator(operator):
    global is_calculated
    current = display_var.get()
    if not current or current == "0":
        if operator == "-":
            display_var.set(operator)
    else:
        if current[-1] in "+-*/":
            display_var.set(current + operator)
    is_calculated = False

buttons = [("7", 1, 0), ("8", 1, 1), ("9", 1, 2),("/", 1, 3),
           ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),("*", 2, 3),
           ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),("-", 3, 3),
           ("0", 4, 0), (".", 4, 1), ("=", 4, 2),("+", 4, 3),]
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text = text, font = ("Arial", 16), padx = 20, pady = 10, command = calculate)
    elif text in "+-*/":
        btn = tk.Button(root, text = text, font = ("Arial", 16), padx = 20, pady = 10, command = lambda t=text : add_operator(t))
    else:
        btn = tk.Button(root, text=text, font=("Arial", 16), padx=20, pady=10, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx = 5, pady = 5)
clear_btn = tk.Button(root, text = "c", font = ("Arial", 16), padx = 20, pady = 10, command = clear)
clear_btn.grid(row=5, column=0, columnspan = 4, sticky = "we", padx = 5)
root.mainloop()
