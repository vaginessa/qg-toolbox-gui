import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading
import darkdetect

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
    os.chdir("bin\\scrcpy")

    installing = tk.Toplevel()
    installing.title("安装应用")
    installing.geometry("250x100")

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
        # else:
            
        installButton.config(state="normal")  # 启用安装按钮

    t = threading.Thread(target=installApkThread)
    t.start()
root = tk.Tk()
root.title("应用管理")
root.geometry("500x260")

installButton =ttk.Button(root, text="安装应用")
installButton.bind("<Button-1>", installApk)
installButton.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")

theme = ["light", "dark"]
root.tk.call("source", "sv.tcl")
if darkdetect.isDark():
    root.tk.call("set_theme", theme[1])
else:
    root.tk.call("set_theme", theme[0])

centerWindow(root)
root.resizable(False, False)

root.mainloop()