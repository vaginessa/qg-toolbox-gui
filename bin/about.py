import tkinter as tk
import darkdetect
from tkinter import *
from tkinter import ttk


def centerWindow(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


root = Tk()
root.title("关于")
root.geometry("200x150")


theme = ["light","dark"]
root.tk.call("source", "sv.tcl")
if darkdetect.isDark():
    root.tk.call("set_theme", theme[1])
else:
    root.tk.call("set_theme", theme[0])


centerWindow(root)
root.mainloop()