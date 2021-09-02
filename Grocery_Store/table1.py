from tkinter import *
from tkinter import ttk

# Creat window
root = Tk()
root.title("Grocery Store")
root.wm_iconbitmap('images\logo.ico')

# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))

my_tree = ttk.Treeview(root)

# Define Our Colums
my_tree['columns'] = ('Name','ID','Favourite')

# Format Our Columns
# IF you don't use parent and Children( widht = 0)
# To be column gone, stretch=NO
my_tree.column('#0', width=120, minwidth=25 )
my_tree.column('Name', anchor=W, width=120)
my_tree.column('ID', anchor=CENTER, width=80)
my_tree.column('Favourite', anchor=W, width=100)

# Create Headings
my_tree.heading('#0', text='Label', anchor=W)
my_tree.heading('Name', text = 'Customer Name', anchor=W)
my_tree.heading('ID', text = 'ID', anchor=CENTER)
my_tree.heading('Favourite', text = 'Favourite', anchor=W)




# Add data
my_tree.insert(parent='', index='end', iid=0, text='Parent', values=('John',1,'Apple'))
my_tree.insert(parent='', index='end', iid=1, text='Parent', values=('Mg Mg',1,'Apple'))
my_tree.insert(parent='', index='end', iid=2, text='Parent', values=('Aung Aung',1,'Apple'))
my_tree.insert(parent='', index='end', iid=3, text='Parent', values=('Zaw Zaw',1,'Apple'))
my_tree.insert(parent='', index='end', iid=4, text='Parent', values=('Kyaw Kyaw',1,'Apple'))
my_tree.insert(parent='', index='end', iid=5, text='Parent', values=('Zaw',1,'Apple'))


# add child
my_tree.insert(parent='', index='end', iid=6, text='Child', values=('Zaw',1,'Apple'))
my_tree.move('6', '0', '0')



my_tree.pack()

root.mainloop()


