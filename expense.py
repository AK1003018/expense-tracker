# expense tracking program using tkinter and mysql.connector

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime

# create a database connection object and cursor
db=mysql.connector.connect(user="root",passwd="Ak0272#",host="localhost")
cursor=db.cursor()

# create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS expense") # if database already exists, it will not create a new one
db.commit() # commit the changes

# create a table
cursor.execute("USE expense")
cursor.execute("CREATE TABLE IF NOT EXISTS expense (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, item VARCHAR(255), amount FLOAT)") # if table already exists, it will not create a new one
db.commit() # commit the changes

# create a window
window=tk.Tk()
window.title("Expense Tracker")
window.geometry("400x400")

# create a frame
frame=ttk.Frame(window)
frame.pack()

# create a label
label=ttk.Label(frame,text="Expense Tracker")
label.pack()




# create a function to add expense
def add_expense():
    # get the values from the entry boxes
    date=entry_date.get()
    item=entry_item.get()
    amount=entry_amount.get()
    # insert the values into the table
    cursor.execute("INSERT INTO expense (date,item,amount) VALUES (%s,%s,%s)",(date,item,amount))
    db.commit() # commit the changes
    # clear the entry boxes
    entry_date.delete(0,tk.END)
    entry_item.delete(0,tk.END)
    entry_amount.delete(0,tk.END)
    # show a message
    messagebox.showinfo("Success","Expense added successfully")
    
# create a function to view expense
def view_expense():
    # create a new window
    new_window=tk.Tk()
    new_window.title("View Expense")
    new_window.geometry("500x500")
    # create a frame
    frame=ttk.Frame(new_window)
    frame.pack()
    # create a label
    label=ttk.Label(frame,text="View Expense")
    label.pack()
    # create a treeview
    treeview=ttk.Treeview(frame)
    treeview.pack()
    # define the columns
    treeview["columns"]=("one","two","three")
    # format the columns
    treeview.column("#0",width=0)
    treeview.column("one",anchor=tk.CENTER,width=100)
    treeview.column("two",anchor=tk.CENTER,width=100)
    treeview.column("three",anchor=tk.CENTER,width=100)
    # create headings
    treeview.heading("#0",text="")
    treeview.heading("one",text="Date")
    treeview.heading("two",text="Item")
    treeview.heading("three",text="Amount")
    # insert data into the table
    cursor.execute("SELECT * FROM expense")
    rows=cursor.fetchall()
    for row in rows:
        treeview.insert("","end",values=row)
    # create a button
    button=ttk.Button(frame,text="Close",command=new_window.destroy)
    button.pack()
    # start the mainloop
    new_window.mainloop()
    
# create a function to delete expense
def delete_expense():
    # get the values from the entry boxes
    date=entry_date.get()
    item=entry_item.get()
    amount=entry_amount.get()
    # delete the values from the table
    cursor.execute("DELETE FROM expense WHERE date=%s AND item=%s AND amount=%s",(date,item,amount))
    db.commit() # commit the changes
    # clear the entry boxes
    entry_date.delete(0,tk.END)
    entry_item.delete(0,tk.END)
    entry_amount.delete(0,tk.END)
    # show a message
    messagebox.showinfo("Success","Expense deleted successfully")
    
# create a function to update expense
def update_expense():
    # get the values from the entry boxes
    date=entry_date.get()
    item=entry_item.get()
    amount=entry_amount.get()
    # update the values in the table
    cursor.execute("UPDATE expense SET date=%s,item=%s,amount=%s WHERE date=%s AND item=%s AND amount=%s",(date,item,amount,date,item,amount))
    db.commit() # commit the changes
    # clear the entry boxes
    entry_date.delete(0,tk.END)
    entry_item.delete(0,tk.END)
    entry_amount.delete(0,tk.END)
    # show a message
    messagebox.showinfo("Success","Expense updated successfully")
    
# create a function to clear expense
def clear_expense():
    # clear the entry boxes
    entry_date.delete(0,tk.END)
    entry_item.delete(0,tk.END)
    entry_amount.delete(0,tk.END)
    # show a message
    messagebox.showinfo("Success","Expense cleared successfully")
    
# create a function to exit the program
def exit_program():
    # show a message
    answer=messagebox.askquestion("Exit","Do you want to exit the program?")
    if answer=="yes":
        window.destroy()
        
# create a function to get the current date
def get_date():
    # get the current date
    today=datetime.date.today()
    # insert the current date into the entry box
    entry_date.insert(0,today)
    
# create a button to get the current date
button_date=ttk.Button(frame,text="Get Date",command=get_date)
button_date.pack()

# create a label
label_date=ttk.Label(frame,text="Date")
label_date.pack()

# create a label
label_date=ttk.Label(frame,text="Date")
label_date.pack()

# create an entry box
entry_date=ttk.Entry(frame)
entry_date.pack()

# create a label
label_item=ttk.Label(frame,text="Item")
label_item.pack()

# create an entry box
entry_item=ttk.Entry(frame)
entry_item.pack()

# create a label
label_amount=ttk.Label(frame,text="Amount")
label_amount.pack()

# create an entry box
entry_amount=ttk.Entry(frame)
entry_amount.pack()

# create a button
button_add=ttk.Button(frame,text="Add Expense",command=add_expense)
button_add.pack()

# create a button
button_view=ttk.Button(frame,text="View Expense",command=view_expense)
button_view.pack()

# create a button
button_delete=ttk.Button(frame,text="Delete Expense",command=delete_expense)
button_delete.pack()

# create a button
button_update=ttk.Button(frame,text="Update Expense",command=update_expense)
button_update.pack()

# create a button
button_clear=ttk.Button(frame,text="Clear Expense",command=clear_expense)
button_clear.pack()

# start the mainloop
window.mainloop()