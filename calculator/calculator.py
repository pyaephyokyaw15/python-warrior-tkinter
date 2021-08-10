from tkinter import *
import custom_button

# create window
root = Tk()
root.iconbitmap('image\calculator.ico')
root.title('Calculator')
root.configure(bg = 'white')


# ==================== Functions =====================================

def on_key(number):
    screen.insert(END, number)


def calculate():
    ans = eval(screen.get())
    screen.delete(0, END)
    screen.insert(END, ans)


    





# =====================  Display ======================================

# create entry
screen= Entry(root, font=("Helvetica", 14), justify='right', bg='#e8d295', fg='yellow')
# place entry
screen.grid(row=0, column=0, columnspan=3, ipady=20)


# ========================== Keys ======================================

# Numbers
button_7 = Button(root, text ="7", width=5, height=3, command=lambda:on_key('7'))
button_7.grid(row=1, column=0, pady=10)

button_8 = Button(root, text ="8", width=5, height=3, command=lambda:on_key('8'))
button_8.grid(row=1, column=1, pady=10)

button_9 = Button(root, text ="9", width=5, height=3, command=lambda:on_key('9'))
button_9.grid(row=1, column=2, pady=10)

button_4 = Button(root, text ="4", width=5, height=3, command=lambda:on_key('4'))
button_4.grid(row=2, column=0, pady=10)

button_5 = Button(root, text ="5", width=5, height=3, command=lambda:on_key('5'))
button_5.grid(row=2, column=1, pady=10)

button_6 = Button(root, text ="6", width=5, height=3, command=lambda:on_key('6'))
button_6.grid(row=2, column=2, pady=10)

button_1 = Button(root, text ="1", width=5, height=3, command=lambda:on_key('1'))
button_1.grid(row=3, column=0, pady=10)

button_2 = Button(root, text ="2", width=5, height=3, command=lambda:on_key('2'))
button_2.grid(row=3, column=1, pady=10)

button_3 = Button(root, text ="3", width=5, height=3, command=lambda:on_key('3'))
button_3.grid(row=3, column=2, pady=10)

# Operators
add_btn = Button(root, text ="+", width=5, height=3, command=lambda:on_key('+'))
add_btn.grid(row=4, column=0, pady=10)

minus_btn = Button(root, text ="-", width=5, height=3, command=lambda:on_key('-'))
minus_btn.grid(row=4, column=1, pady=10)

multlipy_btn = Button(root, text ="x", width=5, height=3, command=lambda:on_key('*'))
multlipy_btn.grid(row=4, column=2, pady=10)

divide_btn = Button(root, text ="÷", width=5, height=3, command=lambda:on_key('/'))
divide_btn.grid(row=5, column=0, pady=10)

calculate_btn = Button(root, text ="=", width=5, height=3, command=calculate)
calculate_btn.grid(row=5, column=1, pady=10)

clear_btn = Button(root, text ="AC", width=5, height=3, command=lambda:screen.delete(0, END))
clear_btn.grid(row=5, column=2, pady=10)


round_btn = custom_button.TkinterCustomButton(master=root, text='5', width=50, height=50, corner_radius=100)
round_btn.grid(row=6, column=0)

root.mainloop()