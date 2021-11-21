import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import target_screen as ts
import uni_save



class Screen:
    def __init__(self):
        # set up page
        self.root2 = tk.Tk()
        self.root2.title("HAPPY RICHIES")
        self.root2.geometry("1500x1000")
        # push button
        self.daily_button = tk.Button(self.root2, text="Daily", padx=150, pady=10, borderwidth=30)
        self.daily_button.place(x=200, y=50)
        self.monthly_button = tk.Button(self.root2, text="Monthly", padx=150, pady=10, borderwidth=30)
        self.monthly_button.place(x=900, y=50)
        self.income_button = tk.Button(self.root2, text="Income", padx=30, pady=5, borderwidth=30, command=self.income)
        self.income_button.place(x=600, y=210)
        self.expense_button = tk.Button(self.root2, text="Expense", padx=30, pady=5, borderwidth=30, command=self.expense)
        self.expense_button.place(x=750, y=210)
        self.target_button = tk.Button(self.root2, text="TARGET", padx=70, pady=5, borderwidth=30, command=self.target)
        self.target_button.place(x=1050, y=120)
        self.balance_button = tk.Button(self.root2, text="Balance", padx=30, pady=5, borderwidth=30, command=self.balance)
        self.balance_button.place(x=900, y=210)
        # label
        # input
        self.in_date = tk.Label(self.root2, text="Date:")
        self.in_date.place(x=244, y=120)
        self.date = Calendar(self.root2, selectmode="day", year=2021, month=11, day=18)
        self.date.place(x=300, y=110)
        # input2
        self.transaction = tk.Label(self.root2, text="Transaction:")
        self.transaction.place(x=600, y=110)
        self.e2 = tk.Entry(self.root2)
        self.e2.place(x=700, y=110)
        # input3
        self.current_option = "Transportation"
        self.category = tk.Label(self.root2, text="Category:")
        self.category.place(x=600, y=140)
        self.options = [
            "Transportation",
            "Food",
            "clothing",
            "Miscellaneous",
            "Healthcare"
        ]
        self.clicked = StringVar()
        self.clicked.set(self.options[0])
        self.drop = OptionMenu(self.root2, self.clicked, *self.options)
        self.drop.place(x=700, y=140)
        # input4
        self.amount = tk.Label(self.root2, text="Amount:")
        self.amount.place(x=600, y=170)
        self.e4 = tk.Entry(self.root2)
        self.e4.place(x=700, y=170)
        self.new_data = uni_save.load_data("./user_data/cal.json")
        self.target = tk.Label(self.root2, text=self.new_data["daily"])
        self.target.place(x=1050, y=150)

        # table
        self.table = ["Date", "Transaction", "Income", "Expense", "Balance"]
        self.op_table = ttk.Treeview(self.root2, column=self.table, show="headings", height=27)
        self.update_ls()
        for i in self.table:
            self.op_table.heading(i, text=i.title())
        self.op_table.place(x=200, y=270)

    def income(self):
        a = self.date.get_date()
        b = self.e2.get()
        c = self.e4.get()
        d = self.clicked.get()
        data = [a, b, c, d, "income"]
        print(d)
        print(data)
        with open("./user_data/trans_ls.txt", "a") as fa:
            fa.write(" ".join(data) + "\n")
            fa.close()
        self.op_table.insert("", 'end', values=data[0:3])

    def expense(self):
        a = self.date.get_date()
        b = self.e2.get()
        c = self.e4.get()
        d = self.clicked.get()
        data = [a, b, c, d, "expense"]
        print(data)
        with open("./user_data/trans_ls.txt", "a") as fa:
            fa.write(" ".join(data) + "\n")
            fa.close()
        render_data = data[0:2] + [" ", data[2]]
        self.op_table.insert("", 'end', values=render_data)

    def target(self):
        self.root2.destroy()
        ts.Screen()

    def update_ls(self):
        with open("./user_data/trans_ls.txt", "r") as fr:
            for line in fr:
                data = line.strip("\n").split()
                if data[-1] == "income":
                    self.op_table.insert("", 'end', values=data[0:3])
                elif data[-1] == "expense":
                    render_data = data[0:2] + [" ", data[2]]
                    self.op_table.insert("", 'end', values=render_data)
            fr.close()

    def balance(self):
        total = 0
        with open("./user_data/trans_ls.txt", "r") as fr:
            for line in fr:
                data = line.strip("\n").split()
                if data[-1] == "income":
                    total += int(data[2])
                elif data[-1] == "expense":
                    total -= int(data[2])
            print(total)
            fr.close()

        if total < -self.new_data["daily"]:
            label = tk.Label(self.root2, bg="red", padx=100, pady=20)
            label.place(x=1050, y=180)
        else:
            label = tk.Label(self.root2, bg="green", padx=100, pady=20)
            label.place(x=1050, y=180)
        self.op_table.insert("", 'end', values=["", "", "", "", total])




