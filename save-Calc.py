# Takes on the salary of a person with travel, food and miscellaneous

# tkinter library

# create the main window

# add widget to main window 

# apply event functionalities to the buttons


def exit():

    window.destroy()

def clear_all():

    e1.delete(0, tk.END)

    e2.delete(0, tk.END)

    e3.delete(0, tk.END)

    e4.delete(0, tk.END)

    e5.config(state = 'normal')

    e5.delete(0, tk.END)

    e5.config(state = 'disabled')

def cal_savings():

    e5.config(state = 'normal')

    e5.delete(0, tk.END)

    e5.config(state = 'disabled')

    salary = int(e1.get())

    total_expenditure = int(e2.get()) + int(e3.get()) + int(e4.get())

    savings = salary - total_expenditure

    e5.config(state = 'normal')

    e5.insert(0, savings)

    e5.config(state = 'disabled')



import tkinter as tk

window = tk.Tk()

window.geometry("300x400")

window.config(bg = "#f39c12")

window.resizable(width = False, height = False)

window.title('Savings Calculator')

v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()
v4 = tk.StringVar()
v5 = tk.StringVar()

l1 = tk.Label(window, text = "Enter the values", font = ("Arial", 20), fg = "Black", bg = "White")

l2 = tk.Label(window, text = " Total salary : ", font = ("Arial", 10), fg = "Black", bg = "White")
e1 = tk.Entry(window, font = ("Arial", 11), textvariable = v1)

l3 = tk.Label(window, text = " Travel : ", font = ("Arial", 10), fg = "Black", bg = "White")
e2 = tk.Entry(window, font = ("Arial", 11), textvariable = v2)

l4 = tk.Label(window, text = " Food : ", font = ("Arial", 10), fg = "Black", bg = "White")
e3 = tk.Entry(window, font = ("Arial", 11), textvariable = v3)

l5 = tk.Label(window, text = " Miscellaneous : ", font = (" Arial ", 10), fg = "Black", bg = "White")
e4 = tk.Entry(window, font = (" Arial ", 11), textvariable = v4)

b1 = tk.Button(window, text = "Calculate your savings ", font = (" Arial", 15), command = cal_savings)

l6 = tk.Label(window, text = "Your savings : ", font = (" Arial ", 10), fg = "Black", bg = "White")
e5 = tk.Entry(window, font = (" Arial ", 11), state = 'disabled', textvariable = v5)

b2 = tk.Button(window, text = "Clear the values ", font = (" Arial ", 15), command = clear_all)
b3 = tk.Button(window, text= "Exit the application", font = (" Arial ", 15), command = exit)

l1.place(x = 50, y = 20)
l2.place(x = 20, y = 70)
e1.place(x = 120, y = 70)
l3.place(x = 20, y = 100)
e2.place(x = 120, y = 100)
l4.place(x = 20, y = 130)
e3.place(x = 120, y = 130)
l5.place(x =20, y = 160)
e4.place(x = 120, y =160)
l6.place(x = 20, y =260)
e5.place(x = 120, y = 260)
b2.place(x = 70, y = 300)
b3.place(x = 60, y = 350)

window.mainloop()
