import tkinter as tk
import daily_screen as ds
import uni_save as us
from tkinter import messagebox
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
import Dec as dec


class Screen:
    def __init__(self):
        # set up page
        self.root3 = tk.Tk()
        self.root3.title("HAPPY RICHIES")
        self.root3.geometry("1500x1000")

        # push button
        self.daily_button = tk.Button(self.root3, text="Daily", padx=150, pady=10, borderwidth=30, command=self.daily)
        self.daily_button.place(x=200, y=50)
        self.monthly_button = tk.Button(self.root3, text="Monthly", padx=150, pady=10, borderwidth=30)
        self.monthly_button.place(x=900, y=50)

        # moth push button
        self.overall_button = tk.Button(self.root3, text="Overall", padx=50, pady=10, borderwidth=30)
        self.overall_button.place(x=200, y=150)
        self.jan_button = tk.Button(self.root3, text="January", padx=47, pady=10, borderwidth=30, command=self.Jan)
        self.jan_button.place(x=200, y=190)
        self.feb_button = tk.Button(self.root3, text="February", padx=44, pady=10, borderwidth=30, command=self.Feb)
        self.feb_button.place(x=200, y=230)
        self.mar_button = tk.Button(self.root3, text="March", padx=52, pady=10, borderwidth=30, command=self.Mar)
        self.mar_button.place(x=200, y=270)
        self.apr_button = tk.Button(self.root3, text="April", padx=58, pady=10, borderwidth=30, command=self.Apr)
        self.apr_button.place(x=200, y=310)
        self.may_button = tk.Button(self.root3, text="May", padx=59, pady=10, borderwidth=30, command=self.May)
        self.may_button.place(x=200, y=350)
        self.jun_button = tk.Button(self.root3, text="June", padx=57, pady=10, borderwidth=30, command=self.Jun)
        self.jun_button.place(x=200, y=390)
        self.jul_button = tk.Button(self.root3, text="July", padx=60, pady=10, borderwidth=30, command=self.Jul)
        self.jul_button.place(x=200, y=430)
        self.aug_button = tk.Button(self.root3, text="August", padx=51, pady=10, borderwidth=30, command=self.Aug)
        self.aug_button.place(x=200, y=470)
        self.sep_button = tk.Button(self.root3, text="September", padx=39, pady=10, borderwidth=30, command=self.Sep)
        self.sep_button.place(x=200, y=510)
        self.oct_button = tk.Button(self.root3, text="October", padx=48, pady=10, borderwidth=30, command=self.Oct)
        self.oct_button.place(x=200, y=550)
        self.nov_button = tk.Button(self.root3, text="November", padx=42, pady=10, borderwidth=30, command=self.Nov)
        self.nov_button.place(x=200, y=590)
        self.dec_button = tk.Button(self.root3, text="December", padx=42, pady=10, borderwidth=30, command=self.Dec)
        self.dec_button.place(x=200, y=630)

        # year push button
        self.year_2021 = tk.Button(self.root3, text="2021", padx=20, pady=10, borderwidth=30)
        self.year_2021.place(x=200, y=100)
        self.year_2020 = tk.Button(self.root3, text="2020", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2020.place(x=290, y=100)
        self.year_2019 = tk.Button(self.root3, text="2019", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2019.place(x=380, y=100)
        self.year_2018 = tk.Button(self.root3, text="2018", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2018.place(x=470, y=100)
        self.year_2017 = tk.Button(self.root3, text="2017", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2017.place(x=560, y=100)
        self.year_2016 = tk.Button(self.root3, text="2016", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2016.place(x=650, y=100)
        self.year_2015 = tk.Button(self.root3, text="2015", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2015.place(x=740, y=100)
        self.year_2014 = tk.Button(self.root3, text="2014", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2014.place(x=830, y=100)
        self.year_2013 = tk.Button(self.root3, text="2013", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2013.place(x=920, y=100)
        self.year_2012 = tk.Button(self.root3, text="2012", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2012.place(x=1010, y=100)
        self.year_2011 = tk.Button(self.root3, text="2011", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2011.place(x=1100, y=100)
        self.year_2010 = tk.Button(self.root3, text="2010", padx=20, pady=10, borderwidth=30, command=self.years)
        self.year_2010.place(x=1190, y=100)

        # input
        self.total = 0
        self.data = us.load_data("./user_data/balance.json")
        for line in self.data:
            self.total += self.data[line]
        self.target = tk.Label(self.root3, text=self.total)
        self.target.place(x=300, y=700)
        self.tol_save = tk.Label(self.root3, text="Total Saving:")
        self.tol_save.place(x=200, y=700)

        # graph
        self.data_new = {}
        self.line_ls = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.save = []
        self.data = us.load_data("./user_data/balance.json")
        for line in self.data:
            self.save.append(int(self.data[line]))
        self.data_new["Month"] = self.line_ls
        self.data_new["Saving"] = self.save

        self.df = DataFrame.sort_index(self.data_new, columns=["Month", "Saving"])

        self.figure1 = plt.Figure(figsize=(14, 8), dpi=100)
        self.ax1 = self.figure1.add_subplot(111)
        self.bar = FigureCanvasTkAgg(self.figure1, self.root3)
        self.bar.get_tk_widget().place(x=360, y=150)
        self.df = self.df[["Month", "Saving"]].groupby("Month").sum()
        self.df.plot(kind="bar", legend=True, ax=self.ax1)
        self.ax1.set_title('Saving per Month')

        # call app
        self.root3.mainloop()

    def years(self):
        messagebox.showinfo("ERROR", "No Data Found")
        exit(0)

    def daily(self):
        self.root3.destroy()
        ds.Screen()

    def Jan(self):
        self.root3.destroy()
        jan.Screen()

    def Feb(self):
        self.root3.destroy()
        feb.Screen()

    def Mar(self):
        self.root3.destroy()
        mar.Screen()

    def Apr(self):
        self.root3.destroy()
        apr.Screen()

    def May(self):
        self.root3.destroy()
        may.Screen()

    def Jun(self):
        self.root3.destroy()
        jun.Screen()

    def Jul(self):
        self.root3.destroy()
        jul.Screen()

    def Aug(self):
        self.root3.destroy()
        aug.Screen()

    def Sep(self):
        self.root3.destroy()
        sep.Screen()

    def Oct(self):
        self.root3.destroy()
        oct.Screen()

    def Nov(self):
        self.root3.destroy()
        nov.Screen()

    def Dec(self):
        self.root3.destroy()
        dec.Screen()





