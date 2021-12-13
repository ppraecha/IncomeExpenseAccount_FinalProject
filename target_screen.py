import tkinter as tk
from tkinter import messagebox
import daily_screen as ds
import uni_save
import monthly_screen as ms


class Screen:
    def __init__(self):
        # set up page
        self.root1 = tk.Tk()
        self.root1.title("HAPPY RICHIES")
        self.root1.geometry("1500x1000")
        # push button
        self.daily_button = tk.Button(self.root1, text="Daily", padx=150, pady=10, borderwidth=30, command=self.back)
        self.daily_button.place(x=200, y=50)
        self.monthly_button = tk.Button(self.root1, text="Monthly", padx=150, pady=10, borderwidth=30, command=self.monthly)
        self.monthly_button.place(x=900, y=50)
        self.cal_button = tk.Button(self.root1, text="Calculate", padx=20, pady=5, borderwidth=30, command=lambda:
                                     self.result(self.e1.get(), self.e2.get()))
        self.cal_button.place(x=900, y=340)
        self.back_button = tk.Button(self.root1, text="Back", padx=20, pady=10, borderwidth=30, command=self.back)
        self.back_button.place(x=200, y=400)
        # label
        # input 1
        self.earn = tk.Label(self.root1, text="Monthly earning:")
        self.earn.place(x=500, y=200)
        self.e1 = tk.Entry(self.root1)
        self.e1.place(x=700, y=200)
        # input2
        self.save = tk.Label(self.root1, text="Annually expected saving:")
        self.save.place(x=500, y=230)
        self.e2 = tk.Entry(self.root1)
        self.e2.place(x=700, y=230)
        # output1
        self.month_save = tk.Label(self.root1, text="Monthly saving:")
        self.month_save.place(x=500, y=310)
        self.month_save.configure()
        # output2
        self.day_spend = tk.Label(self.root1, text="Mothly spending:")
        self.day_spend.place(x=500, y=340)
        self.day_spend.configure()
        # call app
        self.root1.mainloop()

    def result(self, a, b):
        try:
            float(a)
            float(b)
            result1 = float(b) // 12
            if result1 > float(a):
                messagebox.showinfo("NOT ENOUGH MONEY", "your income is lower than monthly saving, "
                                                        "please enter new value")
            result2 = (float(a) - result1)
            temp1 = "Monthly saving:" + str(result1)
            temp2 = "Monthly spending:" + str(result2)
            self.month_save.configure(text=temp1)
            self.day_spend.configure(text=temp2)
            dict_data = {"monthly": result1, "daily": result2}
            uni_save.save_data(dict_data, "./user_data/cal.json")
            return result2

        except ValueError:
            messagebox.showinfo("ERROR", "Please fill in NUMBER only")

    def back(self):
        self.root1.destroy()
        ds.Screen()

    def monthly(self):
        self.root1.destroy()
        ms.Screen()




