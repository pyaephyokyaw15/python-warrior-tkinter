import tkinter
from tkinter.constants import LEFT, RIGHT
# from tkinter import *

# create window
root = tkinter.Tk()
root.iconbitmap('image\logo.ico')
root.title('GUI v-1')

# full screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('{}x{}+0+0'.format(width, height))

# =========== variables ==============================

text = tkinter.StringVar(root, value='hello')
input_txt = tkinter.StringVar()


#  ==================  funtions  =========================
def hello():
    # create label
    label = tkinter.Label(root, text='hello', bg='#e68632', font=("Helvetica", 20), width=100)
    # palce label
    label.pack()



def hello():
    text.set(input_text.get())
    input_txt.set('')
    

# ======================  widgets ==============================================


# create label
label1 = tkinter.Label(root, textvariable=text, bg='#e68632', font=("Helvetica", 14), anchor='e', width=100)
# place label
label1.pack()

# create button
btn = tkinter.Button(root, text ="Click me", width=15, height=10, activebackground='#e68632', command=hello)
# place label
btn.pack()

# create entry
input_text = tkinter.Entry(root, font=("Helvetica", 14), textvariable=input_txt)
# place entry
input_text.pack()




root.mainloop()