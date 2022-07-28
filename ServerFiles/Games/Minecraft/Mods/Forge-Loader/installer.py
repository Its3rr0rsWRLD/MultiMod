import urllib.request
import sys
import os

if not os.path.exists("/usr/local/bin/MultiMod/Temp/Forge"):
    os.makedir("/usr/local/bin/MultiMod/Temp/Forge")

print("Please wait while installing Forge.\n\nThis will launch 1 program. Please install using 'client side', this is selected as default.\n\nThis will install Forge 1.19.1\n")
urllib.request.urlretrieve("https://maven.minecraftforge.net/net/minecraftforge/forge/1.19-41.1.0/forge-1.19-41.1.0-installer.jar", "/usr/local/bin/MultiMod/Temp/Forge/forge-1.19-41.1.0-installer.jar")
os.system("java -jar /usr/local/bin/MultiMod/Temp/Forge/forge-1.19-41.1.0-installer.jar")
