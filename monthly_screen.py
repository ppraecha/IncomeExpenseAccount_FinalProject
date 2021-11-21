import tkinter as tk


class Screen:
    def __init__(self):
        # set up page
        self.root3 = tk.Tk()
        self.root3.title("HAPPY RICHIES")
        self.root3.geometry("1500x1000")
        # push button
        self.daily_button = tk.Button(self.root3, text="Daily", padx=150, pady=10, borderwidth=30)
        self.daily_button.place(x=200, y=50)
        self.monthly_button = tk.Button(self.root3, text="Monthly", padx=150, pady=10, borderwidth=30)
        self.monthly_button.place(x=900, y=50)
        # moth push button
        self.overall_button = tk.Button(self.root3, text="Overall", padx=100, pady=10, borderwidth=30)
        self.overall_button.place(x=200, y=150)
        self.jan_button = tk.Button(self.root3, text="January", padx=97, pady=10, borderwidth=30)
        self.jan_button.place(x=200, y=190)
        self.feb_button = tk.Button(self.root3, text="February", padx=100, pady=10, borderwidth=30)
        self.feb_button.place(x=200, y=230)
        self.mar_button = tk.Button(self.root3, text="March", padx=100, pady=10, borderwidth=30)
        self.mar_button.place(x=200, y=270)
        self.apr_button = tk.Button(self.root3, text="April", padx=100, pady=10, borderwidth=30)
        self.apr_button.place(x=200, y=310)
        self.may_button = tk.Button(self.root3, text="May", padx=100, pady=10, borderwidth=30)
        self.may_button.place(x=200, y=350)
        self.jun_button = tk.Button(self.root3, text="June", padx=100, pady=10, borderwidth=30)
        self.jun_button.place(x=200, y=390)
        self.jul_button = tk.Button(self.root3, text="July", padx=100, pady=10, borderwidth=30)
        self.jul_button.place(x=200, y=430)
        self.aug_button = tk.Button(self.root3, text="August", padx=100, pady=10, borderwidth=30)
        self.aug_button.place(x=200, y=470)
        self.sep_button = tk.Button(self.root3, text="September", padx=100, pady=10, borderwidth=30)
        self.sep_button.place(x=200, y=510)
        self.oct_button = tk.Button(self.root3, text="October", padx=100, pady=10, borderwidth=30)
        self.oct_button.place(x=200, y=550)
        self.nov_button = tk.Button(self.root3, text="November", padx=100, pady=10, borderwidth=30)
        self.nov_button.place(x=200, y=590)
        self.dec_button = tk.Button(self.root3, text="December", padx=100, pady=10, borderwidth=30)
        self.dec_button.place(x=200, y=630)
        # call app
        self.root3.mainloop()
