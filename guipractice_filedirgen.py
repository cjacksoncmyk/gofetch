import os
import tkinter as tk

# create_dir = this creates the new folder dir from user input


def create_dir():
    directory = job_name.get() + "_" + job_product.get() + "_" + job_number.get()
    parent_dir = r"C:\Users\bruta\Desktop"
    newFolder = path = os.path.join(parent_dir, directory)
    os.mkdir(newFolder)
    os.chdir(newFolder)
    for dir in ['Art', 'Production', 'Proof']:
        os.mkdir(dir)
    print("Directory '%s' created" % directory)
    job_name.delete(0, tk.END)
    job_product.delete(0, tk.END)
    job_number.delete(0, tk.END)


# parent window
master = tk.Tk()
master.title('Go Fetch Beta')
master.geometry('275x100')
tk.Label(master, text='Enter Job Name: ').grid(row=0)
tk.Label(master, text='Enter Job Product: ').grid(row=1)
tk.Label(master, text='Enter Job Number: ').grid(row=2)

job_name = tk.Entry(master)
job_product = tk.Entry(master)
job_number = tk.Entry(master)

job_name.grid(row=0, column=1)
job_product.grid(row=1, column=1)
job_number.grid(row=2, column=1)

tk.Button(master, text='Create', command=create_dir).grid(
    row=4, column=1, sticky=tk.W, pady=2)

master.mainloop()
