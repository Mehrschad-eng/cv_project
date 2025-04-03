import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("calculator")
root.geometry("300x400")
display_var = tk.stringvar()
display_var.set("0")
is_calculated = False
display = tk.Entry(root, textvariable=display_var, font=("Arial", 20), justify="right", bd=10, insertwidth=4, width=15)
