import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from custom_button import TkinterCustomButton


# Creat window
root = tkinter.Tk()
root.title("Billing")
root.wm_iconbitmap('images\logo.ico')

# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))
root.configure(background='#698c7b')
# ===========================================================================


root.mainloop()