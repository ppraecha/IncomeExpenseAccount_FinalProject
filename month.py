import tkinter as tk
import daily_screen as ds
import uni_save as us
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Screen:

    def __init__(self, year="21"):
        # set up page
        self.root4 = tk.Tk()
        self.root4.title("HAPPY RICHIES")
        self.root4.geometry("1500x1000")
        self.year = year

        # push button
        self.daily_button = tk.Button(self.root4, text="Daily", padx=150, pady=10, borderwidth=30,
                                      command=self.daily)
        self.daily_button.place(x=200, y=50)
        self.monthly_button = tk.Button(self.root4, text="Monthly", padx=150, pady=10, borderwidth=30)
        self.monthly_button.place(x=900, y=50)

        # month push button
        overall_button = tk.Button(self.root4, text="Overall", padx=50,
                                   pady=10, borderwidth=30, command=lambda: self.overall(self.year))
        overall_button.place(x=200, y=150)
        jan_button = tk.Button(self.root4, text="January", padx=47, pady=10,
                               borderwidth=30, command=lambda: self.change_month("1"))
        jan_button.place(x=200, y=190)
        feb_button = tk.Button(self.root4, text="February", padx=44, pady=10,
                               borderwidth=30, command=lambda: self.change_month("2"))
        feb_button.place(x=200, y=230)
        mar_button = tk.Button(self.root4, text="March", padx=52, pady=10,
                               borderwidth=30, command=lambda: self.change_month("3"))
        mar_button.place(x=200, y=270)
        apr_button = tk.Button(self.root4, text="April", padx=58, pady=10,
                               borderwidth=30, command=lambda: self.change_month("4"))
        apr_button.place(x=200, y=310)
        may_button = tk.Button(self.root4, text="May", padx=59, pady=10,
                               borderwidth=30, command=lambda: self.change_month("5"))
        may_button.place(x=200, y=350)
        jun_button = tk.Button(self.root4, text="June", padx=57, pady=10,
                               borderwidth=30, command=lambda: self.change_month("6"))
        jun_button.place(x=200, y=390)
        jul_button = tk.Button(self.root4, text="July", padx=60, pady=10,
                               borderwidth=30, command=lambda: self.change_month("7"))
        jul_button.place(x=200, y=430)
        aug_button = tk.Button(self.root4, text="August", padx=51, pady=10,
                               borderwidth=30, command=lambda: self.change_month("8"))
        aug_button.place(x=200, y=470)
        sep_button = tk.Button(self.root4, text="September", padx=39, pady=10,
                               borderwidth=30, command=lambda: self.change_month("9"))
        sep_button.place(x=200, y=510)
        oct_button = tk.Button(self.root4, text="October", padx=48, pady=10,
                               borderwidth=30, command=lambda: self.change_month("10"))
        oct_button.place(x=200, y=550)
        nov_button = tk.Button(self.root4, text="November", padx=42, pady=10,
                               borderwidth=30, command=lambda: self.change_month("11"))
        nov_button.place(x=200, y=590)
        dec_button = tk.Button(self.root4, text="December", padx=42, pady=10,
                               borderwidth=30, command=lambda: self.change_month("12"))
        dec_button.place(x=200, y=630)

        # year push button
        year_2021 = tk.Button(self.root4, text="2021", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("21"))
        year_2021.place(x=200, y=100)
        year_2020 = tk.Button(self.root4, text="2020", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("20"))
        year_2020.place(x=290, y=100)
        year_2019 = tk.Button(self.root4, text="2019", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("19"))
        year_2019.place(x=380, y=100)
        year_2018 = tk.Button(self.root4, text="2018", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("18"))
        year_2018.place(x=470, y=100)
        year_2017 = tk.Button(self.root4, text="2017", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("17"))
        year_2017.place(x=560, y=100)
        year_2016 = tk.Button(self.root4, text="2016", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("16"))
        year_2016.place(x=650, y=100)
        year_2015 = tk.Button(self.root4, text="2015", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("15"))
        year_2015.place(x=740, y=100)
        year_2014 = tk.Button(self.root4, text="2014", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("14"))
        year_2014.place(x=830, y=100)
        year_2013 = tk.Button(self.root4, text="2013", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("13"))
        year_2013.place(x=920, y=100)
        year_2012 = tk.Button(self.root4, text="2012", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("12"))
        year_2012.place(x=1010, y=100)
        year_2011 = tk.Button(self.root4, text="2011", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("11"))
        year_2011.place(x=1100, y=100)
        year_2010 = tk.Button(self.root4, text="2010", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("10"))
        year_2010.place(x=1190, y=100)

        # input
        total = 0
        data = us.load_data("./user_data/balance.json")
        for line in data:
            total += data[line]
        target = tk.Label(self.root4, text=total)
        target.place(x=300, y=700)
        tol_save = tk.Label(self.root4, text="Total Saving:")
        tol_save.place(x=200, y=700)

        # graph
        data_new = {}
        line_ls = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        save = []
        data = us.load_data("./user_data/balance.json")
        for line in data:
            if line.split("/")[1] == self.year:
                save.append(int(data[line]))
        if not save:
            return
        data_new["Month"] = line_ls
        data_new["Saving"] = save

        df = DataFrame(data_new, columns=["Month", "Saving"])

        figure1 = plt.Figure(figsize=(14, 8), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar = FigureCanvasTkAgg(figure1, self.root4)
        bar.get_tk_widget().place(x=360, y=150)
        df = df[["Month", "Saving"]].groupby("Month").sum().reindex(line_ls)
        df.plot(kind="bar", ax=ax1)
        ax1.set_title('Saving per Month')

        # call app
        self.root4.mainloop()

        # messagebox.showinfo("ERROR", "No Data Found")

    def daily(self):
        self.root4.destroy()
        ds.Screen()

    def overall(self, year):
        self.root4.destroy()
        Screen(year)

    def change_month(self, month):
        self.root4.destroy()

        # setup page
        self.root4 = tk.Tk()
        self.root4.title("HAPPY RICHIES")
        self.root4.geometry("1500x1000")

        # push button
        daily_button = tk.Button(self.root4, text="Daily", padx=150, pady=10, borderwidth=30, command=self.daily)
        daily_button.place(x=200, y=50)
        monthly_button = tk.Button(self.root4, text="Monthly", padx=150, pady=10,
                                   borderwidth=30, command=lambda: self.overall(self.year))
        monthly_button.place(x=900, y=50)

        # month push button
        overall_button = tk.Button(self.root4, text="Overall", padx=50, pady=10,
                                   borderwidth=30, command=lambda: self.overall(self.year))
        overall_button.place(x=200, y=150)
        jan_button = tk.Button(self.root4, text="January", padx=47, pady=10,
                               borderwidth=30, command=lambda: self.change_month("1"))
        jan_button.place(x=200, y=190)
        feb_button = tk.Button(self.root4, text="February", padx=44, pady=10,
                               borderwidth=30, command=lambda: self.change_month("2"))
        feb_button.place(x=200, y=230)
        mar_button = tk.Button(self.root4, text="March", padx=52, pady=10,
                               borderwidth=30, command=lambda: self.change_month("3"))
        mar_button.place(x=200, y=270)
        apr_button = tk.Button(self.root4, text="April", padx=58, pady=10,
                               borderwidth=30, command=lambda: self.change_month("4"))
        apr_button.place(x=200, y=310)
        may_button = tk.Button(self.root4, text="May", padx=59, pady=10,
                               borderwidth=30, command=lambda: self.change_month("5"))
        may_button.place(x=200, y=350)
        jun_button = tk.Button(self.root4, text="June", padx=57, pady=10,
                               borderwidth=30, command=lambda: self.change_month("6"))
        jun_button.place(x=200, y=390)
        jul_button = tk.Button(self.root4, text="July", padx=60, pady=10,
                               borderwidth=30, command=lambda: self.change_month("7"))
        jul_button.place(x=200, y=430)
        aug_button = tk.Button(self.root4, text="August", padx=51, pady=10,
                               borderwidth=30, command=lambda: self.change_month("8"))
        aug_button.place(x=200, y=470)
        sep_button = tk.Button(self.root4, text="September", padx=39, pady=10,
                               borderwidth=30, command=lambda: self.change_month("9"))
        sep_button.place(x=200, y=510)
        oct_button = tk.Button(self.root4, text="October", padx=48, pady=10,
                               borderwidth=30, command=lambda: self.change_month("10"))
        oct_button.place(x=200, y=550)
        nov_button = tk.Button(self.root4, text="November", padx=42, pady=10,
                               borderwidth=30, command=lambda: self.change_month("11"))
        nov_button.place(x=200, y=590)
        dec_button = tk.Button(self.root4, text="December", padx=42, pady=10,
                               borderwidth=30, command=lambda: self.change_month("12"))
        dec_button.place(x=200, y=630)

        # year push button
        year_2021 = tk.Button(self.root4, text="2021", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("21"))
        year_2021.place(x=200, y=100)
        year_2020 = tk.Button(self.root4, text="2020", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("20"))
        year_2020.place(x=290, y=100)
        year_2019 = tk.Button(self.root4, text="2019", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("19"))
        year_2019.place(x=380, y=100)
        year_2018 = tk.Button(self.root4, text="2018", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("18"))
        year_2018.place(x=470, y=100)
        year_2017 = tk.Button(self.root4, text="2017", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("17"))
        year_2017.place(x=560, y=100)
        year_2016 = tk.Button(self.root4, text="2016", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("16"))
        year_2016.place(x=650, y=100)
        year_2015 = tk.Button(self.root4, text="2015", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("15"))
        year_2015.place(x=740, y=100)
        year_2014 = tk.Button(self.root4, text="2014", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("14"))
        year_2014.place(x=830, y=100)
        year_2013 = tk.Button(self.root4, text="2013", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("13"))
        year_2013.place(x=920, y=100)
        year_2012 = tk.Button(self.root4, text="2012", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("12"))
        year_2012.place(x=1010, y=100)
        year_2011 = tk.Button(self.root4, text="2011", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("11"))
        year_2011.place(x=1100, y=100)
        year_2010 = tk.Button(self.root4, text="2010", padx=20, pady=10,
                              borderwidth=30, command=lambda: self.overall("10"))
        year_2010.place(x=1190, y=100)

        # input saving
        data = us.load_data("./user_data/balance.json")
        month_years = month + "/" + self.year
        if month_years not in data:
            messagebox.showinfo("ERROR", "No Data Found")
            return

        save = tk.Label(self.root4, text=data[month_years])
        save.place(x=1300, y=480)
        save_label = tk.Label(self.root4, text="Saving:")
        save_label.place(x=1200, y=480)

        # input target save
        new_data = us.load_data("./user_data/cal.json")
        target = tk.Label(self.root4, text=new_data["monthly"])
        target.place(x=1300, y=500)
        target_save = tk.Label(self.root4, text="Target Saving:")
        target_save.place(x=1200, y=500)

        # input Differences
        minus = int(data[month_years]) - int(new_data["monthly"])
        minus_show = tk.Label(self.root4, text=minus)
        minus_show.place(x=1300, y=530)
        dif_save = tk.Label(self.root4, text="Differences:")
        dif_save.place(x=1200, y=530)

        # show congrats
        if data[month_years] > new_data["monthly"]:
            label = tk.Label(self.root4, text=" ☻ Congratulation!" + "\n" + "GOOD JOB for this month!",
                             bg="green", padx=30, pady=20, width=14, height=10)
            label.place(x=1200, y=560)
        else:
            label = tk.Label(self.root4, text=" ☹ Please" + "\n" + "TRY AGAIN NEXT MONTH",
                             bg="red", padx=30, pady=20, width=14, height=10)
            label.place(x=1200, y=560)

        # table
        table = ["Date", "Transaction", "Income", "Expense", "Balance"]
        op_table = ttk.Treeview(self.root4, column=table, show="headings", height=15)
        for i in table:
            op_table.heading(i, text=i.title())
        op_table.place(x=380, y=150)

        # show table
        with open("./user_data/trans_ls.txt", "r") as readtable:
            for line in readtable:
                data = line.strip("\n").split()
                if data[0].split("/")[0] == month:
                    if data[-1] == "income":
                        op_table.insert("", 'end', values=data[0:3])
                    elif data[-1] == "expense":
                        render_data = data[0:2] + [" ", data[2]]
                        op_table.insert("", 'end', values=render_data)
            readtable.close()

        # graph
        food = 0
        trans = 0
        cloth = 0
        mis = 0
        health = 0
        data_new = {}
        with open("./user_data/trans_ls.txt", "r") as fr:
            for line in fr:
                data = line.strip("\n").split()
                if data[0].split("/")[0] == month:
                    if data[3] == "Food":
                        food += int(data[2])
                    elif data[3] == "Transportation":
                        trans += int(data[2])
                    elif data[3] == "clothing":
                        cloth += int(data[2])
                    elif data[3] == "Miscellaneous":
                        mis += int(data[2])
                    elif data[3] == "Healthcare":
                        health += int(data[2])
        data_new["Category"] = ["Food", "Transportation", "Clothing", "Miscellaneous", "Healthcare"]
        data_new["Expense"] = [food, trans, cloth, mis, health]

        df = DataFrame(data_new, columns=["Category", "Expense"])

        figure1 = plt.Figure(figsize=(10, 4.8), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar = FigureCanvasTkAgg(figure1, self.root4)
        bar.get_tk_widget().place(x=380, y=440)
        df = df[["Category", "Expense"]].groupby("Category").sum()
        df.plot(kind="bar", legend=True, ax=ax1, rot=0)
        ax1.set_title('Monthly Expense by Category')
