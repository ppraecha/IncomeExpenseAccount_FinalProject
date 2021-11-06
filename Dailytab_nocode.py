import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar import DateEntry


def insert():
    a = Edate.get()
    b = e2.get()
    c = e4.get()
    data = [a,b,c]
    print(data)
    Op_table.insert("", 'end', values=data)



root1 = tk.Tk()

# set title
root1.title("HAPPY RICHIES")
root1.geometry("1500x1000")
root1.state('zoomed')


# set bg
entry = tk.Entry()


# Category drag down
cat_label = tk.Label(root1, text="Category:").place(x=215, y=180)


def selected(event):
    Category_label = tk.Label(root1, text=clicked.get()).place(x=350, y=180)


options = [
    "Transportation",
    "Food",
    "clothing",
    "Miscellaneous",
    "Healthcare",
]

clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root1, clicked, *options, command=selected)
drop.place(x=300, y=180)

# push button
daily_button = tk.Button(root1, text="Daily", padx=150, pady=10, borderwidth=30)
daily_button.place(x=200, y=50)

monthly_button = tk.Button(root1, text="Monthly", padx=150, pady=10, borderwidth=30)
monthly_button.place(x=900, y=50)

income_button = tk.Button(root1, text="Income", padx=30, pady=5, borderwidth=30)
income_button.place(x=600, y=210)

expense_button = tk.Button(root1, text="Expense", padx=30, pady=5, borderwidth=30)
expense_button.place(x=750, y=210)

insert_button = tk.Button(root1, text="Insert", padx=30, pady=5, borderwidth=30, command=insert)
insert_button.place(x=900, y=210)

target_button = tk.Button(root1, text="TARGET", padx=70, pady=5, borderwidth=30)
target_button.place(x=1050, y=120)

# input textbox

in_date = tk.Label(root1, text="Date:").place(x=244, y=120)
Edate = DateEntry(root1, width=10, background="blue", foreground="white")
Edate.place(x=300, y=120)

Transaction = tk.Label(root1, text="Transaction:").place(x=200, y=150)
e2 = tk.Entry(root1)
e2.place(x=300, y=150)

Amount = tk.Label(root1, text="Amount:").place(x=223, y=210)
e4 = tk.Entry(root1)
e4.place(x=300, y=210)


# Creates table
Table = ["Date", "Transaction", "Income", "Expense", "Balance"]
Op_table = ttk.Treeview(root1, column=Table, show="headings", height=27)
for i in Table:
    Op_table.heading(i, text=i.title())
Op_table.place(x=200, y=270)
# call app
root1.mainloop()
