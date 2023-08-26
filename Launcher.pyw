import tkinter as tk
import os
import darkdetect
from tkinter import *
from tkinter import ttk


originalDir = os.getcwd()


root = Tk() 
root.title("QG Toolbox")
root.geometry("500x290")


def startCmd(cmd):
    os.chdir("bin\\scrcpy")
    os.system("start cmd")
    os.chdir(originalDir)


def startShell(shell):
    os.chdir("bin\\scrcpy")
    os.system("start shell.bat")
    os.chdir(originalDir)


def apps(apps):
    os.startfile("bin\\apps.pyw")


def goRoot(root):
    os.startfile("bin\\root.exe")


def flash(flash):
    os.startfile("bin\\flash.exe")


def scrcpy(scrcpy):
    os.system("bin\\scrcpy\\scrcpy -d")


def about(about):
    os.startfile("bin\\about.exe")

    
def centerWindow(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


buttonCmd = ttk.Button(root)
buttonCmd["text"] = "打开“命令行”"
buttonCmd.bind("<Button-1>", startCmd)
buttonCmd.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")


buttonShell = ttk.Button(root)
buttonShell["text"] = "打开“Shell”"
buttonShell.bind("<Button-1>", startShell)
buttonShell.grid(row=1, column=0, padx=10, pady=10, sticky="nesw")


buttonApps = ttk.Button(root)
buttonApps["text"] = "应用管理"
buttonApps.bind("<Button-1>", apps)
buttonApps.grid(row=2, column=0, padx=10, pady=10, sticky="nesw")


buttonRoot = ttk.Button(root)
buttonRoot["text"] = "Root 管理"
buttonRoot.bind("<Button-1>", goRoot)
buttonRoot.grid(row=3, column=0, padx=10, pady=10, sticky="nesw")


buttonFlash = ttk.Button(root)
buttonFlash["text"] = "刷写镜像"
buttonFlash.bind("<Button-1>", flash)
buttonFlash.grid(row=4, column=0, padx=10, pady=10, sticky="nesw")


buttonScrcpy = ttk.Button(root)
buttonScrcpy["text"] = "画面投屏"
buttonScrcpy.bind("<Button-1>", scrcpy)
buttonScrcpy.grid(row=0, column=1, padx=10, pady=10, sticky="nesw")


buttonAbout = ttk.Button(root)
buttonAbout["text"] = "关于"
buttonAbout.bind("<Button-1>", about)
buttonAbout.grid(row=1, column=1, padx=10, pady=10, sticky="nesw")


aboutTitle = tk.Label(root, text="关于设备")
aboutTitle.grid(row=0, column=2, padx=100, pady=10,sticky="nesw")


deviceBrand = os.popen("adb shell getprop ro.product.brand")
deviceBrand = deviceBrand.read()
brand = tk.Label(root, text="厂商：" + deviceBrand)
brand.grid(row=1, column=2, padx=100, pady=10,sticky="nesw")


deviceModel = os.popen("adb shell getprop ro.product.model")
deviceModel = deviceModel.read()
model = tk.Label(root, text="型号：" + deviceModel)
model.grid(row=2, column=2, padx=100, pady=10, sticky="nesw")


AndroidVersion = os.popen("adb shell getprop ro.build.version.release")
AndroidVersion = AndroidVersion.read()
Android = tk.Label(root, text="Android：" + AndroidVersion)
Android.grid(row=3, column=2, padx=100, pady=10, sticky="nesw")


deviceSoc = os.popen("adb shell getprop ro.soc.model")
deviceSoc = deviceSoc.read()
soc = tk.Label(root, text="Soc：" + deviceSoc)
soc.grid(row=4, column=2, padx=100, pady=10, sticky="nesw")


theme = ["light","dark"]
root.tk.call("source", "sv.tcl")
if darkdetect.isDark():
    root.tk.call("set_theme", theme[1])
else:
    root.tk.call("set_theme", theme[0])


centerWindow(root)
root.resizable(False, False)
os.system("adb devices")
root.mainloop()