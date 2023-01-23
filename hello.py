# Importing Essentials
from tkinter import *

# Create Root Widget
root = Tk()

# Set Default Size of Our GUI Window
root.geometry("200x200")

# Set Minimun size of Our GUI Window
root.minsize(150, 100)

# Create Our  Labels
myLabel1 = Label(text="Hello, World!!")
myLabel2 = Label(text="Praddyumn Yadav")

# Pack(Show it on Screen) Our Labels
myLabel1.pack()
myLabel2.pack()

# Run The Tkinter MainLoop
root.mainloop()
