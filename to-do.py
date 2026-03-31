''' SD-GAL-05 SD-TA-009 Exercise 001 Author: Mary Ronan Last Modified:
30/03/2026 A To Do Application in Python built using Tkinter '''

# Required imports
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# FUNCTIONS

# Exit func
def fExit():
	answer = messagebox.askquestion("Exit Application", "Are you sure you want to exit this application?")
	if answer == 'yes':
		window.destroy()

# GUI

# Initialise tk window
window = tk.Tk()

# Set window properties
window.title("My To-Do List")
window.geometry('800x550+50+50') 
window.config(bg="DarkSlateBlue")

# Define title widget
titleFrame = Frame(window)
titleLabel = Label(titleFrame, 
		 text="My To-Do List",
                 fg="black",
                 bg="DarkSlateBlue",
		 font = "Garamond 32 bold italic",
                 pady=20,
                 padx=10)
titleLabel.pack(fill="x", expand = True)

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
                      pady=20,
                      padx=10)
taskListLabel.pack(fill="x", expand = True)

# Define list widget
overviewFrame = Frame(window)
completeLabel = Label(overviewFrame,
                 text="Complete Tasks: ",
                      font = "Tahoma 12 bold",
                      bg="DarkSlateBlue",
                      anchor="w",
                      pady=20,
                      padx=10)
completeLabel.pack(fill="x", expand = True)

outstandingLabel = Label(overviewFrame,
                 text="Outstanding Tasks: ",
                      font = "Tahoma 12 bold",
                      bg="DarkSlateBlue",
                      anchor="w",
                      pady=20,
                      padx=10)
outstandingLabel.pack(fill="x", expand = True)

# Place frames on screen
titleFrame.pack()
taskFrame.pack(fill="x", expand = True, padx=20)
taskListFrame.pack(fill="x", expand = True, padx=20)
overviewFrame.pack(fill="x", expand = True, padx=20)

# Add button
btnAdd = Button(window, text="Add").place(x=100, y = 500)

# Exit button
btnExit = Button(window, text="Exit", command=fExit).place(x=500, y = 500)


# display window
window.mainloop()


