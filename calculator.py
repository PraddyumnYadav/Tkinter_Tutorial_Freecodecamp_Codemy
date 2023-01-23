# Importing Essentials
from tkinter import *

# Create Root Widget
root = Tk()

# Set Title of Our Calculator
root.title("Simple Calculator")

# Create Our Entry Widget
e = Entry(root, width=33, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define Functions for Our Number Buttons
def button_click(char):
    current = str(e.get())
    e.delete(0, END)
    e.insert(0, current + str(char))


def button_clear():
    e.delete(0, END)


def button_equal():
    current = str(e.get())
    e.delete(0, END)
    e.insert(0, eval(current))


# Create Our Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
add_btn = Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+"))
sub_btn = Button(root, text="-", padx=40, pady=20, command=lambda: button_click("-"))
mult_btn = Button(root, text="X", padx=40, pady=20, command=lambda: button_click("*"))
div_btn = Button(root, text="/", padx=40, pady=20, command=lambda: button_click("/"))
clear_screen = Button(root, text="Clear", padx=80, pady=20, command=button_clear)
equal_btn = Button(root, text="=", padx=93, pady=20, command=button_equal)

# Display all the Buttons on Our Screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
sub_btn.grid(row=4, column=1)
mult_btn.grid(row=4, column=2)

add_btn.grid(row=5, column=0)
clear_screen.grid(row=5, column=1, columnspan=2)

div_btn.grid(row=6, column=0)
equal_btn.grid(row=6, column=1, columnspan=2)

# Run The Tkinter MainLoop
root.mainloop()
