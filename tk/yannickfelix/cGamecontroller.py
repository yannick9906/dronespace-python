"""
@license
This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International
License. To view a copy of this license, visit 
http://creativecommons.org/licenses/by-nc-sa/4.0/.

@author Yannick Félix
"""
from random import randint

from tk.yannickfelix.tkwrapper import *
from tk.yannickfelix.dronespace import *
from tkinter import *
from tkinter import messagebox


class Gamecontroller(object):
    textoutput = None
    textinput = None
    userinput = None
    wins = []

    def __init__(self, textoutput, textinput, userinput):
        """

        @param textoutput: GTextOutput
        @param textinput: GTextInput
        @param userinput: GUserInput
        """
        self.textinput = textinput
        self.textoutput = textoutput
        self.userinput = userinput

    def update(self):
        cmd = self.textinput.getUserText()
        self.textoutput.printMessage(cmd, "right", "")
        if cmd == " ":
            self.textoutput.printMessage("Hey, hör auf damit!", "left", "Kitteh")
        elif cmd == " ":
            self.textoutput.printMessage("Naa toll, jetzt hast du's kaputt gemacht", "left", "Kitteh")
        elif cmd == "Hover kitteh":
            self.textoutput.printMessage("Looking for purmision to land", "left", "Hover Kitteh")
        elif cmd == "map()":
            self.textoutput.printMessage("Dis FODMAP is stoopid. I sees no noms at all.", "left", "Space Kitteh")
        elif cmd == "attack()":
            self.textoutput.printMessage("disapproves ur submishinz", "left", "Moderator Kitteh")
        elif cmd == "zombieh kittehs":
            self.textoutput.printMessage("Zombieh Kittehs coming to cuddle you to death", "left", "")
        elif cmd == "destroy.now()":
            self.textoutput.printMessage("Mhh, naja wenn du willst...", "center")
            for i in range(50):
                self.openWindow()

    def openWindow(self,arg=None):
        if len(self.wins) > 20:
            self.wins[randint(1, len(self.wins))].destroy()
        t = Toplevel()
        t.title("Error")
        self.wins.append(t)
        f = Frame(master=t)
        f.place(x=0, y=0, width=200, height=200)
        btn = Button(master=f, text="Error", command=self.openWindow)
        t.bind("<Return>", self.openWindow)
        btn.place(x=50, y=150, width=100, height=20)