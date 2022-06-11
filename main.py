import tkinter as tk                                                                 #SG

from tkinter import * 

window = Tk()
window.title('Library Book Management')
window.geometry('900x500')
window.configure(bg='light grey')

import sqlite3

conn = sqlite3.connect('books.db')
cursorObj = conn.cursor()

conn = sqlite3.connect('books.db')
cursorObj = conn.cursor()
cursorObj.execute('CREATE TABLE IF NOT EXISTS book_table( bookname TEXT, author TEXT,year TEXT ,bookstatus TEXT)')

lb1 = Listbox(window,width=40, height=10,)
lb1.grid(row = 4 ,column =0,columnspan = 7)

t1 = Text(window,height=1,width=20)
t1.grid(row=5,column=1)

wel = str("      Welcome!")
t1.insert(END,wel)

e1_var = StringVar()

e1 = Entry(window,textvariable = e1_var)
e1.grid(row=0,column=1)

e2_var = StringVar()

e2 = Entry(window,textvariable = e2_var)
e2.grid(row=1,column=1)

e3_var = StringVar()

e3 = Entry(window, textvariable = e3_var)
e3.grid(row=2,column=1)

e4_var = str('not issued')

l1 = tk.Label(window, text="Book name :")
l1.grid(row=0,column=0)

l2 = tk.Label(window, text="Author name :")
l2.grid(row=1,column=0)

l3 = tk.Label(window, text="year :")
l3.grid(row=2,column=0)

l4 = tk.Label(window, text="Status :")
l4.grid(row=5,column=0)

l5 = tk.Label(window, text="Exist  :")
l5.grid(row=17,column=3)

l6 = tk.Label(window, text="Enter elements into entry widget to perform operations",bg='orange')
l6.grid(row=0,column=3)

def insert_books():
    conn = sqlite3.connect('books.db')
    cursorObj = conn.cursor()
    cursorObj.execute('INSERT INTO book_table values(?,?,?,?)',(e1_var.get(),e2_var.get(),e3_var.get(),e4_var))
    conn.commit()
    t1.delete("1.0",END)
    a = str("Book Added !")
    t1.insert(END,a)
    
    
global rows
conn = sqlite3.connect('books.db')
cursorObj = conn.cursor()
cursorObj.execute('SELECT * FROM book_table')
rows = cursorObj.fetchall()
conn.commit()

def read_d():
    global rows
    conn = sqlite3.connect('books.db')
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT * FROM book_table')
    rows = cursorObj.fetchall()
    conn.commit()
    lb1.delete(0,END)
    lb1.insert(0,*rows)
    t1.delete("1.0",END)
    r = str("All Data Read !")
    t1.insert(END,r)
    


def delete_book():
    global e55_var
    conn = sqlite3.connect('books.db')
    cursorObj = conn.cursor()
    cursorObj.execute('DELETE From book_table WHERE  bookname = ?',[e1_var.get()])
    conn.commit()
    conn.close()
    t1.delete("1.0",END)
    d = str("Book Deleted !")
    t1.insert(END,d )
    
def Search_books():
    global lb1,row1,e3
    conn = sqlite3.connect('books.db')
    cursorObjSearch_books = conn.cursor()
    cursorObj.execute('SELECT * FROM book_table WHERE bookname like ? or author like ? or year like ? ',[e1_var.get(),e2_var.get(),e3_var.get()])
    row1 = cursorObj.fetchall()
    conn.commit()
    conn.close()
    #e3.delete(0,END)
    #e3.insert(0,0)
    lb1.delete(0,END)
    lb1.insert(0,*row1)
    t1.delete("1.0",END)
    s = str("Book Searched !")
    t1.insert(END,s)

def insert_books():
    conn = sqlite3.connect('books.db')
    cursorObj = conn.cursor()
    cursorObj.execute('INSERT INTO book_table values(?,?,?,?)',(e1_var.get(),e2_var.get(),e3_var.get(),e4_var))
    conn.commit()
    t1.delete("1.0",END)
    a = str("Book Added !")
    t1.insert(END,a)
    


def issue_book():
    global t1
    e4_var = str('issued')
    conn = sqlite3.connect('books.db')
    cursorObj = conn.cursor()
    cursorObj.execute('UPDATE book_table SET bookstatus = ?  WHERE bookname  = ?',[e4_var,e1_var.get()])
    #rows = cursorObj.fetchall()
    conn.commit()
    conn.close()
    #return rows
    t1.delete("1.0",END)
    i = str("Book Issued !")
    t1.insert(END,i)
    
    
def withdraw_book():
    global t1
    e4_var = str('not issued')
    conn = sqlite3.connect('books.db')
    cursorObj = conn.cursor()
    cursorObj.execute('UPDATE book_table SET bookstatus = ?  WHERE bookname  = ?',[e4_var,e1_var.get()])
    #rows = cursorObj.fetchall()
    conn.commit()
    conn.close()
    #return rows
    t1.delete("1.0",END)
    w = str("Book withdrew !")
    t1.insert(END,w)

def Quit():
    window.destroy()
b_insert=tk.Button(window, text ="Add Book",bg='pink', command = insert_books)
b_insert.grid(row=3,column=0)

b_read=tk.Button(window, text ="Read",bg='pink', command = read_d)
b_read.grid(row=3,column=1)

b_delete=tk.Button(window, text ="delete",bg='pink', command = delete_book)
b_delete.grid(row=3,column=2)

b_search=tk.Button(window, text ="search",bg='pink', command = Search_books)
b_search.grid(row=3,column=3)

b_issue=tk.Button(window, text ="issue book",bg='pink', command = issue_book)
b_issue.grid(row=3,column=4)

b_withdraw =tk.Button(window, text ="return book",bg='pink', command = withdraw_book)
b_withdraw.grid(row=3,column=6)

B_quit = tk.Button(window, text ="Close Window",bg='red', command = Quit )
B_quit.grid(row =18 ,column=3)

window.mainloop()
