import tkinter as tk
from tkinter import *
from tkinter import messagebox


def monthly_save(b):
    global month_save

    try:
        float(b)
    except ValueError:
        messagebox.showinfo("Error", "Please fill in the INTEGERS only")

    result = b//12
    temp = "Monthly saving:" + str(result)
    month_save.configure(text=temp)
    return result


def day_spend(a, c):
    global daily_spend

    try:
        float(a)
    except ValueError:
        messagebox.showinfo("Error", "Please fill in the INTEGERS only")
    try:
        float(c)
    except ValueError:
        messagebox.showinfo("Error", "Please fill in the INTEGERS only")

    result = (a-c)//31
    temp2 = "Daily spending:" + str(result)
    daily_spend.configure(text=temp2)
    return result


def day_page():
    root1.destroy()
    import Dailytab_nocode

root1 = tk.Tk()

# set title
root1.title("HAPPY RICHIES")
root1.geometry("1500x1000")

# set bg
entry = tk.Entry()

# push button
daily_button = tk.Button(root1, text="Daily", padx=150, pady=10, borderwidth=30, command=day_page)
daily_button.place(x=200, y=50)

monthly_button = tk.Button(root1, text="Monthly", padx=150, pady=10, borderwidth=30)
monthly_button.place(x=900, y=50)

cal_button1 = tk.Button(root1, text="Calculate", padx=20, pady=5, borderwidth=30, command=lambda: monthly_save(float(e2.get())))
cal_button1.place(x=900, y=310)

cal_button2 = tk.Button(root1, text="Calculate", padx=20, pady=5, borderwidth=30, command=lambda: day_spend(float(e1.get()), monthly_save(float(e2.get()))))
cal_button2.place(x=900, y=340)

back_button = tk.Button(root1, text="Back", padx=20, pady=10, borderwidth=30, command=day_page)
back_button.place(x=200, y=400)

# input textbox
earn = tk.Label(root1, text="Monthly earning:").place(x=500, y=200)
e1 = tk.Entry(root1)
e1.place(x=700, y=200)

annual_save = tk.Label(root1, text="Annually expected saving:").place(x=500, y=230)
e2 = tk.Entry(root1)
e2.place(x=700, y=230)




# program1
month_save = tk.Label(root1, text="Monthly saving:")
month_save.place(x=500, y=310)
month_save.configure()

daily_spend = tk.Label(root1, text="Daily spending:")
daily_spend.place(x=500, y=340)
daily_spend.configure()
# call app
root1.mainloop()
