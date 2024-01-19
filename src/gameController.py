import random
import string
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from src.checkFiles import *
from src.validation import *
from src.snd import *


class Controller(Frame):
    """The Controller is the director of the program."""
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.master.title("4 pics 1 word")
        self.main_window()


        
    def main_window(self):
        """This is the method that displays the Starting Page of the Program."""
        global imgs
        
        imgs = ["logo.png", "play.png", "ribbon.png", "coin.png", "levelrib.png",
                "back.png", "iicon.png"]
        
        self.frmmain = Frame(self, width=530, height=770, bg="#152238")

        lvl = ImageTk.PhotoImage(Image.open("assets/" + imgs[2]))
        dlvl = Label(self.frmmain, image=lvl, background="#152238")
        dlvl.image = lvl

        self.curlevel = USERINFO["Level"]
        self.dcurlevel = Label(self.frmmain, text=f"{str(self.curlevel)}",
                               fg="white", bg="#BC1823", font="MSSansSerif 23 bold")
        

        logo = ImageTk.PhotoImage(Image.open("assets/" + imgs[0]))
        dlogo = Label(self.frmmain, image=logo, background="#152238")
        dlogo.image = logo

        iplay = ImageTk.PhotoImage(Image.open("assets/" + imgs[1]))
        play = Button(self.frmmain, image=iplay, background="#152238",
                      borderwidth=0, activebackground="#152238",
                      command=lambda: [dbtn_snd(), self.startgame_components(), self.body_window()] if int(self.curlevel) < 51 else self.endgame())
        play.image = iplay

        if int(self.curlevel) < 10:
            self.dcurlevel.place(x=255, y=115)
        else:
            self.dcurlevel.place(x=250, y=115)

        dlvl.place(x=228, y=95)
        dlogo.place(x=115, y=210)
        play.place(x=160, y=535)
        self.frmmain.pack()

        self.pack()



    def startgame_components(self, *args):
        """This is the method that displays the Header and Game's Image in the Main Game's Page of the Program."""
        try:
            for x in self.frmmain.winfo_children():
                x.destroy()
            self.frmmain.destroy()
        except:
            pass

        self.header = Frame(self, width=530, height=50, bg="#121621")

        coin = ImageTk.PhotoImage(Image.open("assets/" + imgs[3]))
        dcoin = Label(self.header, image=coin, background="#121621")
        dcoin.image = coin

        self.cvalue = USERINFO["Coins"]
        self.dcvalue = Label(self.header, text=f"{str(self.cvalue)}",
                             fg="white", background="#121621", font="MSSansSerif 15 bold")

        level = ImageTk.PhotoImage(Image.open("assets/" + imgs[4]))
        dlevel = Label(self.header, image=level, background="#121621")
        dlevel.image = level

        self.curlevel = USERINFO["Level"]
        self.dcurlevel = Label(self.header, text=f"{str(self.curlevel)}",
                               fg="white", bg="#BC1823", font="MSSansSerif 15 bold")

        back = ImageTk.PhotoImage(Image.open("assets/" + imgs[5]))
        dback = Button(self.header, image=back, background="#121621",
                       borderwidth=0, activebackground="#121621",
                       command=lambda: [dbtn_snd(), self.bridge()])
        dback.image = back

        self.body = Frame(self, width=530, height=770, bg="#152238")
        
        self.gpics = Frame(self.body, width=300, height=250, bg="#152238")

        gimg = Image.open("assets/game/" + str(GAMEINFO[str(self.curlevel)]) + ".png")
        gimg = ImageTk.PhotoImage(gimg.resize((400, 400), Image.LANCZOS))
        dgimg = Label(self.gpics, image=gimg, background="#152238")
        dgimg.image = gimg

        dcoin.place(x=490, y=5)
        if int(self.cvalue) > 999:
            self.dcvalue.place(x=440, y=10)
        else:
            self.dcvalue.place(x=450, y=10)

        if int(self.curlevel) < 10:
            self.dcurlevel.place(x=260, y=12)
        else:
            self.dcurlevel.place(x=255, y=12)
        dlevel.place(x=243, y=2)
        
        dback.place(x=2, y=2)

        self.header.pack()

        dgimg.pack()
        self.gpics.place(x=65, y=20)

        self.body.pack()        



    def body_window(self):
        """This is the method that displays the buttons in the Main Game's Page of the Program."""
        alphabet = string.ascii_lowercase
        self.ans = GAMEINFO[str(USERINFO["Level"])]
        self.n = 0
        self.barr = ["" for _ in range(len(self.ans))]
        self.revlett = ["" for _ in range(len(self.ans))]

        self.arrans = [_ for _ in self.ans.upper()]
        self.ANSARR = [_ for _ in self.ans.upper()]

        self.saverevidx = [] 

        self.mainbody = Frame(self, width=530, height=770, bg="#152238")

        self.bnkletters = Frame(self.mainbody, width=530)
        
        sbox = ImageTk.PhotoImage(Image.open("assets/box.png"))
        c = 0
        for i in range(len(self.ans)):
            xbox = Label(self.bnkletters, image=sbox, bg="#152238", borderwidth=0, 
                          activebackground="#152238")
            xbox.image = sbox
            xbox.grid(row=0, column=c)
            c += 1

        self.calpha = [None for _ in range(len(self.ans))]
        self.cllabel = Frame(self.mainbody)
        r = 10
        for k in range(len(self.calpha)):
            self.calpha[k] = Button(self.bnkletters, text="", fg="white", bg="#121621",
                              font="MSSansSerif 18 bold", borderwidth=0, activebackground="#121621",
                              command=lambda k = k: self.delbut(k))
            self.calpha[k].place(x=r, y=28, anchor="w")
            r += 58

        self.bodylet = Frame(self.mainbody, width=530, height=190, bg="#152238")

        aletters = ' '.join(random.choice(alphabet) for i in range(12 - len(self.ans)))
        self.ranletters = [*self.ans]
        self.ranletters.extend(aletters.split(" "))
        random.shuffle(self.ranletters)

        self.ranlettersC = self.ranletters.copy()
        self.ranlettersCD = []

        self.balpha = [None for _ in range(12)]

        self.tile = ImageTk.PhotoImage(Image.open("assets/tile.png"))
        c = 0
        r = 0
        for i in range(len(self.ranletters)):
            self.balpha[i] = Button(self.bodylet, text=self.ranletters[i].upper(), font="MSSansSerif 25 bold",
                                    bg="#152238", fg="black", height=59, width=67, activebackground="#152238",
                                    borderwidth=0, activeforeground="#152238", image=self.tile, compound=CENTER,
                                    command=lambda i = i: self.addc(i))
            self.balpha[i].image = self.tile
            self.balpha[i].grid(row=r, column=c, padx=0, pady=1)
            c += 1
            if c != 0 and (i + 1) % 6 == 0:
                r += 1
                c = 0
                if r == 1:
                    c = 0
        

        self.ures = ["" for _ in range(len(self.ans))]

        hintbtn = ImageTk.PhotoImage(Image.open("assets/hintbtn.png"))
        dhintbtn = Button(self.bodylet, image=hintbtn, background="#152238",
                          activebackground="#152238", activeforeground="#152238",
                          borderwidth=0, command=self.revletter)
        dhintbtn.image = hintbtn

        skipbtn = ImageTk.PhotoImage(Image.open("assets/skipbtn.png"))
        dskipbtn = Button(self.bodylet, image=skipbtn, background="#152238",
                          activebackground="#152238", activeforeground="#152238",
                          borderwidth=0, command=self.skiplvl)
        dskipbtn.image = skipbtn

        dhintbtn.grid(row=0, column=7)
        dskipbtn.grid(row=1, column=7)

        self.cllabel.place(relx=0.5, y=50, anchor=CENTER)
        self.bnkletters.place(relx=0.5, y=50, anchor=CENTER)
        self.bodylet.place(x=512, anchor="e", y=185)

        self.mainbody.place(y=500)



    def revletter(self):      
        """This is the method that contains the Hint Execution of the Logic."""              
        if int(self.cvalue) < 2:    
            tkinter.messagebox.showwarning("Cannot Reveal a Letter", "Not Enough Coins!\nRevealing a Letter Costs 2 Coins.")
        else:
            isyes = tkinter.messagebox.askyesno("Reveal Letter", "Do you want to spend 2 coins to reveal a letter?")
            if isyes == True:
                self.cvalue = int(self.cvalue) - 2
                self.dcvalue.config(text=f"{self.cvalue}")     

                self.rlet = random.choice(self.arrans)
                

                for i in range(len(self.ranletters)):
                    self.balpha[i].config(text=self.ranletters[i].upper(),
                                          image=self.tile,
                                          state=NORMAL)

                idx = self.ranlettersC.index(self.rlet.lower())
                self.saverevidx.append(int(idx))

                ttile = ImageTk.PhotoImage(Image.open("assets/ttile.png"))
                for i in self.saverevidx:
                    self.balpha[i].config(image=ttile, state=DISABLED, text="")
                    self.balpha[i].image = ttile

                self.midx = self.ANSARR.index(self.rlet)
                self.revlett[self.midx] = self.rlet
                
                for i in range(len(self.ranlettersC)):
                    for j in range(len(self.revlett)):
                        if self.ranlettersC[i].upper() != self.revlett[j].upper():
                            self.balpha[i].config(text=self.ranlettersC[i].upper())

                dbtn = self.ranlettersC.index(self.rlet.lower()) 
                self.ranlettersCD.append(dbtn)
                
                for i in self.ranlettersCD:
                    self.balpha[i].config(text="")

                for i in range(len(self.revlett)):
                    if i != self.midx:
                        self.calpha[i].config(text=self.revlett[i])
                        self.ures[i] = ""
                        self.barr[i] = ""

                self.ures[self.midx] = self.rlet
                self.barr[self.midx] = self.ranlettersC.index(self.rlet.lower())

                self.ures = self.revlett.copy()
                self.barr = self.revlett.copy()
                
                for i in range(len(self.revlett)):
                    if self.revlett[i] != "":
                        self.calpha[i].config(disabledforeground="green yellow", text=self.revlett[i],
                                              state=DISABLED)

                self.arrans.remove(self.rlet)
                self.n = len(self.ans) - self.ures.count("")

                if self.n >= len(self.ans):
                        self.woc, self.cvalue, self.curlevel = UserAnswerValidation.isvalid(self.ures, self.ans, self.calpha,
                                                    self.cvalue, self.curlevel)
                        if self.woc == True:
                            self.after(1500, self.next_level)
                        else:
                            inc_snd()

                dbtn_snd()

      
                        
    def skiplvl(self):
        """This is the method that contains the Skip Execution of the Logic."""     
        if int(self.cvalue) < 10:    
            tkinter.messagebox.showwarning("Cannot Skip a Level", "Not Enough Coins!\nSkipping a Level Costs 10 Coins.")
        else:
            isyes = tkinter.messagebox.askyesno("Reveal Letter", "Do you want to spend 10 coins to skip a level?")
            if isyes == True:
                for i in self.balpha:
                    i.config(state=DISABLED)
                
                for i in range(len(self.calpha)):
                    self.calpha[i].config(text=self.ANSARR[i])

                self.cvalue = int(self.cvalue) - 20
                
                self.ures = self.ANSARR
                self.n = len(self.ans)

                if self.n >= len(self.ans):
                    self.woc, self.cvalue, self.curlevel = UserAnswerValidation.isvalid(self.ures, self.ans, self.calpha,
                                                self.cvalue, self.curlevel)
                    if self.woc == True:
                        self.after(1500, self.next_level)
                    else:
                        inc_snd()



    def addc(self, i):
        """This is the method that adds Letters to the Blank Boxes of the Game."""     
        try:
            dbtn_snd()

            idx = self.barr.index("")
            self.barr[idx] = i

            self.ures[idx] = str(self.balpha[i]["text"])
            self.calpha[idx].config(text=self.balpha[i]["text"])

            ttile = ImageTk.PhotoImage(Image.open("assets/ttile.png"))
            self.balpha[i].config(image=ttile, state=DISABLED, text="")
            self.balpha[i].image = ttile

            self.n += 1

        except:
            pass

        if self.n >= len(self.ans):
                self.woc, self.cvalue, self.curlevel = UserAnswerValidation.isvalid(self.ures, self.ans, self.calpha,
                                             self.cvalue, self.curlevel)
                if self.woc == True:
                    self.after(1500, self.next_level)
                else:
                    inc_snd()



    def delbut(self, k):
        """This is the method that removes Letters to the Blank Boxes of the Game.""" 

        dbtn_snd()

        self.ranletters[self.barr[k]] = ""
        iidx = self.barr[k]

        idx = k
        self.v = self.calpha[k]["text"].lower()
        self.balpha[iidx].config(text=self.v.upper(), state=NORMAL, 
                                 image=self.tile)
        self.balpha[iidx].image = self.tile

        self.barr[idx] = ""
        self.ures[idx] = ""
        self.calpha[idx].config(text=" ")

        self.n -= 1



    def endgame(self, *args):
        """This is the method that displays when the Users completes all levels of the game."""
        try:
            for x in self.frmmain.winfo_children():
                x.destroy()
            self.frmmain.destroy()
        except:
            pass
        
        self.frmfnl = Frame(self, width=530, height=770, bg="#152238")
        
        Label(self.frmfnl, text="Congratulations!",
              bg="#152238", font="MSSansSerif 38 bold",
              fg="white").place(relx=0.12, y=200)
        
        Label(self.frmfnl, text="You Completed the Game.",
              bg="#152238", font="MSSansSerif 23",
              fg="white").place(relx=0.15, y=280)
        
        res = ImageTk.PhotoImage(Image.open("assets/resbtn.png"))
        resbtn = Button(self.frmfnl, image=res, activebackground="#152238",
                        activeforeground="#152238", borderwidth=0,
                        background="#152238", command=lambda: [self.bridge(), self.resgame(), dbtn_snd()])
        resbtn.image = res

        mm = ImageTk.PhotoImage(Image.open("assets/mmbtn.png"))
        mmbtn = Button(self.frmfnl, image=mm, activebackground="#152238",
                        activeforeground="#152238", borderwidth=0,
                        background="#152238", command=lambda: [self.bridge(), dbtn_snd()])
        mmbtn.image = mm


        resbtn.place(relx=0.33, y=370)
        mmbtn.place(relx=0.34, y=440)
        self.frmfnl.pack()



    def resgame(self, *args):
        """This is the method that resets the level and coins of the game."""
        self.curlevel = 1
        self.cvalue = 100
        resusergp()
        tkinter.messagebox.showinfo("4 pics 1 word", "The Game will Restart.\nOpen the app to play again.")
        quit()



    def next_level(self, *args):
        """This is the method that helps transition from one level page to the next."""
        win_snd()

        for x in self.header.winfo_children():
            x.destroy()
        self.header.destroy()

        for x in self.body.winfo_children():
            x.destroy()
        self.body.destroy()

        for x in self.mainbody.winfo_children():
            x.destroy()
        self.mainbody.destroy()

        if int(self.curlevel) == 51:
            self.endgame()
        else:
            self.startgame_components()
            self.body_window()



    def bridge(self, *args):
        """This is the method that helps transition from the main game's page to the starting game's page."""
        try:
            for x in self.frmfnl.winfo_children():
                x.destroy()
            self.frmfnl.destroy()
        except: 
            pass
        
        try:
            for x in self.header.winfo_children():
                x.destroy()
            self.header.destroy()
        except: 
            pass
        
        try:
            for x in self.body.winfo_children():
                x.destroy()
            self.body.destroy()
        except:
            pass

        self.main_window()



