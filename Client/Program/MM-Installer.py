import urllib.request
import urllib
import time
import sys
import os

print("Installing MultiMod...\n")
# Create a folder for MultiMod in /usr/local/bin
if not os.path.exists("/usr/local/bin/MultiMod"):
    os.makedirs("/usr/local/bin/MultiMod")
if not os.path.exists("/usr/local/bin/MultiMod/LocalFiles"):
    os.makedirs("/usr/local/bin/MultiMod/LocalFiles")
if os.path.exists("/usr/local/bin/MultiMod/icon.png"):
    print("MultiMod icon already exists. Deleting...\n")
    os.remove("/usr/local/bin/MultiMod/icon.png")
    print("MultiMod icon deleted.\n")
print("Downloading icon...\n")
# Download icon from https://github.com/ThatError404/MultiMod/blob/main/ServerFiles/icon/MultiMod.png?raw=true
urllib.request.urlretrieve("https://github.com/ThatError404/MultiMod/blob/main/ServerFiles/Icon/MM-256x.png?raw=true", "/usr/local/bin/MultiMod/icon.png")
print("Icon downloaded.\n")

if not os.path.exists("/usr/local/bin/MultiMod/LocalFiles/search.png"):
    print("Downloading search icon...\n")
if os.path.exists("/usr/local/bin/MultiMod/LocalFiles/search.png"):
    print("Search icon already exists. Deleting...\n")
    os.remove("/usr/local/bin/MultiMod/LocalFiles/search.png")
    print("Search icon deleted.\n")
# Download icon from https://github.com/ThatError404/MultiMod/blob/main/ServerFiles/Icon/search.png?raw=true
urllib.request.urlretrieve("https://github.com/ThatError404/MultiMod/blob/main/ServerFiles/Icon/search.png?raw=true", "/usr/local/bin/MultiMod/LocalFiles/search.png")
print("Search icon downloaded.\n")

print("I'm too lazy to make a new print function for every file. Installing neccecary files.\n")

if not os.path.exists("/usr/local/bin/MultiMod/LocalFiles/Minecraft"):
    os.makedirs("/usr/local/bin/MultiMod/LocalFiles/Minecraft")
urllib.request.urlretrieve("https://github.com/ThatError404/MultiMod/blob/main/ServerFiles/Icon/MC-256x.png?raw=true", "/usr/local/bin/MultiMod/LocalFiles/Minecraft/Icon.png")


# Download icon from https://github.com/ThatError404/MultiMod/blob/main/ServerFiles/Icon/search.png?raw=true
urllib.request.urlretrieve("https://github.com/ThatError404/MultiMod/blob/main/ServerFiles/Icon/search.png?raw=true", "/usr/local/bin/MultiMod/LocalFiles/search.png")
print("Search icon downloaded.\n")

#print("Downloading launcher...\n")

print("MultiMod installed!")
time.sleep(2)
os.system("clear")
