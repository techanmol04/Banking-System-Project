import csv
import os
from tkinter import *

def csv_creator(a, t, i, f):
    filename = 'history.csv'
    rows = [str(a), str(t), str(i), str(f)]
    
    if filename in os.listdir():
        with open(filename, 'a', newline='') as f_object:
            writer_object = csv.writer(f_object)
            writer_object.writerow(rows)
    else:
        fields = ['AMOUNT', 'TIME(YEAR)', 'INTEREST', 'SIMPLE']
        with open(filename, 'w', newline='') as csvfile:
            writer_object = csv.writer(csvfile)
            writer_object.writerow(fields)
            writer_object.writerows([rows])

def calculate():
    try:
        t1 = float(t.get())
        a1 = float(a.get())
        i1 = float(i.get())
        t1 = t1 / 12  # Monthly time period
        f = (((i1 * a1 * t1) / 100) + a1)  # Simple Interest Formula
        csv_creator(a1, t1 * 12, i1, f)
        Result.set(f)
    except ValueError:
        Result.set("Invalid Input")

root = Tk()
root.geometry('500x500')
root.resizable(0, 0)
root.title('FIXED DEPOSIT')
root.config(bg='Yellow')

Label(root, text='Fixed Deposit', font='algerian', bg='yellow').pack()

Label(root, text='Amount', font='arial', bg='yellow').place(x=60, y=120)
a = StringVar()
Entry(root, font='arial', textvariable=a).place(x=200, y=120)

Label(root, text='Time', font='arial', bg='yellow').place(x=60, y=150)
t = StringVar()
Entry(root, font='arial', textvariable=t).place(x=200, y=150)

Label(root, text='Interest', font='arial', bg='yellow').place(x=60, y=180)
i = StringVar()
Entry(root, font='arial', textvariable=i).place(x=200, y=180)

Label(root, text='Result', font='arial', bg='yellow').place(x=60, y=210)
Result = StringVar()
Entry(root, font='arial', textvariable=Result).place(x=200, y=210)

Button(root, font='arial', text='CALCULATE', command=calculate).place(x=300, y=300)

root.mainloop()