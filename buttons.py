# Importing Essentials
from tkinter import *

# Create Root Widget
root = Tk()

# Set Default Size of Our GUI Window
root.geometry("300x600")

# Set Minimun size of Our GUI Window
root.minsize(150, 100)

# Define a Function for Our Button
def clickAction():
    myLabel = Label(root, text='Look! The Button is Clicked!!', fg="white", bg="red")
    myLabel.pack()

# Create Our Buttons
myButton = Button(root, text='Click Me!', padx=50, pady=25, command=clickAction, fg="white", bg="blue")

# Grid(Show it on Screen) Our Buttons
myButton.pack()

# Run The Tkinter MainLoop
root.mainloop()
