from tkinter import *
import time
from tododb import Database
from tkinter import messagebox


app = Tk()
app.title('Abdulsalam\'s List')
app.geometry('310x510')
app.configure(background='White')
app.resizable(0, 0)
# app.position(side='right')
db = Database('todo.db')

def add_item():
    if text_.get() == '':
        messagebox.showerror('Required Fields', 'Please input Task')
        return
    entry = text_.get()
    todo_list.insert(END, entry)
    db.insert(entry)
    text_.set('')


def clear_list():
    todo_list.delete(0, END)
    db.clear_data()
    

def select_item(event):
    global selected_item
    index = todo_list.curselection()[0]
    selected_item = todo_list.get(index)


def remove_task():
    while select_item:
        todo_list.delete([0])
        break

    
    
#widgets
#Heading Text
heading_l = Label(app, text='To-do List', font=('Arial black', 20, 'bold'), 
                        fg ='white', bg='Blue')
heading_l.grid(row=0, column=0, pady=5, padx=5)

#Input Text
text_ = StringVar()
text_entry = Entry(app, width=20, textvariable=text_)
text_entry.grid(row=1, column=0, columnspan=2, padx=7, ipadx=4, sticky=W)

#Add button
add_bt = Button(app, font=('bold', 10), text='Add task', fg='white', bg='blue', command=add_item) 
add_bt.grid(row=1, column=1, padx=20)

#TO-DO list
todo_list = Listbox(app, height=19, width=30, bg='white', fg='Blue', border=0, font=('Arialblack'))
todo_list.grid(row=2, column=0, columnspan=3, rowspan=7, padx=5, sticky=W)

#Reomve button
remove_bt = Button(app, text='Remove task', fg='white', bg='blue', command=remove_task) 
remove_bt.grid(row=10, column=0)

#CLear button
clear_bt = Button(app, text='Clear List', bg='blue', fg='white', command=clear_list) 
clear_bt.grid(row=10, column=1, pady=5)


# if text_ != '':
#     add_item()





app.mainloop()
