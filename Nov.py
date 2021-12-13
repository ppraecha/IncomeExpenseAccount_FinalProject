import tkinter as tk
import daily_screen as ds
import uni_save
import monthly_screen as ms
from tkinter import messagebox
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
import Dec as dec
import matplotlib.pyplot as plt
import csv


class Screen:
    def __init__(self):
        # set up page
        self.root14 = tk.Tk()
        self.root14.title("HAPPY RICHIES")
        self.root14.geometry("1500x1000")
        # push button
        self.daily_button = tk.Button(self.root14, text="Daily", padx=150, pady=10, borderwidth=30, command=self.daily)
        self.daily_button.place(x=200, y=50)
        self.monthly_button = tk.Button(self.root14, text="Monthly", padx=150, pady=10, borderwidth=30,
                                        command=self.overall)
        self.monthly_button.place(x=900, y=50)
        # moth push button
        self.overall_button = tk.Button(self.root14, text="Overall", padx=100, pady=10, borderwidth=30,
                                        command=self.overall)
        self.overall_button.place(x=200, y=150)
        self.jan_button = tk.Button(self.root14, text="January", padx=97, pady=10, borderwidth=30, command=self.Jan)
        self.jan_button.place(x=200, y=190)
        self.feb_button = tk.Button(self.root14, text="February", padx=94, pady=10, borderwidth=30, command=self.Feb)
        self.feb_button.place(x=200, y=230)
        self.mar_button = tk.Button(self.root14, text="March", padx=102, pady=10, borderwidth=30, command=self.Mar)
        self.mar_button.place(x=200, y=270)
        self.apr_button = tk.Button(self.root14, text="April", padx=108, pady=10, borderwidth=30, command=self.Apr)
        self.apr_button.place(x=200, y=310)
        self.may_button = tk.Button(self.root14, text="May", padx=109, pady=10, borderwidth=30, command=self.May)
        self.may_button.place(x=200, y=350)
        self.jun_button = tk.Button(self.root14, text="June", padx=107, pady=10, borderwidth=30, command=self.Jun)
        self.jun_button.place(x=200, y=390)
        self.jul_button = tk.Button(self.root14, text="July", padx=110, pady=10, borderwidth=30, command=self.Jul)
        self.jul_button.place(x=200, y=430)
        self.aug_button = tk.Button(self.root14, text="August", padx=102, pady=10, borderwidth=30, command=self.Aug)
        self.aug_button.place(x=200, y=470)
        self.sep_button = tk.Button(self.root14, text="September", padx=90, pady=10, borderwidth=30, command=self.Sep)
        self.sep_button.place(x=200, y=510)
        self.oct_button = tk.Button(self.root14, text="October", padx=99, pady=10, borderwidth=30, command=self.Oct)
        self.oct_button.place(x=200, y=550)
        self.nov_button = tk.Button(self.root14, text="November", padx=93, pady=10, borderwidth=30)
        self.nov_button.place(x=200, y=590)
        self.dec_button = tk.Button(self.root14, text="December", padx=93, pady=10, borderwidth=30, command=self.Dec)
        self.dec_button.place(x=200, y=630)
        # year push button
        self.year_2021 = tk.Button(self.root14, text="2021", padx=20, pady=10, borderwidth=30, command=self.overall)
        self.year_2021.place(x=200, y=100)
        self.year_2020 = tk.Button(self.root14, text="2020", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2020.place(x=290, y=100)
        self.year_2019 = tk.Button(self.root14, text="2019", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2019.place(x=380, y=100)
        self.year_2018 = tk.Button(self.root14, text="2018", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2018.place(x=470, y=100)
        self.year_2017 = tk.Button(self.root14, text="2017", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2017.place(x=560, y=100)
        self.year_2016 = tk.Button(self.root14, text="2016", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2016.place(x=650, y=100)
        self.year_2015 = tk.Button(self.root14, text="2015", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2015.place(x=740, y=100)
        self.year_2014 = tk.Button(self.root14, text="2014", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2014.place(x=830, y=100)
        self.year_2013 = tk.Button(self.root14, text="2013", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2013.place(x=920, y=100)
        self.year_2012 = tk.Button(self.root14, text="2012", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2012.place(x=1010, y=100)
        self.year_2011 = tk.Button(self.root14, text="2011", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2011.place(x=1100, y=100)
        self.year_2010 = tk.Button(self.root14, text="2010", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2010.place(x=1190, y=100)
        # input saving

        # input target save
        self.new_data = uni_save.load_data("./user_data/cal.json")
        self.target = tk.Label(self.root14, text=self.new_data["monthly"])
        self.target.place(x=1300, y=700)
        self.target_save = tk.Label(self.root14, text="Target Saving:")
        self.target_save.place(x=1200, y=700)

        # table
        self.table = ["Date", "Transaction", "Income", "Expense", "Balance"]
        self.op_table = ttk.Treeview(self.root14, column=self.table, show="headings", height=15)
        for i in self.table:
            self.op_table.heading(i, text=i.title())
        self.op_table.place(x=380, y=150)

        # call app
        self.root14.mainloop()

    # def graph(self):
    #     with open("./user_data/trans_ls.txt", "r") as fr:

    def table(self):
        with open("./user_data/trans_ls.txt", "r") as readtable:
            for line in readtable:
                if line[0] == "11":
                    print(line)
            readtable.close()

    def years(self):
        messagebox.showinfo("ERROR", "No Data Found")
        exit(0)

    def daily(self):
        self.root14.destroy()
        ds.Screen()

    def overall(self):
        self.root14.destroy()
        ms.Screen()

    def Jan(self):
        self.root14.destroy()
        jan.Screen()

    def Feb(self):
        self.root14.destroy()
        feb.Screen()

    def Mar(self):
        self.root14.destroy()
        mar.Screen()

    def Apr(self):
        self.root14.destroy()
        apr.Screen()

    def May(self):
        self.root14.destroy()
        may.Screen()

    def Jun(self):
        self.root14.destroy()
        jun.Screen()

    def Jul(self):
        self.root14.destroy()
        jul.Screen()

    def Aug(self):
        self.root14.destroy()
        aug.Screen()

    def Sep(self):
        self.root14.destroy()
        sep.Screen()

    def Oct(self):
        self.root14.destroy()
        oct.Screen()

    def Dec(self):
        self.root14.destroy()
        dec.Screen()