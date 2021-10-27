import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pathlib import Path

# get user name
user = os.getlogin()
if user == "root":
    user = os.getenv("USER")


def make_file_if_not_exist():
    # touch does not overwrite file if it exists
    from pathlib import Path
    Path(counter_file).touch()


def add_one_to_file():
    make_file_if_not_exist()
    data = open(counter_file, 'r').read()
    data = data.strip()  # remove white space
    if len(data) == 0:
        data = 0
    data = int(data)  # convert to number
    data += 1  # add 1
    open(counter_file, 'w').write(str(data))


counter_file = Path(__file__).absolute().parent.joinpath("data")


def CreateWidgets():
    # create widget
    template_Label = Label(master, text='Select template: ')
    template_Label.grid(row=4, column=0, pady=5, padx=5)

    # template file source display
    master.sourceTemplate = Entry(
        master, width=50, textvariable=sourceLocation)
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
        master, width=50, textvariable=artSourceLocation)
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
        initialdir=r"C:\\Users\\bruta\\Desktop\\ai_files\\new"))

    # displays selected file(s) in the master.sourceText
    master.sourceTemplate.insert('1', master.files_list)


def ArtSourceBrowse():
    # opens file-dialog directory
    # prompts user to select file to copy
    # filedialog.askopenfilenames() method.
    # Initial directory set to server path where templates are housed
    # converts it to list using list()
    master.artfiles_list = list(filedialog.askopenfilenames(
        initialdir=r"C:\\Users\\bruta\\Desktop\\ai_files\\sourcebrowse"))

    # displays selected file(s) in the master.artSourceText
    master.artSource.insert('1', master.artfiles_list)


def create_dir():
    directory = e1.get() + "_" + e2.get() + "_" + e3.get()
    parent_dir = f"C:\\Users\\{user}\\Desktop"
    newFolder = path = os.path.join(parent_dir, directory)
    os.mkdir(newFolder)
    os.chdir(newFolder)
    add_one_to_file()
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
    path_abs = ('C:\\Users\\bruta\\Desktop\\ai_files\\test')
    walk = list(os.walk(path_abs))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)


# parent window
master = tk.Tk()
master.title('Go Fetch')
master.geometry('800x200')
icon = path = Path(__file__).absolute().parent.joinpath("tennisball.png")

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
artSourceLocation = StringVar()

# widget
CreateWidgets()


# create button with def function assigned to it
tk.Button(master, text='Create', command=create_dir).grid(
    row=6, column=1, sticky=tk.W, pady=2)

tk.Button(master, text='Close', command=master.destroy).grid(
    row=6, column=1, sticky=tk.W, padx=50, pady=10)

master.mainloop()
