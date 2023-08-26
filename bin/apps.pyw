import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os
import threading
import darkdetect
import re

originalDir = os.getcwd()

def centerWindow(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def installApk(event):
    apkPath = filedialog.askopenfilename(title="选择一个 apk 文件", filetypes=(("APK 文件", "*.apk"), ))
    os.chdir(originalDir + "\\bin\\scrcpy")

    installing = tk.Toplevel()
    installing.title("安装应用")
    installing.geometry("250x100")
    centerWindow(installing)

    installProgressbar = ttk.Progressbar(installing, length=200, mode="indeterminate")
    installProgressbar.pack(pady=20)
    installProgressbar.start()

    installButton.config(state="disabled")  # 禁用安装按钮

    installing.deiconify()  # 显示安装窗口

    def installApkThread():
        installOutput = os.popen("adb install " + apkPath)
        installOutput = installOutput.read()
        installProgressbar.stop()
        installing.destroy()
        if "Success" in installOutput:
            messagebox.showinfo("安装应用", "安装成功")
        else:
            messagebox.showerror("安装应用", "安装失败")
        installButton.config(state="normal")  # 启用安装按钮

    t = threading.Thread(target=installApkThread)
    os.chdir(originalDir)
    t.start()


def uninstallApp(event):


    def uninstall(uninstall):
        packageName = packageStr.get()
        uninstalled = os.popen("adb uninstall " + packageName)
        uninstalled = uninstalled.read()
        print(uninstalled)
        if "Success" in uninstalled:
            messagebox.showinfo("卸载应用", "卸载成功")
        else:
            messagebox.showerror("卸载应用", "卸载失败")
        uninstallButton.config(state=tk.NORMAL)


    uninstallButton.config(state=tk.DISABLED)  # 禁用卸载按钮


    inputPackage = tk.Toplevel()
    inputPackage.title("卸载应用")
    inputPackage.geometry("250x100")

    thisPackage = os.popen("adb shell dumpsys window | findstr mCurrentFocus")
    print(type(thisPackage))
    thisPackage = thisPackage.read()
    print(thisPackage)
    pattern = r"([a-zA-Z0-9_\.]+)\/"
    match_obj = re.search(pattern, thisPackage)

    if match_obj is not None:
        packageName = match_obj.group(1)
        print(packageName)

        package = ttk.Frame(inputPackage)
        packageStr = StringVar()
        packageStr.set(packageName)
        Entry = ttk.Entry(package, width=23, textvariable=packageStr)
        package.grid()
        Entry.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

    else:
        package = ttk.Frame(inputPackage)
        packageStr = StringVar()
        Entry = ttk.Entry(package, width=23, textvariable=packageStr)
        package.grid()
        Entry.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        print(packageStr.get())

    getPackage = ttk.Button(inputPackage, text="→")
    getPackage.bind("<Button-1>", uninstall)
    getPackage.grid(row=0, column=1, padx=0, pady=10, sticky="nesw")

    inputPackage.mainloop()

    centerWindow(inputPackage)

    uninstalling = tk.Toplevel()
    uninstalling.title("卸载应用")
    uninstalling.geometry("250x100")
    centerWindow(uninstalling)


root = tk.Tk()
root.title("应用管理")
root.geometry("500x290")


installButton =ttk.Button(root, text="安装应用")
installButton.bind("<Button-1>", installApk)
installButton.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")


uninstallButton = ttk.Button(root, text="卸载应用")
uninstallButton.bind("<Button-1>", uninstallApp)
uninstallButton.grid(row=1, column=0, padx=10, pady=10, sticky="nesw")


sysApp = ttk.Button(root, text="转为系统应用")
sysApp.bind("<Button-1>")
sysApp.grid(row=2, column=0, padx=10, pady=10, sticky="nesw")


theme = ["light", "dark"]
root.tk.call("source", "sv.tcl")
if darkdetect.isDark():
    root.tk.call("set_theme", theme[1])
else:
    root.tk.call("set_theme", theme[0])

centerWindow(root)
root.resizable(False, False)

root.mainloop()