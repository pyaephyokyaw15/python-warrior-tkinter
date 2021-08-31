# importing libraries
import tkinter
from PIL import ImageTk, Image
from custom_button import TkinterCustomButton
import sqlite3
import os
from tkinter import messagebox


# Database Connection
with sqlite3.connect('grocery_store.db') as db:
    cur = db.cursor()


# Creat window
root = tkinter.Tk()
root.title("Employee Manager")
root.wm_iconbitmap('images\logo.ico')

# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))


root.mainloop()