from tkinter import *

master = Tk()

def callback():
    print("click!")

b = Button(master, text="OK", command=callback)
b.pack()
b.place(bordermode = OUTSIDE, height = 100, width = 100, x = 50, y = 50)

mainloop()