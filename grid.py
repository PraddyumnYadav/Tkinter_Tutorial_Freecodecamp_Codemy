# Importing Essentials
from tkinter import *

# Create Root Widget
root = Tk()

# Set Default Size of Our GUI Window
root.geometry("300x200")

# Set Minimun size of Our GUI Window
root.minsize(100, 100)

# Create Our Labels
myLabel1 = Label(text="Hello, World!!")
myLabel2 = Label(text="Praddyumn Yadav")

# Grid(Show it on Screen) Our Labels
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# Run The Tkinter MainLoop
root.mainloop()
