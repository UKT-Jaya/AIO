import DataHandler
import UI
import os

def main():
    DataHandler.check()

    data = DataHandler.readJSON("./data/Data.json")
    menuNames = []
    for i in data["data"]:
        if(os.path.exists("./data/" + i["title"])):
            menuNames.append("(" + i["type"].capitalize() + ") \33[92m" + i["title"] + "\33[0m")
        else:
            menuNames.append("(" + i["type"].capitalize() + ") \33[91m" + i["title"] + "\33[0m")
    menuNames.append("Exit")
    UI.menu("", menuNames)
    inputRes = input("Choose Menu: ")
    try:
        inputRes = int(inputRes)
    except:
        print("Input must be an Integer")
        return
        
    if(inputRes == len(menuNames)):
        os.system("cls")
        exit()
    elif(inputRes >= 0 & inputRes < len(menuNames)):
        inputRes -= 1
        cmdExec = "data\\" + data["data"][inputRes]["title"] + "\\" + data["data"][inputRes]["main"]
        if(os.path.exists("data/" + data["data"][inputRes]["title"] + "/")):
            os.system(cmdExec)
        else:
            DataHandler.downloader(data["data"][inputRes]["title"], data["data"][inputRes]["download"]["url"], data["data"][inputRes]["download"]["fileName"])
            os.system(cmdExec)
    else:
        UI.notificator("Menu not found!", 2, 38, 50)
        main()
        return

main()