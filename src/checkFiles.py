import os

USERPLAY_FILE = os.getcwd() + "\\data\\userplay.txt"
PICLIST_FILE = os.getcwd() + "\\data\\picList.txt"

USERINFO = dict()
GAMEINFO = dict()

def usergp():
    """This is the function that reads the User's Game Data (current coints and level)."""
    if os.path.isfile(USERPLAY_FILE) == True:
        with open(USERPLAY_FILE, "r") as file:
            fileRead = file.read().split()
            for i in fileRead:
                i = i.split(":")
                USERINFO.update({
                    i[0]: i[1]
                })
    else:
        with open(USERPLAY_FILE, "a") as file:
            file.write(f"Level:1\n")
            file.write(f"Coins:100")
            
        with open(USERPLAY_FILE, "r") as file:
            fileRead = file.read().split()
            for i in fileRead:
                i = i.split(":")
                USERINFO.update({
                    i[0]: i[1]
                })
            

def game_levels():
    """This is the function that reads the Game's Information, both levels and answers."""
    with open(PICLIST_FILE, "r") as file:
        fileRead = file.read().split()
        for i in fileRead:
            i = i.split(";")
            GAMEINFO.update({
                str(i[0]): i[1]
            })

def resusergp():
    """This is the function that resets the User's Game Data back to default."""
    with open(USERPLAY_FILE, "w") as file:
            file.write(f"Level:1\n")
            file.write(f"Coins:100")
