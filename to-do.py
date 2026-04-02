'''
SD-GAL-05 SD-TA-009 Exercise 001
Author: Mary Ronan
Last Modified:
02/04/2026
A To Do Application in Python built using Tkinter
'''

# Required imports
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv

# Variables
filename = "./tasks.csv"

# ---------
# FUNCTIONS
# ---------

# Import tasks
def fReadFile():
        try:
                # Access csv file
                with open(filename) as taskFile:
                        reader = csv.reader(taskFile)
                        data = list(reader)

                        # Populate task list
                        if len(data) > 0:
                                for task in list(range(0, len(data))):
                                        taskList.insert(task, data[task][0])
                                        if data[task][1] == "c":
                                                taskList.itemconfig(task, background="green", foreground="black")
                                        else:
                                                taskList.itemconfig(task, background="gold", foreground="black")
        except:
                messagebox.showerror("File IO Error", "Failed to import tasks")
                window.destroy()

        # Display task counters
        taskCounter()

# Task Counter
def taskCounter():
        complete = 0
        outstanding = 0
        count = taskList.index("end")

        # Count complete vs outstanding tasks
        for task in range(count):
                bground = taskList.itemcget(task, "background")
                if bground == "seagreen":
                        complete += 1
                else:
                        outstanding += 1
        # Display count
        completeLabel.config(text="Tasks Completed: " + str(complete))
        outstandingLabel.config(text="Tasks Outstanding: " + str(outstanding))
        

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
        taskCounter()
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
        taskCounter()
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
                                taskList.itemconfig(task, background="seagreen", foreground="black")
                        else:
                                taskList.itemconfig(task, background="gold", foreground="black")
        taskList.selection_clear(0, "end")
        taskCounter()
        taskEntry.focus()

# Export task
def fSave():

        # Get number of tasks
        count = taskList.index("end")

        # Export tasks to csv file
        try:
                with open("./tasks.csv", "w") as taskFile:
                        for task in range(0, count):
                                bground = taskList.itemcget(task, "background")
                                if bground == "seagreen":
                                        complete = "c"
                                else:
                                      complete = "o"
                                taskFile.write(f"{taskList.get(task)},{complete}\n")
                        messagebox.showinfo("Save Tasks", "Taks have been succesfully saved")
        except:
                messagebox.showerror("File IO Error", "File " + filename + " failed to load.")
                                

# Exit application
def fExit():
        answer = messagebox.askquestion("Exit Application", "Are you sure you want to exit this application?")
        if answer == 'yes':
                fSave()
                window.destroy()

# ---
# GUI
# ---

# Initialise tk window
window = tk.Tk()

# Set window properties
window.title("To-Do List")
window.geometry('640x660+50+50') 
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
                   font = "Tahoma 12",
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
                 text="Tasks Completed: ",
                      font = "Tahoma 12 bold",
                      fg = "seagreen",
                      bg = "DarkSlateBlue",
                      anchor = "w",
                      pady = 5)
completeLabel.pack(fill = "x")

# Define outstanding label widget
outstandingLabel = Label(overviewFrame,
                 text="Tasks Outstanding: ",
                      font = "Tahoma 12 bold",
                      fg = "gold",                        
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
                   command = fDel).place(x = 25, y = 620)

btnComplete = Button(window,
                     text = "Set Task Complete/Incomplete",
                     padx = 10,
                     command = fComplete).place(x = 125, y = 620)

btnSave= Button(window,
                text = "Save Tasks",
                padx = 10,
                command = fSave).place(x = 330, y = 620)

btnExit = Button(window,
                 text = "Exit",
                 padx = 10,
                 command = fExit).place(x = 570, y = 620)

# Display application window
fReadFile()
window.mainloop()
