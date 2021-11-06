import tkinter as tk

root1 = tk.Tk()

# set title
root1.title("HAPPY RICHIES")
root1.geometry("1500x1000")

# set bg
entry = tk.Entry()

# push button
daily_button = tk.Button(root1, text="Daily", padx=150, pady=10, borderwidth=30)
daily_button.place(x=200, y=50)

monthly_button = tk.Button(root1, text="Monthly", padx=150, pady=10, borderwidth=30)
monthly_button.place(x=900, y=50)

back_button = tk.Button(root1, text="Back", padx=20, pady=10, borderwidth=30)
back_button.place(x=200, y=400)

# input textbox
earn = tk.Label(root1, text="Monthly earning:").place(x=500, y=200)
e1 = tk.Entry(root1)
e1.place(x=635, y=200)

target_save = tk.Label(root1, text="Expected saving:").place(x=500, y=230)
e2 = tk.Entry(root1)
e2.place(x=635, y=230)

num_day = tk.Label(root1, text="Amount of Day:").place(x=500, y=260)
e3 = tk.Entry(root1)
e3.place(x=635, y=260)

# program1
month_save = tk.Label(root1, text="Monthly saving:").place(x=500, y=310)
daily_save = tk.Label(root1, text="Daily saving:").place(x=500, y=340)

# call app
root1.mainloop()