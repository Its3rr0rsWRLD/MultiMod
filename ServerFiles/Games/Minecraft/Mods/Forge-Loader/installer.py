import urllib.request
import requests
import sys
import os

print("Please wait while installing Forge.\n\nThis will launch 1 program. Please install using 'client side', this is selected as default.\n\nThis will install Forge 1.19.1")
urllib.request.urlretrieve("https://maven.minecraftforge.net/net/minecraftforge/forge/1.19-41.1.0/forge-1.19-41.1.0-installer.jar", "/usr/local/bin/MultiMod/Temp/Forge/forge-1.19-41.1.0-installer.jar")
os.system("java -jar /usr/local/bin/MultiMod/Temp/Forge/forge-1.19-41.1.0-installer.jar")
