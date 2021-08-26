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
root.title("Grocery Store")
root.wm_iconbitmap('images\logo.ico')

# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))


# ==============  variables ======================
user = tkinter.StringVar()
passwd = tkinter.StringVar()



# ==============  Functions ======================
def admin():
    global option
    login_window.deiconify()
    option = 'admin'


def employee():
    global option
    login_window.deiconify()
    option = 'Employee'

def login():
    username = user.get()
    password = passwd.get()
    entry1.delete(0, tkinter.END)
    entry2.delete(0, tkinter.END)

    find_user = 'SELECT * FROM {} WHERE id = ? and password = ?'.format(option)
    
    print(username, password)
    cur.execute(find_user, [username, password])
    results = cur.fetchone()
    print(results)

    if results:
        print('login')
        root.withdraw()
        login_window.withdraw()
        os.system('python {}.py'.format(option))

    else:
        messagebox.showerror('Error', 'Incorrect username or password.')





# ==============  Background photo   =======================
# Make To be compatible with tkinter and resize photo
bg_photo = Image.open('images/home.jpg')
bg_photo = bg_photo.resize((window_width, window_height), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_photo)

# Place on the window
tkinter.Label(root, image=bg_photo).place(relx=0, rely=0)


# ==============  Admin Button   =======================
admin_logo = ImageTk.PhotoImage(Image.open("images/admin.png").resize((200, 200)))

# Create Admin button
button1 = tkinter.Button(root,image=admin_logo, borderwidth=5, bg='#cadbc3', relief=tkinter.RIDGE, command=admin)
button1.place(relx=0.25, rely=0.4, width=200, height=200)
tkinter.Label(root, text = 'Admin', font=('Arial', 15), bg='#ede5dd').place(relx=0.255, rely=0.6)

# ==============  Employee Button   =======================
# Photo for Employee button
employee_logo = ImageTk.PhotoImage(Image.open("images/employee.png").resize((200, 200)))

# Create Employee button
button2 = tkinter.Button(root,image=employee_logo, borderwidth=5, bg='#cadbc3', relief=tkinter.RIDGE, command=employee)
button2.place(relx=0.65, rely=0.4, width=200, height=200)
tkinter.Label(root, text = 'Employee', font=('Arial', 15), bg='#ede5dd').place(relx=0.655, rely=0.6)



# ==============  login Screen  ========================
login_window = tkinter.Toplevel(root)

login_window.title("Login")
login_window.geometry("{}x{}+{}+{}".format(window_width//7, window_height//3,
                        int(window_width/2.3), window_height//3))
login_window.iconbitmap('images\login.ico')

# login logo
login_logo = ImageTk.PhotoImage(Image.open("images/user_name.png").resize((20, 20)))
tkinter.Label(login_window, image=login_logo).place(relx=0.1, rely=0.2)
tkinter.Label(login_window,text='Username', font="-family {Poppins} -size 10" ).place(relx=0.1, rely=0.1)

# login entry
entry1 = tkinter.Entry(login_window)
entry1.place(relx=0.25, rely=0.2, relwidth=0.7, relheight=0.08)
entry1.configure(font="-family {Poppins} -size 10")
entry1.configure(relief="flat")
entry1.configure(textvariable=user)


# password logo
password_logo = ImageTk.PhotoImage(Image.open("images/password.png").resize((20, 20)))
tkinter.Label(login_window, image=password_logo).place(relx=0.1, rely=0.5)
tkinter.Label(login_window,text='Password', font="-family {Poppins} -size 10" ).place(relx=0.1, rely=0.4)

# password entry
entry2 = tkinter.Entry(login_window)
entry2.place(relx=0.25, rely=0.5, relwidth=0.7, relheight=0.08)
entry2.configure(font="-family {Poppins} -size 10")
entry2.configure(relief="flat")
entry2.configure(show="*")
entry2.configure(textvariable=passwd)

# login_buttons
button1 = TkinterCustomButton(master=login_window, corner_radius=20,text="LOGIN", command=login)
button1.place(relx=0.5, rely=0.8,  anchor=tkinter.CENTER)


# hide
login_window.withdraw()














# Execute Tkinter
root.mainloop()