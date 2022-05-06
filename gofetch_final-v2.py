import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pathlib import Path
import subprocess
from subprocess import call


#get user name
user = os.getlogin()
if user == "root":
    user = os.getenv("USER")

# create_dir = this creates the new folder dir from user input
# create widget

def CreateWidgets():
    template_Label = Label(master, text='Select template: ')
    template_Label.grid(row=4, column=0, pady=5, padx=5)

    # template file source display
    master.sourceTemplate = Entry(
        master, width=40, textvariable=sourceLocation)
    master.sourceTemplate.grid(row=4, column=2, columnspan=2)

    # template browse button
    source_browseButton = Button(
        master, text="Browse", command=SourceBrowse, width=15)
    source_browseButton.grid(row=4, column=1, pady=5, padx=5)

    # art browser------------
    template_Label = Label(master, text='Select artwork: ')
    template_Label.grid(row=5, column=0, pady=5, padx=5)

    # art file source display
    master.artSource = Entry(
        master, width=40, textvariable=artSourceLocation)
    master.artSource.grid(row=5, column=2, columnspan=2)

    # template browse button
    source_browseButton = Button(
        master, text="Browse", command=ArtSourceBrowse, width=15)
    source_browseButton.grid(row=5, column=1, pady=5, padx=5)


def SourceBrowse():
    # opens file-dialog directory
    # prompts user to select file to copy
    # filedialog.askopenfilenames() method.
    # Initial directory set to server path where templates are housed
    # converts it to list using list()
    master.files_list = list(filedialog.askopenfilenames(
        initialdir=r"/Volumes/Art Dept/[Templates]/Journals/Pick A Book"))

    # displays selected file(s) in the master.sourceText
    master.sourceTemplate.insert('1', master.files_list)


def ArtSourceBrowse():
    # opens file-dialog directory
    # prompts user to select file to copy
    # filedialog.askopenfilenames() method.
    # Initial directory set to server path where templates are housed
    # converts it to list using list()
    master.artfiles_list = list(filedialog.askopenfilenames(
        initialdir=r"/Volumes/Art Dept/Art Email"))

    # displays selected file(s) in the master.artSourceText
    master.artSource.insert('1', master.artfiles_list)


def create_dir():
    directory = e1.get() + "_" + e2.get() + "_" + e3.get()
    parent_dir = f"//Users//{user}//Desktop//"
    newFolder = path = os.path.join(parent_dir, directory)
    os.mkdir(newFolder)
    os.chdir(newFolder)
    for dir in ['ART', 'PRODUCTION', 'PROOF']:
        os.mkdir(dir)
    print("Directory '%s' created" % directory)
    files_list = master.files_list
    for f in files_list:
        shutil.copy2(f, newFolder)
    files_list = master.artfiles_list
    for f in files_list:
        shutil.move(f, 'Art')
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    master.sourceTemplate.delete(0, END)
    master.artSource.delete(0, END)
    path_abs = ('/Volumes/Art Dept/Art Email')
    walk = list(os.walk(path_abs))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)


def clear_btn():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    master.sourceTemplate.delete(0, END)
    master.artSource.delete(0, END)


# shortcuts
def VirtualShortCut():
    targetDirectory = "/Volumes/Creative Sales"
    call(["open", targetDirectory])

def ArtDeptStorageShortCut():
    targetDirectory = "/Volumes/Art Dept/Art Dept Storage"
    call(["open", targetDirectory])

def OptionsShortCut():
    targetDirectory = "/Volumes/Art Dept/[Templates]/Options"
    call(["open", targetDirectory])

def CDTemplateShortCut():
    targetDirectory = "/Volumes/Art Dept/•••ColorDirect Press Templates"
    call(["open", targetDirectory])

# parent window
master = tk.Tk()
master.title('Go Fetch Hub')
master.geometry('800x200')
icon = path = Path(__file__).absolute().parent.joinpath("tennisball.png")

# input box
tk.Label(master, text='Enter Job Name: ', anchor='w').grid(row=0)
tk.Label(master, text='Enter Job Product: ').grid(row=1)
tk.Label(master, text='Enter Job Number: ').grid(row=2)

#shortcut
tk.Label(master, text='Shortcuts').grid(row=0, column=2, sticky=tk.W)

# user input return values
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

#shortcut buttons
tk.Button(master, text='Virtuals', command=VirtualShortCut, width=10).grid(row=1, column=2, sticky=tk.W, pady=5, padx=5)
tk.Button(master, text='Options', command=OptionsShortCut, width=10).grid(row=1, column=3, sticky=tk.W, pady=5, padx=5)
tk.Button(master, text='Art Storage', command=ArtDeptStorageShortCut, width=10).grid(row=2, sticky=tk.W, column=2, pady=5, padx=5)
tk.Button(master, text='CD Templates', command=CDTemplateShortCut, width=10).grid(row=2, column=3, sticky=tk.W, pady=5, padx=5)

# file entry field
sourceLocation = StringVar()
artSourceLocation = StringVar()

# widget
CreateWidgets()

# create button with def function assigned to it
tk.Button(master, text='Create', command=create_dir).grid(
    row=6, column=1, sticky=tk.W, pady=10)

tk.Button(master, text='Clear', command=clear_btn).grid(
    row=6, column=1, sticky=tk.W, padx=50, pady=10)

tk.Button(master, text='Close', command=master.destroy).grid(
    row=6, column=1, sticky=tk.W, padx=92, pady=10)


master.mainloop()
