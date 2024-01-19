from src.checkFiles import *

class UserAnswerValidation:
    """The UserAnswerValidation is the main logic of the program."""
    @staticmethod
    def isvalid(uans, answer, btns, ucoins, clvl):
        uval = "".join(uans)
        answer = answer.upper()

        if uval == answer:
            ucoins = int(ucoins) + 10
            clvl = int(clvl) + 1

            arr = []
            for i in range(len(uans)):
                arr.append(btns[i])

            for i in range(len(arr)):
                arr[i].after(500, lambda i = i: arr[i].config(fg="green yellow"))
                arr[i].after(100, lambda i = i: arr[i].config(fg="white"))

            USERINFO["Level"] = str(clvl)
            USERINFO["Coins"] = str(ucoins)

            UserAnswerValidation.savegame()

            return True, ucoins, clvl

        else:
            arr = []
            for i in range(len(uans)):
                arr.append(btns[i])

            for i in range(len(arr)):
                arr[i].after(100, lambda i = i: arr[i].config(fg="red"))
                arr[i].after(500, lambda i = i: arr[i].config(fg="white"))

            return False, ucoins, clvl


    @staticmethod
    def savegame():
        with open(USERPLAY_FILE, "w") as file:
            file.write(f"Level:{USERINFO['Level']}\n")
            file.write(f"Coins:{USERINFO['Coins']}")
