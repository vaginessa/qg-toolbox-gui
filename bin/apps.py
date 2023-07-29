import tkinter as tk
import os
import darkdetect
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
root.title("应用管理")
root.geometry("500x260")


originalDir = os.getcwd()


def centerWindow(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def installApk(installApk):
    apk = Tk()
    apk.withdraw()
    apkPath = filedialog.askopenfilename(title="选择一个 apk 文件", filetypes=(("APK Files", "*.apk"),))
    os.chdir("bin\\scrcpy")
    os.system("adb install " + apkPath)
    os.chdir(originalDir)


installApp = ttk.Button(root, text="安装应用")
installApp.bind("<Button-1>", installApk)
installApp.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")


theme = ["light","dark"]
root.tk.call("source", "sv.tcl")
if darkdetect.isDark():
    root.tk.call("set_theme", theme[1])
else:
    root.tk.call("set_theme", theme[0])


centerWindow(root)
root.mainloop()