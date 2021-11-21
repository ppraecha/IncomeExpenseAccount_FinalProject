import tkinter as tk
import daily_screen as ds
import uni_save


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
        self.overall_button = tk.Button(self.root3, text="Overall", padx=100, pady=10, borderwidth=30)
        self.overall_button.place(x=200, y=150)
        self.jan_button = tk.Button(self.root3, text="January", padx=97, pady=10, borderwidth=30)
        self.jan_button.place(x=200, y=190)
        self.feb_button = tk.Button(self.root3, text="February", padx=94, pady=10, borderwidth=30)
        self.feb_button.place(x=200, y=230)
        self.mar_button = tk.Button(self.root3, text="March", padx=102, pady=10, borderwidth=30)
        self.mar_button.place(x=200, y=270)
        self.apr_button = tk.Button(self.root3, text="April", padx=108, pady=10, borderwidth=30)
        self.apr_button.place(x=200, y=310)
        self.may_button = tk.Button(self.root3, text="May", padx=109, pady=10, borderwidth=30)
        self.may_button.place(x=200, y=350)
        self.jun_button = tk.Button(self.root3, text="June", padx=107, pady=10, borderwidth=30)
        self.jun_button.place(x=200, y=390)
        self.jul_button = tk.Button(self.root3, text="July", padx=110, pady=10, borderwidth=30)
        self.jul_button.place(x=200, y=430)
        self.aug_button = tk.Button(self.root3, text="August", padx=102, pady=10, borderwidth=30)
        self.aug_button.place(x=200, y=470)
        self.sep_button = tk.Button(self.root3, text="September", padx=90, pady=10, borderwidth=30)
        self.sep_button.place(x=200, y=510)
        self.oct_button = tk.Button(self.root3, text="October", padx=99, pady=10, borderwidth=30)
        self.oct_button.place(x=200, y=550)
        self.nov_button = tk.Button(self.root3, text="November", padx=93, pady=10, borderwidth=30)
        self.nov_button.place(x=200, y=590)
        self.dec_button = tk.Button(self.root3, text="December", padx=93, pady=10, borderwidth=30)
        self.dec_button.place(x=200, y=630)
        # year push button
        self.year_2021 = tk.Button(self.root3, text="2021", padx=20, pady=10, borderwidth=30)
        self.year_2021.place(x=200, y=100)
        self.year_2020 = tk.Button(self.root3, text="2020", padx=20, pady=10, borderwidth=30)
        self.year_2020.place(x=290, y=100)
        self.year_2019 = tk.Button(self.root3, text="2019", padx=20, pady=10, borderwidth=30)
        self.year_2019.place(x=380, y=100)
        self.year_2018 = tk.Button(self.root3, text="2018", padx=20, pady=10, borderwidth=30)
        self.year_2018.place(x=470, y=100)
        self.year_2017 = tk.Button(self.root3, text="2017", padx=20, pady=10, borderwidth=30)
        self.year_2017.place(x=560, y=100)
        self.year_2016 = tk.Button(self.root3, text="2016", padx=20, pady=10, borderwidth=30)
        self.year_2016.place(x=650, y=100)
        self.year_2015 = tk.Button(self.root3, text="2015", padx=20, pady=10, borderwidth=30)
        self.year_2015.place(x=740, y=100)
        self.year_2014 = tk.Button(self.root3, text="2014", padx=20, pady=10, borderwidth=30)
        self.year_2014.place(x=830, y=100)
        self.year_2013 = tk.Button(self.root3, text="2013", padx=20, pady=10, borderwidth=30)
        self.year_2013.place(x=920, y=100)
        self.year_2012 = tk.Button(self.root3, text="2012", padx=20, pady=10, borderwidth=30)
        self.year_2012.place(x=1010, y=100)
        self.year_2011 = tk.Button(self.root3, text="2011", padx=20, pady=10, borderwidth=30)
        self.year_2011.place(x=1100, y=100)
        self.year_2010 = tk.Button(self.root3, text="2010", padx=20, pady=10, borderwidth=30)
        self.year_2010.place(x=1190, y=100)
        # input
        self.new_data = uni_save.load_data("./user_data/cal.json")
        self.target = tk.Label(self.root3, text=self.new_data["monthly"])
        self.target.place(x=300, y=700)

        self.tol_save = tk.Label(self.root3, text="Total Saving:")
        self.tol_save.place(x=200, y=700)
        # call app
        self.root3.mainloop()

    def daily(self):
        self.root3.destroy()
        ds.Screen()
