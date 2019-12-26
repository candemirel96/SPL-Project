import random
import itertools
from collections import Counter
from tkinter import *
from PIL import ImageTk, Image
import threading
import queue
import time

import deck
import GameSetup
import GameView

def SnapGame():
    root = Tk()

    frame = Frame(root, bg="green", width=1024, height=768)
    frame.pack()

    cc_1 = Label(frame, bg="green")
    cc_1.place(relwidth=(.50 / 3), relheight=1)
    card_d1 = ImageTk.PhotoImage(
        Image.open("cards\default0.png").resize((55, 85), Image.ANTIALIAS))
    cc_1.image = card_d1
    cc_1.configure(image=card_d1)

    cc_2 = Label(frame, bg="green")
    cc_2.place(relx=(.55 / 3) * 2, relwidth=(.70 / 3), relheight=1.6)
    card_d2 = ImageTk.PhotoImage(
        Image.open("cards\default1.png").resize((55, 85), Image.ANTIALIAS))
    cc_2.image = card_d2
    cc_2.configure(image=card_d2)

    cc_3 = Label(frame, bg="green")
    cc_3.place(relx=(.55 / 3) * 2, relwidth=(.70 / 3), relheight=0.4)
    card_d3 = ImageTk.PhotoImage(
        Image.open("cards\default1.png").resize((55, 85), Image.ANTIALIAS))
    cc_3.image = card_d3
    cc_3.configure(image=card_d3)

    cc_4 = Label(frame, bg="green")
    cc_4.place(relx=(.60 / 3) * 4, relwidth=0.25, relheight=1)
    card_d4 = ImageTk.PhotoImage(
        Image.open("cards\default1.png").resize((55, 85), Image.ANTIALIAS))
    cc_4.image = card_d4
    cc_4.configure(image=card_d4)

    root.mainloop()




