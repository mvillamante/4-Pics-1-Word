from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from src.checkFiles import *
from src.gameController import *


def main():
    try:
        usergp()
        game_levels()

        root = Tk()
        root.geometry("530x770")

        ico = ImageTk.PhotoImage(Image.open("assets/iicon.png"))
        root.wm_iconphoto(False, ico)
        
        root.resizable(0, 0)
        app = Controller(root)
        root.mainloop()
    except ModuleNotFoundError:
        messagebox.showerror(title = "Error", message = "The program has unexpectedly crashed. Please contact the developers")


if __name__ == "__main__":
    main()
