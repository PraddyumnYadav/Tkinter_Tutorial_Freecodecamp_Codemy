# Importing Essentials
from tkinter import *

# Create Root Widget
root = Tk()

# Set Default Size of Our GUI Window
root.geometry("500x600")

# Set Minimun size of Our GUI Window
root.minsize(150, 100)

# Define a Function for Our Button
def clickAction():
    myLabel = Label(
        root, text=f"Look! This Button is Clicked By {e.get()}.", fg="white", bg="red"
    )
    mySpaceLabel = Label(root, text="  ")

    # Pack Labels on the screen
    myLabel.pack()
    mySpaceLabel.pack()


# Create Entry(Input) Widget
e = Entry(root, width=25)
mySpaceLabel = Label(root, text="  ")

# Pack Our Widgets
mySpaceLabel.pack()
e.pack()

# Add Spacing
mySpaceLabel = Label(root, text="  ")
mySpaceLabel.pack()

# Create Our Buttons
myButton = Button(
    root, text="Enter Your Name", command=clickAction, fg="white", bg="blue"
)
mySpaceLabel = Label(root, text="  ")

# Grid(Show it on Screen) Our Buttons
myButton.pack()
mySpaceLabel.pack()

# Run The Tkinter MainLoop
root.mainloop()
