import tkinter as tk
import daily_screen as ds
import uni_save as us
import monthly_screen as ms
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from months_package import Jan
from months_package import Mar
from months_package import Apr
from months_package import May
from months_package import Jun
from months_package import Jul
from months_package import Aug
from months_package import Sep
from months_package import Oct
from months_package import Nov
from months_package import Dec


class Screen:
    def __init__(self):
        # set up page
        self.root5 = tk.Tk()
        self.root5.title("HAPPY RICHIES")
        self.root5.geometry("1500x1000")
        # push button
        self.daily_button = tk.Button(self.root5, text="Daily", padx=150, pady=10, borderwidth=30, command=self.daily)
        self.daily_button.place(x=200, y=50)
        self.monthly_button = tk.Button(self.root5, text="Monthly", padx=150, pady=10, borderwidth=30,
                                        command=self.overall)
        self.monthly_button.place(x=900, y=50)
        # moth push button
        self.overall_button = tk.Button(self.root5, text="Overall", padx=50, pady=10, borderwidth=30,
                                        command=self.overall)
        self.overall_button.place(x=200, y=150)
        self.jan_button = tk.Button(self.root5, text="January", padx=47, pady=10, borderwidth=30, command=self.jan)
        self.jan_button.place(x=200, y=190)
        self.feb_button = tk.Button(self.root5, text="February", padx=44, pady=10, borderwidth=30)
        self.feb_button.place(x=200, y=230)
        self.mar_button = tk.Button(self.root5, text="March", padx=52, pady=10, borderwidth=30, command=self.mar)
        self.mar_button.place(x=200, y=270)
        self.apr_button = tk.Button(self.root5, text="April", padx=58, pady=10, borderwidth=30, command=self.apr)
        self.apr_button.place(x=200, y=310)
        self.may_button = tk.Button(self.root5, text="May", padx=59, pady=10, borderwidth=30, command=self.may)
        self.may_button.place(x=200, y=350)
        self.jun_button = tk.Button(self.root5, text="June", padx=57, pady=10, borderwidth=30, command=self.jun)
        self.jun_button.place(x=200, y=390)
        self.jul_button = tk.Button(self.root5, text="July", padx=60, pady=10, borderwidth=30, command=self.jul)
        self.jul_button.place(x=200, y=430)
        self.aug_button = tk.Button(self.root5, text="August", padx=51, pady=10, borderwidth=30, command=self.aug)
        self.aug_button.place(x=200, y=470)
        self.sep_button = tk.Button(self.root5, text="September", padx=39, pady=10, borderwidth=30, command=self.sep)
        self.sep_button.place(x=200, y=510)
        self.oct_button = tk.Button(self.root5, text="October", padx=48, pady=10, borderwidth=30, command=self.oct)
        self.oct_button.place(x=200, y=550)
        self.nov_button = tk.Button(self.root5, text="November", padx=42, pady=10, borderwidth=30, command=self.nov)
        self.nov_button.place(x=200, y=590)
        self.dec_button = tk.Button(self.root5, text="December", padx=42, pady=10, borderwidth=30, command=self.dec)
        self.dec_button.place(x=200, y=630)
        # year push button
        self.year_2021 = tk.Button(self.root5, text="2021", padx=20, pady=10, borderwidth=30, command=self.overall)
        self.year_2021.place(x=200, y=100)
        self.year_2020 = tk.Button(self.root5, text="2020", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2020.place(x=290, y=100)
        self.year_2019 = tk.Button(self.root5, text="2019", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2019.place(x=380, y=100)
        self.year_2018 = tk.Button(self.root5, text="2018", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2018.place(x=470, y=100)
        self.year_2017 = tk.Button(self.root5, text="2017", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2017.place(x=560, y=100)
        self.year_2016 = tk.Button(self.root5, text="2016", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2016.place(x=650, y=100)
        self.year_2015 = tk.Button(self.root5, text="2015", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2015.place(x=740, y=100)
        self.year_2014 = tk.Button(self.root5, text="2014", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2014.place(x=830, y=100)
        self.year_2013 = tk.Button(self.root5, text="2013", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2013.place(x=920, y=100)
        self.year_2012 = tk.Button(self.root5, text="2012", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2012.place(x=1010, y=100)
        self.year_2011 = tk.Button(self.root5, text="2011", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2011.place(x=1100, y=100)
        self.year_2010 = tk.Button(self.root5, text="2010", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2010.place(x=1190, y=100)
        # input saving
        self.data = us.load_data("./user_data/balance.json")
        self.save = tk.Label(self.root5, text=self.data["2/21"])
        self.save.place(x=1300, y=480)
        self.save_save = tk.Label(self.root5, text="Saving:")
        self.save_save.place(x=1200, y=480)

        # input target save
        self.new_data = us.load_data("./user_data/cal.json")
        self.target = tk.Label(self.root5, text=self.new_data["monthly"])
        self.target.place(x=1300, y=500)
        self.target_save = tk.Label(self.root5, text="Target Saving:")
        self.target_save.place(x=1200, y=500)

        # input Differences
        self.minus = int(self.data["2/21"]) - int(self.new_data["monthly"])
        self.minus_show = tk.Label(self.root5, text=self.minus)
        self.minus_show.place(x=1300, y=530)
        self.dif_save = tk.Label(self.root5, text="Differences:")
        self.dif_save.place(x=1200, y=530)

        # show congrats
        if self.data["2/21"] > self.new_data["monthly"]:
            label = tk.Label(self.root5, text=" ☻ Congratulation!" + "\n" + "GOOD JOB for this month!", bg="green",
                             padx=30,
                             pady=20, width=14, height=10)
            label.place(x=1200, y=560)
        else:
            label = tk.Label(self.root5, text=" ☹ Please" + "\n" + "TRY AGAIN NEXT MONTH", bg="red", padx=30, pady=20,
                             width=14, height=10)
            label.place(x=1200, y=560)

        # table
        self.table = ["Date", "Transaction", "Income", "Expense", "Balance"]
        self.op_table = ttk.Treeview(self.root5, column=self.table, show="headings", height=15)
        for i in self.table:
            self.op_table.heading(i, text=i.title())
        self.op_table.place(x=380, y=150)

        # show table
        with open("./user_data/trans_ls.txt", "r") as self.readtable:
            for line in self.readtable:
                self.data = line.strip("\n").split()
                if self.data[0].split("/")[0] == "2":
                    if self.data[-1] == "income":
                        self.op_table.insert("", 'end', values=self.data[0:3])
                    elif self.data[-1] == "expense":
                        render_data = self.data[0:2] + [" ", self.data[2]]
                        self.op_table.insert("", 'end', values=render_data)
            self.readtable.close()

        # graph
        self.food = 0
        self.trans = 0
        self.cloth = 0
        self.mis = 0
        self.health = 0
        self.data_new = {}
        with open("./user_data/trans_ls.txt", "r") as self.fr:
            for line in self.fr:
                self.data = line.strip("\n").split()
                if self.data[0].split("/")[0] == "2":
                    if self.data[3] == "Food":
                        self.food += int(self.data[2])
                    elif self.data[3] == "Transportation":
                        self.trans += int(self.data[2])
                    elif self.data[3] == "clothing":
                        self.cloth += int(self.data[2])
                    elif self.data[3] == "Miscellaneous":
                        self.mis += int(self.data[2])
                    elif self.data[3] == "Healthcare":
                        self.health += int(self.data[2])
        self.data_new["Category"] = ["Food", "Transportation", "Clothing", "Miscellaneous", "Healthcare"]
        self.data_new["Expense"] = [self.food, self.trans, self.cloth, self.mis, self.health]

        self.df = DataFrame(self.data_new, columns=["Category", "Expense"])

        self.figure1 = plt.Figure(figsize=(10, 4.8), dpi=100)
        self.ax1 = self.figure1.add_subplot(111)
        self.bar = FigureCanvasTkAgg(self.figure1, self.root5)
        self.bar.get_tk_widget().place(x=380, y=440)
        self.df = self.df[["Category", "Expense"]].groupby("Category").sum()
        self.df.plot(kind="bar", legend=True, ax=self.ax1, rot=0)
        self.ax1.set_title('Monthly Expense by Category')

        # call app
        self.root5.mainloop()

    @staticmethod
    def years():
        messagebox.showinfo("ERROR", "No Data Found")

    def daily(self):
        self.root5.destroy()
        ds.Screen()

    def overall(self):
        self.root5.destroy()
        ms.Screen()

    def jan(self):
        self.root5.destroy()
        Jan.Screen()

    def mar(self):
        self.root5.destroy()
        Mar.Screen()

    def apr(self):
        self.root5.destroy()
        Apr.Screen()

    def may(self):
        self.root5.destroy()
        May.Screen()

    def jun(self):
        self.root5.destroy()
        Jun.Screen()

    def jul(self):
        self.root5.destroy()
        Jul.Screen()

    def aug(self):
        self.root5.destroy()
        Aug.Screen()

    def sep(self):
        self.root5.destroy()
        Sep.Screen()

    def oct(self):
        self.root5.destroy()
        Oct.Screen()

    def nov(self):
        self.root5.destroy()
        Nov.Screen()

    def dec(self):
        self.root5.destroy()
        Dec.Screen()
