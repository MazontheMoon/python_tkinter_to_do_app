''' SD-GAL-05 SD-TA-009 Exercise 001 Author: Mary Ronan Last Modified:
30/03/2026 A To Do Application in Python built using Tkinter '''

# Required imports
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# ---------
# FUNCTIONS
# ---------

# Display user guide
def fGuide():
	messagebox.showinfo("To-Do: A User Guide", "Enter your task and press the Add button to Add it to the list. Select an item in the list to mark it as complete by pressing the Complete button, or delete the task by pressing the Delete button.""")

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
window.title("My To-Do List")
window.geometry('640x600+50+50') 
window.config(bg="DarkSlateBlue")
window.resizable(False, False)

# Define title widget
titleFrame = Frame(window)
titleLabel = Label(titleFrame, 
		 text="My To-Do List",
                 fg="black",
                 bg="DarkSlateBlue",
		 font = "Garamond 32 bold italic",
                 pady=10,
                 padx=10)
titleLabel.pack(fill="x")


# Define task widget
taskFrame = Frame(window, 
                padx=10,
                highlightbackground="black", 
                highlightthickness=3)

# Task input
nameLabel = Label(taskFrame,
                  text="Enter Task: ",
                  font = "Tahoma 12",
                  pady=10)
nameLabel.grid(row=0, column=0)
taskName = Entry(taskFrame)
taskName.grid(row=0, column=1, sticky="ew")
taskFrame.columnconfigure(1, weight=1)

# Define list widget
taskListFrame = Frame(window)
taskListLabel = Label(taskListFrame,
                 text="Current Tasks: ",
                      font = "Tahoma 12 bold",
                      bg="DarkSlateBlue",
                      anchor="w",
                      pady=10,
                      padx=10)
taskListLabel.pack(fill="x")


# Define list widget
overviewFrame = Frame(window)
completeLabel = Label(overviewFrame,
                 text="Complete Tasks: ",
                      font = "Tahoma 12 bold",
                      bg="DarkSlateBlue",
                      anchor="w",
                      pady=10,
                      padx=10)
completeLabel.pack(fill="x", expand = True)


outstandingLabel = Label(overviewFrame,
                 text="Outstanding Tasks: ",
                      font = "Tahoma 12 bold",
                      bg="DarkSlateBlue",
                      anchor="w",
                      pady=10,
                      padx=10)
outstandingLabel.pack(fill="x", expand = True)


# Place frames on screen

titleFrame.pack()
taskFrame.pack(fill="x", expand = True, padx=20)
taskListFrame.pack(fill="x", expand = True, padx=20)
overviewFrame.pack(fill="x", expand = True, padx=20)


# User guide button
btnGuide = Button(window, text="User Guide", padx=10, command=fGuide).place(x=25, y=70)

# Add button
btnAdd = Button(window, text="Add Task" , padx=10).place(x=540, y=180)

# Delete button
btnDelete = Button(window, text="Delete Task", padx=10).place(x=25, y=560)

# Complete button
btnComplete = Button(window, text="Complete Task", padx=10).place(x=125, y=560)

# Outstanding button
btnOutstanding = Button(window, text="Outstanding Tasks", padx=10).place(x=245, y=560)

# Exit button
btnExit = Button(window, text="Exit", padx=10, command=fExit).place(x=570, y=560)

# display window
window.mainloop()
