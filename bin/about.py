import tkinter as tk
import darkdetect
import os
import webbrowser
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


def openOpenSource():
    os.startfile("bin\\open source.html")


def openQq(openQq):
    webbrowser.open_new("https://qm.qq.com/q/oLoAhqhnQm&personal_qrcode_source=4")


def startGithub(startGithub):
    webbrowser.open_new("https://github.com/qgmzmy/qg-toolbox-gui")


openGithub = ttk.Button(root, text="GitHub")
openGithub.bind("<Button-1>", startGithub)
openGithub.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")


openQQ = ttk.Button(root, text="联系作者（QQ）")
openQQ.bind("<Button-1>", openQq)
openQQ.grid(row=1, column=0, padx=10, pady=10, sticky="nesw")


openSource = ttk.Label(root, text="开源相关", foreground="#0078d4", cursor="hand2")
openSource.bind("<Button-1>", lambda e: openOpenSource())
openSource.grid(row=2, column=0, padx=10, pady=10, sticky="nesw")


theme = ["light","dark"]
root.tk.call("source", "sv.tcl")
if darkdetect.isDark():
    root.tk.call("set_theme", theme[1])
else:
    root.tk.call("set_theme", theme[0])


centerWindow(root)
root.mainloop()