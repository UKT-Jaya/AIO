import DataHandler
import UI
import dataTemp

import shutil
import os

def main():
    if(dataTemp.isChecked == False):
        DataHandler.check()
        dataTemp.isChecked = True

    data = DataHandler.readJSON("./data/Data.json")
    menuNames = []
    for i in data["data"]:
        if(os.path.exists("./data/" + i["title"])):
            menuNames.append("(" + i["type"].capitalize() + ") " + i["title"])
        else:
            menuNames.append("(" + i["type"].capitalize() + ") \33[91m" + i["title"] + "\33[0m")
    menuNames.append("Settings")
    menuNames.append("Exit")
    UI.menu("", menuNames)
    inputRes = input("Choose Menu: ")
    try:
        inputRes = int(inputRes)
    except:
        UI.notificator("Input must be an integer!", 2, 38, 50)
        main()
        return
        
    if(inputRes >= 1 and inputRes <= len(menuNames) - 2):
        print(str(inputRes))
        print(str(len(menuNames)))
        inputRes -= 1
        cmdExec = "data\\" + data["data"][inputRes]["title"] + "\\" + data["data"][inputRes]["main"]
        if(os.path.exists("data/" + data["data"][inputRes]["title"] + "/")):
            os.system(cmdExec)
            main()
        else:
            DataHandler.downloader(data["data"][inputRes]["title"], data["data"][inputRes]["download"]["url"], data["data"][inputRes]["download"]["fileName"])
            os.system(cmdExec)
            main()
    elif(inputRes == (len(menuNames) - 1)):
        settings()
    elif(inputRes == len(menuNames)):
        os.system("cls")
        exit()
    else:
        UI.notificator("Menu not found!", 2, 38, 50)
        main()
        return

def settings():
    UI.menu("", ["Repair", "Back"])
    inputRes = input("Choose Menu: ")
    if(inputRes == "1"):
        shutil.rmtree("./data/")
        DataHandler.check()
        main()
    elif(inputRes == "2"):
        main()
    else:
        UI.notificator("Menu not found!", 2, 38, 50)
        settings()
        return

main()