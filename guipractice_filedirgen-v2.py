import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog

# create_dir = this creates the new folder dir from user input
# create widget


def CreateWidgets():
    template_Label = Label(master, text='Select template: ')
    template_Label.grid(row=4, column=0, pady=5, padx=5)

    # template file source display
    master.sourceText = Entry(master, width=50, textvariable=sourceLocation)
    master.sourceText.grid(row=4, column=1, columnspan=2)

    # template browse button
    source_browseButton = Button(
        master, text="Browse", command=SourceBrowse, width=15)
    source_browseButton.grid(row=4, column=3, pady=5, padx=5)


def SourceBrowse():
    # opens file-dailog directory
    # prompts user to select file to copy
    # filedialog.askopenfilenames() method.
    # Initial directory set to server path where templates are housed
    # converts it to list using list()
    master.files_list = list(filedialog.askopenfilenames(
        initialdir=r"C:\Users\bruta\Desktop\ai_files"))

    # displays selected file(s) in the master.sourceText
    master.sourceText.insert('1', master.files_list)


def create_dir():
    directory = e1.get() + "_" + e2.get() + "_" + e3.get()
    parent_dir = r"C:\Users\bruta\Desktop"
    newFolder = path = os.path.join(parent_dir, directory)
    os.mkdir(newFolder)
    os.chdir(newFolder)
    for dir in ['Art', 'Production', 'Proof']:
        os.mkdir(dir)
    print("Directory '%s' created" % directory)
    files_list = master.files_list
    for f in files_list:
        shutil.copy(f, newFolder)
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    sourceLocation.delete(0, tk.END)


# parent window
master = tk.Tk()
master.title('Go Fetch Beta')
master.geometry('600x200')
# input box
tk.Label(master, text='Enter Job Name: ').grid(row=0)
tk.Label(master, text='Enter Job Product: ').grid(row=1)
tk.Label(master, text='Enter Job Number: ').grid(row=2)
# user input return values
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

# file entry field
sourceLocation = StringVar()

# widget
CreateWidgets()

# create button with def function assigned to it
tk.Button(master, text='Create', command=create_dir).grid(
    row=5, column=1, sticky=tk.W, pady=2)

master.mainloop()
