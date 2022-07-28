from re import M, S, T
import time
import tkinter as tk
import requests
from tkinter import Tk, Canvas, NW
import sys
import os
from turtle import position

list = [
    "Minecraft",
]

Minecraft = "/usr/local/bin/MultiMod/LocalFiles/Minecraft/Icon.png"

root = tk.Tk()
root.title("MultiMod Menu")
root.geometry("800x600")
root.resizable(False, False)
root.configure(background='#212121')

def install(mfile, install_button, back_button, title_label, desc_label, req_label):
    install_button.pack_forget()
    back_button.pack_forget()
    title_label.pack_forget()
    desc_label.pack_forget()
    req_label.pack_forget()
    
    # Create a new label that says "Installing..." in the top center of the window
    installing_label = tk.Label(root, text="Installing...", bg='#212121', fg='#FFFFFF', font=('Helvetica', 12))
    installing_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    
    r = requests.get(mfile)
    if not os.path.exists("/usr/local/bin/MultiMod/Temp/Scripts/Install.py"):
        os.makedirs("/usr/local/bin/MultiMod/Temp/")
        os.mkdir("/usr/local/bin/MultiMod/Temp/Scripts/")
    with open("/usr/local/bin/MultiMod/Temp/Scripts/Install.py", "w") as f:
        f.write(r.text)
    
    installing_label.pack_forget()
    
    # Create a new label that says "Installed!" in the top center of the window
    installed_label = tk.Label(root, text="Installed!", bg='#212121', fg='#FFFFFF', font=('Helvetica', 12))
    installed_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    
    os.system("python3 /usr/local/bin/MultiMod/Temp/Scripts/Install.py")
    
    sys.exit()

def MC_Mod(button, title_box, mods_label, line, title, desc, req, mfile):
    button.pack_forget()
    title_box.pack_forget()
    mods_label.pack_forget()
    
    # Create a new button that says "Install" in the bottom right corner of the window
    install_button = tk.Button(root, text="Install", bg='#212121', fg='#000000', font=('Helvetica', 12))
    install_button.bind('<Button-1>', lambda event: install(mfile, install_button, back_button, title_label, desc_label, req_label))
    install_button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
    
    # Create a new button that says "Back" in the bottom left corner of the window
    back_button = tk.Button(root, text="Exit", bg='#212121', fg='#000000', font=('Helvetica', 12))
    back_button.bind('<Button-1>', lambda event: sys.exit())
    back_button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
    
    # Create a new label that says "Title" in the top left corner of the window
    title_label = tk.Label(root, text="Mod Name: "+title, bg='#212121', fg='#FFFFFF', font=('Helvetica', 12))
    title_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    
    # Create a new label that says "Description" in the top left corner of the window
    desc_label = tk.Label(root, text="Mod Description: "+desc, bg='#212121', fg='#FFFFFF', font=('Helvetica', 12))
    desc_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    
    # Create a new label that says "Requirements" in the top left corner of the window
    req_label = tk.Label(root, text="Required Mods/Libraries: "+req, bg='#212121', fg='#FFFFFF', font=('Helvetica', 12))
    req_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

def search(value):
    search_icon_label.pack_forget()
    # Make a box for the search bar and let the user enter text
    search_bar = tk.Entry(root, width=50, bg='#212121', fg='#FFFFFF', font=('Helvetica', 12))
    search_bar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    # When the user presses enter, search for the text they entered
    search_bar.bind('<Return>', lambda event: search_for(search_bar.get()))

def Minecraft_Menu(item, ):
    item.pack_forget()
    # Add a box at the top center of the window to display the title of the game
    title_box = tk.Label(root, text="Minecraft", bg='#212121', fg='#FFFFFF', font=('Helvetica', 20))
    title_box.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
    
    mods_label = tk.Label(root, text="Mods", bg='#212121', fg='#FFFFFF', font=('Helvetica', 20))
    mods_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=20)
    
    # Get the list of mods from https://raw.githubusercontent.com/ThatError404/MultiMod/main/ServerFiles/Games/Minecraft/Mods/Mods.mm
    r = requests.get("https://raw.githubusercontent.com/ThatError404/MultiMod/main/ServerFiles/Games/Minecraft/Mods/Mods.mm")
    # See how many lines are in the file
    lines = r.text.splitlines()
    # Create a list of the mods
    mods = []
    for line in lines:
        mods.append(line)
        # See how many mods are in the list
        mod_count = len(mods)
    # For each line, split the line into a list of contents
    for line in lines:
        title = line.split("%" + "TITLE:")[1]
        title = title.split("%")[0]
        
        desc = line.split("%" + "DESC:")[1]
        desc = desc.split("%")[0]
        
        req = line.split("%" + "REQ:")[1]
        req = req.split("%")[0]
        
        mfile = line.split("%" + "FILE:")[1]
        mfile = mfile.split("%")[0]
        
        # Create a button for each line
        button = tk.Button(root, text=title, bg='#212121', fg='#000000', font=('Helvetica', 12))
        button.bind('<Button-1>', lambda event: MC_Mod(button, title_box, mods_label, line, title, desc, req, mfile))
        button.pack(side=tk.TOP, fill=tk.X, padx=3, pady=3)

def search_for(text):
    
    # Check if text is close to the list of games (list)
    if text in list:
        if text == "Minecraft" or text == "minecraft":
            # Make a box below the search bar to the very left of the window and display the game icon
            Icon = tk.PhotoImage(file=Minecraft)
            minecraft_box = tk.Label(root, image=Icon, bg='#212121')
            # Always keep the position of the icon the same
            minecraft_box.image = Icon
            minecraft_box.bind('<Button-1>', lambda event: Minecraft_Menu(minecraft_box))
            minecraft_box.pack(side=tk.LEFT, padx=0, pady=0)

search_icon = tk.PhotoImage(file="/usr/local/bin/MultiMod/LocalFiles/search.png")
# Show the image on the window and put it in the top right corner and make the background color the same as the window and resize it
search_icon_label = tk.Label(root, image=search_icon, bg='#212121')
search_icon_label.image = search_icon
search_icon_label.configure(background='#212121')
search_icon_label.configure(foreground='#FFFFFF')
search_icon_label.configure(font=('Helvetica', 12))
search_icon_label.pack(side=tk.RIGHT, anchor=tk.NE)
search_icon_label.bind("<Button-1>", search)
os.system("clear")
root.mainloop()
