'''
SD-GAL-05 SD-TA-009 Exercise 001
Author: Mary Ronan
Last Modified:
01/04/2026
A To Do Application in Python built using Tkinter
'''

# Required imports
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# ---------
# FUNCTIONS
# ---------

# Display user guide
def fGuide():
        guideText = """How to use the To Do application.\n
Enter the task and press the Add Task button to add it to the list.\n
When a task has been completed, select the item in the list and mark it as complete by pressing the Complete button.\n
To delete a saved task, select the item in the list and delete it by pressing the Delete button."""
        messagebox.showinfo("To-Do: A User Guide", guideText)

# Exit application
def fExit():
	answer = messagebox.askquestion("Exit Application", "Are you sure you want to exit this application?")
	if answer == 'yes':
		window.destroy()

# ---
# GUI
# ---

# Initialise tk window
window = tk.Tk()

# Set window properties
window.title("To-Do List")
window.geometry('640x600+50+50') 
window.config(bg="DarkSlateBlue")
window.resizable(False, False)

# Define title widget
titleFrame = Frame(window)
titleLabel = Label(titleFrame, 
		 text="To-Do List",
                 fg="black",
                 bg="DarkSlateBlue",
		 font = "Garamond 32 bold italic",
                 pady=20,
                 padx=10)
titleLabel.pack(fill="x")

# Define task widget
taskFrame = Frame(window, 
                padx=10,
                highlightbackground="black", 
                highlightthickness=2)

# Task input
nameLabel = Label(taskFrame,
                  text="Enter Task: ",
                  font = "Tahoma 10",
                  pady=10)
nameLabel.grid(row=0, column=0)
taskName = Entry(taskFrame)
taskName.grid(row=0, column=1, sticky="ew")
taskFrame.columnconfigure(1, weight=1)

# Define task header widget
currentFrame = Frame(window,
                      bg="DarkSlateBlue",
                     bd=2)


# Define list frame
taskListFrame = Frame(window,
                      height=330,
                      width=500,
                      bd=2,
                      bg="DarkSlateBlue")

# Define current task header widget
currentLabel = Label(taskListFrame,
                 text="Current Tasks: ",
                      font = "Tahoma 12 bold",
                      bg="DarkSlateBlue",
                      anchor="w",
                      pady=10)
currentLabel.pack(fill="x")

# Define task listbox widget
taskList = Listbox(taskListFrame,
                   font="Tahoma 10",
                   bg="grey",
                   #height=15,
                   width=300,
                   cursor="hand2", bd=2)
taskListFrame.pack_propagate(False)
taskList.pack(side=LEFT, fill=BOTH, padx=2)

#taskList.pack(fill="x")


# Define overview frame 
overviewFrame = Frame(window)

# Define complete label widget
completeLabel = Label(overviewFrame,
                 text="Complete Tasks: ",
                      font = "Tahoma 12 bold",
                      bg="DarkSlateBlue",
                      anchor="w",
                      pady=5)
completeLabel.pack(fill="x")

# Define outstanding label widget
outstandingLabel = Label(overviewFrame,
                 text="Outstanding Tasks: ",
                      font = "Tahoma 12 bold",
                      bg="DarkSlateBlue",
                      anchor="w",
                      pady=5)
outstandingLabel.pack(fill="x")

# Add frames to window
titleFrame.pack()
taskFrame.pack(fill="x", padx=20)
taskListFrame.pack(fill="x", padx=20)
overviewFrame.pack(fill="x", padx=20, pady=10)

# Buttons - static placement
btnGuide = Button(window, text="User Guide", padx=10, command=fGuide).place(x=22, y=55)
btnAdd = Button(window, text="Add Task" , padx=10).place(x=540, y=145)
btnDelete = Button(window, text="Delete Task", padx=10).place(x=25, y=560)
btnComplete = Button(window, text="Complete Task", padx=10).place(x=125, y=560)
btnOutstanding = Button(window, text="Outstanding Tasks", padx=10).place(x=245, y=560)
btnExit = Button(window, text="Exit", padx=10, command=fExit).place(x=570, y=560)

# Display application window
window.mainloop()
