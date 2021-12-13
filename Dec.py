import tkinter as tk
import daily_screen as ds
import uni_save
import monthly_screen as ms
from tkinter import messagebox
from tkinter import ttk
import Jan as jan
import Feb as feb
import Mar as mar
import Apr as apr
import May as may
import Jun as jun
import Jul as jul
import Aug as aug
import Sep as sep
import Oct as oct
import Nov as nov
import matplotlib.pyplot as plt
import csv


class Screen:
    def __init__(self):
        # set up page
        self.root15 = tk.Tk()
        self.root15.title("HAPPY RICHIES")
        self.root15.geometry("1500x1000")
        # push button
        self.daily_button = tk.Button(self.root15, text="Daily", padx=150, pady=10, borderwidth=30, command=self.daily)
        self.daily_button.place(x=200, y=50)
        self.monthly_button = tk.Button(self.root15, text="Monthly", padx=150, pady=10, borderwidth=30,
                                        command=self.overall)
        self.monthly_button.place(x=900, y=50)
        # moth push button
        self.overall_button = tk.Button(self.root15, text="Overall", padx=50, pady=10, borderwidth=30,
                                        command=self.overall)
        self.overall_button.place(x=200, y=150)
        self.jan_button = tk.Button(self.root15, text="January", padx=47, pady=10, borderwidth=30, command=self.Jan)
        self.jan_button.place(x=200, y=190)
        self.feb_button = tk.Button(self.root15, text="February", padx=44, pady=10, borderwidth=30, command=self.Feb)
        self.feb_button.place(x=200, y=230)
        self.mar_button = tk.Button(self.root15, text="March", padx=52, pady=10, borderwidth=30, command=self.Mar)
        self.mar_button.place(x=200, y=270)
        self.apr_button = tk.Button(self.root15, text="April", padx=58, pady=10, borderwidth=30, command=self.Apr)
        self.apr_button.place(x=200, y=310)
        self.may_button = tk.Button(self.root15, text="May", padx=59, pady=10, borderwidth=30, command=self.May)
        self.may_button.place(x=200, y=350)
        self.jun_button = tk.Button(self.root15, text="June", padx=57, pady=10, borderwidth=30, command=self.Jun)
        self.jun_button.place(x=200, y=390)
        self.jul_button = tk.Button(self.root15, text="July", padx=60, pady=10, borderwidth=30, command=self.Jul)
        self.jul_button.place(x=200, y=430)
        self.aug_button = tk.Button(self.root15, text="August", padx=52, pady=10, borderwidth=30, command=self.Aug)
        self.aug_button.place(x=200, y=470)
        self.sep_button = tk.Button(self.root15, text="September", padx=39, pady=10, borderwidth=30, command=self.Sep)
        self.sep_button.place(x=200, y=510)
        self.oct_button = tk.Button(self.root15, text="October", padx=48, pady=10, borderwidth=30, command=self.Oct)
        self.oct_button.place(x=200, y=550)
        self.nov_button = tk.Button(self.root15, text="November", padx=42, pady=10, borderwidth=30, command=self.Nov)
        self.nov_button.place(x=200, y=590)
        self.dec_button = tk.Button(self.root15, text="December", padx=42, pady=10, borderwidth=30)
        self.dec_button.place(x=200, y=630)
        # year push button
        self.year_2021 = tk.Button(self.root15, text="2021", padx=20, pady=10, borderwidth=30, command=self.overall)
        self.year_2021.place(x=200, y=100)
        self.year_2020 = tk.Button(self.root15, text="2020", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2020.place(x=290, y=100)
        self.year_2019 = tk.Button(self.root15, text="2019", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2019.place(x=380, y=100)
        self.year_2018 = tk.Button(self.root15, text="2018", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2018.place(x=470, y=100)
        self.year_2017 = tk.Button(self.root15, text="2017", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2017.place(x=560, y=100)
        self.year_2016 = tk.Button(self.root15, text="2016", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2016.place(x=650, y=100)
        self.year_2015 = tk.Button(self.root15, text="2015", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2015.place(x=740, y=100)
        self.year_2014 = tk.Button(self.root15, text="2014", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2014.place(x=830, y=100)
        self.year_2013 = tk.Button(self.root15, text="2013", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2013.place(x=920, y=100)
        self.year_2012 = tk.Button(self.root15, text="2012", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2012.place(x=1010, y=100)
        self.year_2011 = tk.Button(self.root15, text="2011", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2011.place(x=1100, y=100)
        self.year_2010 = tk.Button(self.root15, text="2010", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2010.place(x=1190, y=100)
        # input saving

        # input target save
        self.new_data = uni_save.load_data("./user_data/cal.json")
        self.target = tk.Label(self.root15, text=self.new_data["monthly"])
        self.target.place(x=1300, y=700)
        self.target_save = tk.Label(self.root15, text="Target Saving:")
        self.target_save.place(x=1200, y=700)

        # table
        self.table = ["Date", "Transaction", "Income", "Expense", "Balance"]
        self.op_table = ttk.Treeview(self.root15, column=self.table, show="headings", height=15)
        for i in self.table:
            self.op_table.heading(i, text=i.title())
        self.op_table.place(x=380, y=150)

        # call app
        self.root15.mainloop()

    # def graph(self):
    #     with open("./user_data/trans_ls.txt", "r") as fr:

    def table(self):
        with open("./user_data/trans_ls.txt", "r") as readtable:
            for line in readtable:
                if line[0] == "12":
                    print(line)
            readtable.close()

    def years(self):
        messagebox.showinfo("ERROR", "No Data Found")
        exit(0)

    def daily(self):
        self.root15.destroy()
        ds.Screen()

    def overall(self):
        self.root15.destroy()
        ms.Screen()

    def Jan(self):
        self.root15.destroy()
        jan.Screen()

    def Feb(self):
        self.root15.destroy()
        feb.Screen()

    def Mar(self):
        self.root15.destroy()
        mar.Screen()

    def Apr(self):
        self.root15.destroy()
        apr.Screen()

    def May(self):
        self.root15.destroy()
        may.Screen()

    def Jun(self):
        self.root15.destroy()
        jun.Screen()

    def Jul(self):
        self.root15.destroy()
        jul.Screen()

    def Aug(self):
        self.root15.destroy()
        aug.Screen()

    def Sep(self):
        self.root15.destroy()
        sep.Screen()

    def Oct(self):
        self.root15.destroy()
        oct.Screen()

    def Nov(self):
        self.root15.destroy()
        nov.Screen()
