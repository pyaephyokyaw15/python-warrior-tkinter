# importing libraries
import tkinter
from PIL import ImageTk, Image
from custom_button import TkinterCustomButton
import sqlite3
import os
from tkinter import messagebox
from tkinter import ttk


# Database Connection
with sqlite3.connect('grocery_store.db') as db:
    cur = db.cursor()


# Creat window
root = tkinter.Tk()
root.title("Inventory")
root.wm_iconbitmap('images\logo.ico')

# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))

# ===================variables============================

new_ID = tkinter.StringVar()
new_item = tkinter.StringVar()
new_quantity = tkinter.StringVar()
new_price = tkinter.StringVar()

# ===================== functions ============================================
def search():
    pass

def add_item():
    print(new_ID.get(), new_item.get(), new_quantity.get(), new_price.get())
    print(type(new_ID.get()), type(new_item.get()), type(new_quantity.get()), type(new_price.get()))
    
    sql_command = ''' INSERT INTO Inventory (id,item,quantity,price)
                    VALUES(?,?,?,?)'''
    cur.execute(sql_command, (new_ID.get(), new_item.get(), int(new_quantity.get()), int(new_price.get())))
    db.commit()
    new_ID.set('')
    new_item.set('')
    new_price.set('')
    new_quantity.set('')
    show_items()
    
   
      
def remove_item():
    sql_command = ''' DELETE FROM Inventory  WHERE id = ?'''
    cur.execute(sql_command, [str(new_ID.get())])
    db.commit()
    new_ID.set('')
    new_item.set('')
    new_price.set('')
    new_quantity.set('')
    show_items()


def edit_item():
    sql_command = ''' UPDATE Inventory SET item =?, quantity = ?, price = ?  WHERE id = ?'''
    cur.execute(sql_command, (new_item.get(), int(new_quantity.get()), int(new_price.get()), new_ID.get()))
    db.commit()
    new_ID.set('')
    new_item.set('')
    new_price.set('')
    new_quantity.set('')
    show_items()


def show_items():
    clear_items()
    sql_command = "SELECT * FROM Inventory ORDER BY quantity ASC"
    cur.execute(sql_command)
    data = cur.fetchall()
    print(data)
    for num, record in enumerate(data):
        print(record)
        my_tree.insert(parent='', index='end', iid=num, values=(record[0], record[1], record[2], record[3]))


def clear_items():
    my_tree.delete(*my_tree.get_children())



# =================================== Manage Items ==============================================

tkinter.Label(root, text = 'Inventory', font="-family {Poppins} -size 40", background='#73695f').place(relx=0.4, rely=0.05, anchor=tkinter.W)
product = tkinter.LabelFrame(root, text='Items', font="-family {Poppins} -size 20")
product.place(relx= 0.05, rely=0.15, relwidth=0.45, relheight=0.7)


# ID
tkinter.Label(product, text='ID',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.1)
entry1 = tkinter.Entry(product)
entry1.place(relx=0.25, rely=0.1, relwidth=0.7, relheight=0.05)
entry1.configure(font="-family {Poppins} -size 15")
entry1.configure(relief="flat")
entry1.configure(textvariable=new_ID)

# Item
tkinter.Label(product, text='Item',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.3)
entry2 = tkinter.Entry(product)
entry2.place(relx=0.25, rely=0.3, relwidth=0.7, relheight=0.05)
entry2.configure(font="-family {Poppins} -size 15")
entry2.configure(relief="flat")
entry2.configure(textvariable=new_item)

# quantity
tkinter.Label(product, text='In Stock',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.5)
entry3 = tkinter.Entry(product)
entry3.place(relx=0.25, rely=0.5, relwidth=0.7, relheight=0.05)
entry3.configure(font="-family {Poppins} -size 15")
entry3.configure(relief="flat")
entry3.configure(textvariable=new_quantity)

# price
tkinter.Label(product, text='Price',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.7)
entry4 = tkinter.Entry(product)
entry4.place(relx=0.25, rely=0.7, relwidth=0.7, relheight=0.05)
entry4.configure(font="-family {Poppins} -size 15")
entry4.configure(relief="flat")
entry4.configure(textvariable=new_price)



# ==================================== Buttons =====================================


search_btn = TkinterCustomButton(master=product, corner_radius=20,text="Search", command=search)
search_btn.place(relx=0.01, rely=0.9)

add_btn = TkinterCustomButton(master=product, corner_radius=20,text="Add Item", command=add_item)
add_btn.place(relx=0.21, rely=0.9)

remove_btn = TkinterCustomButton(master=product, corner_radius=20,text="Remove Item", command=remove_item)
remove_btn.place(relx=0.41, rely=0.9)


edit_btn = TkinterCustomButton(master=product, corner_radius=20,text="Edit Item", command=edit_item)
edit_btn.place(relx=0.61, rely=0.9)


exit_btn = TkinterCustomButton(master=product, corner_radius=20,text="Exit", command=exit)
exit_btn.place(relx=0.81, rely=0.9)


# ======================= Table ======================================
item_aera= tkinter.Frame(root)
item_aera.place(relx=0.52,rely=0.12,relwidth=0.5,relheight=0.78, )

my_tree = ttk.Treeview(item_aera, height=10)
my_tree.place(relx=0,rely=0, relwidth=0.9, relheight=1)
style = ttk.Style()
style.configure("Treeview", font="-family {Poppins} -size 12", rowheight=30)
style.configure("Treeview.Heading", font="-family {Poppins} -size 15")


my_tree['columns'] = ('Item-ID', 'Item', 'Quantity', 'Price')

my_tree.column('#0', width=0, minwidth=0, stretch=tkinter.NO)
my_tree.column('Item-ID', width=100)
my_tree.column('Item', width=200)
my_tree.column('Quantity', width=50)
my_tree.column('Price', width=50)



# heading
my_tree.heading('#0', text='')
my_tree.heading('Item-ID', text = 'Item ID')
my_tree.heading('Item', text = 'Item')
my_tree.heading('Quantity', text = 'In Stock')
my_tree.heading('Price', text = 'Price')

show_items()
# loop forever
root.mainloop()