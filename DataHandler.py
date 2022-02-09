import UI

import os
import time
import json
import sys
import requests
import zipfile

def check():
    UI.menu("", [])
    if not os.path.exists("./data"):
        os.makedirs("./data")
        os.makedirs("./data/temp")
    
    if(os.path.isfile("./data/Data.json")):
        if(isOnline() == True):
            updater()
            return
        else:
            return
    else:
        print("> Prepare for installation")
        time.sleep(1)
        print("> Please wait...")
        time.sleep(3)
        if(isOnline() == True):
            updater()
            return
        else:
            print("\nConnection Time Out\nYou must connected to internet for installation")
            exit()

def isOnline():
    try:
        requests.get("https://www.google.com", timeout=5000)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

def updater():
    if(os.path.isfile("./data/Data.json")):
        doing = "update"
    else:
        doing = "install"

    link = "https://github.com/UKT-Jaya/AIO/raw/main/data/Data.json"
    fileName = "Data.json"
    pathFile = "./data/" + fileName
    with open(pathFile, "wb") as f:
        if(doing == "install"):
            print("> Installing " + fileName)
        elif(doing == "update"):
            print("> Updating " + fileName)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
    
    if(doing == "install"):
        print("\n> Installation Successfull, opening main menu...")
    elif(doing == "update"):
        print("\n> Update Successfull, opening main menu...")
    time.sleep(3)

def downloader(title, url, fileName):
    UI.menu("", [])
    print("> " + fileName + " not installed")
    time.sleep(1)
    print("> Prepare for downloading file")
    time.sleep(1)
    print("> Please wait...")
    time.sleep(3)
    path = "./data/temp/" + fileName
    with open(path, "wb") as f:
        UI.menu("", [])
        print("> Downloading " + fileName)
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
    print("\n> Download Success!")
    time.sleep(1)
    print("> Installing...")
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall("./data/" + title)
    os.remove(path)
    print("> Installation successfully, opening menu...")
    time.sleep(3)
    return

def writeJSON(path, data):
  with open(path, "w") as writeFile:
    json.dump(data, writeFile, indent = 2)
    return

def readJSON(path):
  if os.path.exists(path) == False:
    return False
  with open(path) as readFile:
    userData = json.load(readFile)
    return userData