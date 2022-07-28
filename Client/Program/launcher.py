import os
from pydoc import plain
import sys
import tkinter as tk
from typing import Sized
import urllib.request
import time

MainMenu = "python /Users/bradygustafson/MultiMod/MacOS/MainMenu.py"

root = tk.Tk()
root.title("MultiMod Launcher")
root.geometry("300x200")
root.resizable(False, False)
# Don't show the title bar
root.overrideredirect(True)
# Place the window in the center of the screen
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))


try:
    urllib.request.urlopen("http://www.google.com")
    img = tk.PhotoImage(file="/usr/local/bin/MultiMod/icon.png")
    # Show the image on the window and center it and resize it
    label = tk.Label(root, image=img)
    # Lable size is half of the window size
    label.size = (int(root.winfo_reqwidth() / 2), int(root.winfo_reqheight() / 2))
    label.image = img
    label.pack()
    root.update()
    time.sleep(3)
    root.withdraw()
    root.destroy()
    os.system(MainMenu)
except urllib.request.URLError:
    loadinginfo = tk.Label(root, text="No internet connection detected.\nPlease connect to the internet and try again.", font=("Helvetica", 12))
    loadinginfo.pack()

root.mainloop()
