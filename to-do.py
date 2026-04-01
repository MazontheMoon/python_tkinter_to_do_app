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

# Add task
def fAdd(event = None):

        # Get task input
        newTask = taskEntry.get()
        taskEntry.delete(0, END)

        # Check for valid task
        if newTask != "":
                taskList.insert(END, newTask)
                taskList.itemconfig("end", background="gold", foreground="black")
        else:
                messagebox.showerror("Error", "Enter a Task")
        taskEntry.focus()

# Delete task
def fDel():

        # Get selected item(s)
        deleteTasks = taskList.curselection()

        # Delete task(s)
        if len(deleteTasks) != 0:
                confirmDel = messagebox.askquestion("Delete Task", "Are you sure you want to delete the task(s)?")
                if confirmDel == 'yes':
                        for task in deleteTasks[::-1]:
                                taskList.delete(task)
        else:
                messagebox.showerror("Error", "No Tasks Selected.")
        taskEntry.focus()

# Complete task
def fComplete():
        # Get selected item(s)
        completeTasks = taskList.curselection()

        # Complete task(s)
        if len(completeTasks) == 0:
                messagebox.showerror("Error", "No Tasks Selected.")
        else:
                for task in completeTasks[::-1]:
                        bgColor = taskList.itemcget(task, "background")
                        if bgColor == "gold":
                                taskList.itemconfig(task, background="green", foreground="black")
                        else:
                                taskList.itemconfig(task, background="gold", foreground="black")
        taskList.selection_clear(0, "end")
        taskEntry.focus()

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
window.config(bg = "DarkSlateBlue")
window.resizable(False, False)

# Define title frame and label
titleFrame = Frame(window)
titleLabel = Label(titleFrame, 
		 text = "To-Do List",
                 fg = "black",
                 bg = "DarkSlateBlue",
		 font = "Garamond 32 bold italic",
                 pady = 20,
                 padx = 10)
titleLabel.pack(fill = "x")

# Define task frame
taskFrame = Frame(window, 
                padx = 10,
                highlightbackground = "black", 
                highlightthickness = 2)

# Define task input widget
nameLabel = Label(taskFrame,
                  text = "Enter Task: ",
                  font = "Tahoma 10",
                  pady = 10)
nameLabel.grid(row = 0, column = 0)
taskEntry = Entry(taskFrame)
taskEntry.grid(row = 0, column = 1, sticky = "ew")
taskEntry.focus()
taskEntry.bind("<Return>", fAdd)
taskFrame.columnconfigure(1, weight = 1)

# Define task header widget
currentFrame = Frame(window)
currentLabel = Label(currentFrame,
                     text = "Current Tasks: ",
                     font = "Tahoma 12 bold",
                     bg = "DarkSlateBlue",
                     anchor = "w",
                     pady = 10)
currentLabel.pack(fill="x")

# Define task listbox widget
taskListFrame = Frame(window,
                      bd = 2,
                      bg = "DarkSlateBlue")

taskList = Listbox(taskListFrame,
                   selectmode = "multiple",
                   font = "Tahoma 10",
                   bg = "white",
                   height = 17,
                   width = 81,
                   cursor = "hand2",
                   selectbackground = "indigo",
                   highlightbackground = "black",
                   highlightthickness = 2)
taskList.pack(side=LEFT,
              fill = "both",
              padx = 2,
              pady = 2)

# Add scrollbar to listbox
scrollbar = Scrollbar(taskListFrame)
scrollbar.pack(side=RIGHT,
               fill = "y",
               padx = 2)
taskList.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = taskList.yview)

# Define overview frame 
overviewFrame = Frame(window)

# Define complete label widget
completeLabel = Label(overviewFrame,
                 text="Complete Tasks: ",
                      font = "Tahoma 12 bold",
                      bg = "DarkSlateBlue",
                      anchor = "w",
                      pady = 5)
completeLabel.pack(fill = "x")

# Define outstanding label widget
outstandingLabel = Label(overviewFrame,
                 text="Outstanding Tasks: ",
                      font = "Tahoma 12 bold",
                      bg = "DarkSlateBlue",
                      anchor = "w",
                      pady = 5)
outstandingLabel.pack(fill = "x")

# Add frames to window
titleFrame.pack()
taskFrame.pack(fill = "x", padx = 20)
currentFrame.pack(fill = "x", padx = 20)
taskListFrame.pack(fill = "x", padx = 20)
overviewFrame.pack(fill = "x", padx = 20, pady = 10)

# Buttons - static placement
btnGuide = Button(window,
                  text = "User Guide",
                  padx = 10,
                  command = fGuide).place(x = 22, y = 55)

btnAdd = Button(window,
                text = "Add Task" ,
                padx = 10,
                command = fAdd).place(x=540, y=145)

btnDelete = Button(window,
                   text = "Delete Task",
                   padx = 10,
                   command = fDel).place(x = 25, y = 560)

btnComplete = Button(window,
                     text = "Set Task Complete/Incomplete",
                     padx = 10,
                     command = fComplete).place(x = 125, y = 560)

btnSave= Button(window,
                text = "Save Tasks",
                padx = 10).place(x = 330, y = 560)

btnExit = Button(window,
                 text = "Exit",
                 padx = 10,
                 command = fExit).place(x = 570, y = 560)

# Display application window
window.mainloop()
