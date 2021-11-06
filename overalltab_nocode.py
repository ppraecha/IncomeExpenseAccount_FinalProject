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

overall_button = tk.Button(root1, text="Overall", padx=100, pady=10, borderwidth=30)
overall_button.place(x=200, y=150)

jan_button = tk.Button(root1, text="January", padx=98, pady=10, borderwidth=30)
jan_button.place(x=200, y=190)

feb_button = tk.Button(root1, text="February", padx=95, pady=10, borderwidth=30)
feb_button.place(x=200, y=230)

mar_button = tk.Button(root1, text="March", padx=103, pady=10, borderwidth=30)
mar_button.place(x=200, y=270)

apr_button = tk.Button(root1, text="April", padx=108, pady=10, borderwidth=30)
apr_button.place(x=200, y=310)

may_button = tk.Button(root1, text="May", padx=109, pady=10, borderwidth=30)
may_button.place(x=200, y=350)

jun_button = tk.Button(root1, text="June", padx=107, pady=10, borderwidth=30)
jun_button.place(x=200, y=390)

jul_button = tk.Button(root1, text="July", padx=110, pady=10, borderwidth=30)
jul_button.place(x=200, y=430)

aug_button = tk.Button(root1, text="August", padx=101, pady=10, borderwidth=30)
aug_button.place(x=200, y=470)

sep_button = tk.Button(root1, text="September", padx=89, pady=10, borderwidth=30)
sep_button.place(x=200, y=510)

oct_button = tk.Button(root1, text="October", padx=97, pady=10, borderwidth=30)
oct_button.place(x=200, y=550)

nov_button = tk.Button(root1, text="November", padx=91, pady=10, borderwidth=30)
nov_button.place(x=200, y=590)

dec_button = tk.Button(root1, text="December", padx=91, pady=10, borderwidth=30)
dec_button.place(x=200, y=630)

record_button = tk.Button(root1, text="Record", padx=20, pady=10, borderwidth=30)
record_button.place(x=200, y=730)

# program shown
Total_save = tk.Label(root1, text="Total saving:").place(x=200, y=690)

# call app
root1.mainloop()
