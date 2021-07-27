import tkinter

# create window
root = tkinter.Tk()
root.iconbitmap('image\logo.ico')
root.title('GUI v-1')

# full screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('{}x{}+0+0'.format(width, height))



root.mainloop()