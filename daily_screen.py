import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import target_screen as ts
import uni_save as us
import monthly_screen as ms
from datetime import datetime


class Screen:
    def __init__(self):
        # date
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.cur_year, self.cur_month, self.cur_date = self.date.split("-")
        # set up page
        self.root2 = tk.Tk()
        self.root2.title("HAPPY RICHIES")
        self.root2.geometry("1500x1000")
        # push button
        self.daily_button = tk.Button(self.root2, text="Daily", padx=150,
                                      pady=10, borderwidth=30)
        self.daily_button.place(x=200, y=50)
        self.monthly_button = tk.Button(self.root2, text="Monthly", padx=150,
                                        pady=10, borderwidth=30, command=self.monthly)
        self.monthly_button.place(x=900, y=50)
        self.income_button = tk.Button(self.root2, text="Income", padx=30,
                                       pady=5, borderwidth=30, command=self.income)
        self.income_button.place(x=600, y=210)
        self.expense_button = tk.Button(self.root2, text="Expense", padx=30,
                                        pady=5, borderwidth=30, command=self.expense)
        self.expense_button.place(x=750, y=210)
        self.target_button = tk.Button(self.root2, text="TARGET", padx=70,
                                       pady=5, borderwidth=30, command=self.target)
        self.target_button.place(x=1050, y=120)
        self.balance_button = tk.Button(self.root2, text="Balance", padx=30,
                                        pady=5, borderwidth=30, command=self.balance)
        self.balance_button.place(x=900, y=210)
        # label
        # input
        self.in_date = tk.Label(self.root2, text="Date:")
        self.in_date.place(x=244, y=120)
        self.date = Calendar(self.root2, selectmode="day", year=int(self.cur_year),
                             month=int(self.cur_month), day=int(self.cur_date))
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
            "Income",
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

        # target
        self.new_data = us.load_data("./user_data/cal.json")
        self.target = tk.Label(self.root2, text=self.new_data["monthly"])
        self.target.place(x=1125, y=150)

        # table
        self.table = ["Date", "Transaction", "Income", "Expense", "Balance"]
        self.op_table = ttk.Treeview(self.root2, column=self.table, show="headings", height=27)
        self.filter_month(int(self.cur_month), int(self.cur_year[2:4]))
        for i in self.table:
            self.op_table.heading(i, text=i.title())
        self.op_table.place(x=200, y=270)

    def income(self):
        a = self.date.get_date()
        b = self.e2.get()
        c = self.e4.get()
        d = self.clicked.get()
        data = [a, b, c, d, "income"]
        print(data)
        with open("user_data/trans_ls.txt", "a") as fa:
            fa.write(" ".join(data) + "\n")
            fa.close()
        a_split = list(map(int, a.split("/")))
        self.filter_month(a_split[0], a_split[2])

    def expense(self):
        a = self.date.get_date()
        b = self.e2.get()
        c = self.e4.get()
        d = self.clicked.get()
        data = [a, b, c, d, "expense"]
        print(data)
        with open("user_data/trans_ls.txt", "a") as fa:
            fa.write(" ".join(data) + "\n")
            fa.close()
        a_split = list(map(int, a.split("/")))
        self.filter_month(a_split[0], a_split[2])

    def target(self):
        self.root2.destroy()
        ts.Screen()

    def update_ls(self):
        with open("user_data/trans_ls.txt", "r") as fr:
            for line in fr:
                data = line.strip("\n").split()
                if data[-1] == "income":
                    self.op_table.insert("", 'end', values=data[0:3])
                elif data[-1] == "expense":
                    render_data = data[0:2] + [" ", data[2]]
                    self.op_table.insert("", 'end', values=render_data)
            fr.close()

    def balance(self):
        temp_date = self.date.get_date().split("/")
        temp_month, temp_year = temp_date[0], temp_date[2]
        self.filter_month(int(temp_month), int(temp_year))
        print(temp_date)
        print(temp_month)
        print(temp_year)
        total = 0
        with open("user_data/trans_ls.txt", "r") as fr:
            for line in fr:
                data = line.strip("\n").split()
                line_date = data[0].split("/")
                if data[-1] == "income" and line_date[0] == temp_month and line_date[2] == temp_year:
                    total += int(data[2])
                elif data[-1] == "expense" and line_date[0] == temp_month and line_date[2] == temp_year:
                    total -= int(data[2])
            print(data)
            print(total)
            fr.close()

            if total > self.new_data["monthly"]:
                label = tk.Label(self.root2, text=" ☻ Congratulation! GOOD JOB for this month!",
                                 bg="green", padx=30, pady=20, width=30)
                label.place(x=1050, y=180)
            else:
                label = tk.Label(self.root2, text=" ☹ Please TRY AGAIN NEXT MONTH",
                                 bg="red", padx=30, pady=20, width=30)
                label.place(x=1050, y=180)
            self.op_table.insert("", 'end', values=["", "", "", "", total])

            bal_dict = us.load_data("./user_data/balance.json")
            print(bal_dict)
            bal_key = str(temp_month) + "/" + str(temp_year)
            bal_dict[bal_key] = total
            us.save_data(bal_dict, "./user_data/balance.json")

    def monthly(self):
        self.root2.destroy()
        ms.Screen()

    def filter_month(self, month, year):
        # clear table
        self.op_table.delete(*self.op_table.get_children())
        with open("user_data/trans_ls.txt", "r") as fr:
            for line in fr:
                data = line.strip("\n").split()
                cur_date = list(map(int, data[0].split("/")))
                if cur_date[0] != month or cur_date[2] != year:
                    continue
                if data[-1] == "income":
                    self.op_table.insert("", 'end', values=data[0:3])
                elif data[-1] == "expense":
                    render_data = data[0:2] + [" ", data[2]]
                    self.op_table.insert("", 'end', values=render_data)
            fr.close()
