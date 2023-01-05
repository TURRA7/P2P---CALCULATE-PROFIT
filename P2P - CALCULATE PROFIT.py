from os import startfile
from tkinter import *
from tkinter import messagebox


# Creating the main window.
window_1 = Tk()
window_1.title("P2P")
window_1.geometry('570x180')
window_1.resizable(width=False, height=False)
lbl = Label(window_1)
lbl.grid(column=0, row=0)


# Function with text symbols.
def label(TEXT, X, Y):
    lbl = Label(window_1, text=TEXT, font=("Arial Bold", 10))
    lbl.grid(column=0, row=0)
    lbl.place(x=X, y=Y)


# Calling functions with text symbols.
label('СТАРТОВАЯ СУММА(₽|$|€|¥):', 10, 20)
label('ПРОФИТ (₽|$|€|¥):', 10, 50)
label('КОЛЛ-ВО КРУГОВ:', 10, 80)
label('КОМИССИЯ(₽|$|€|¥):', 10, 110)
label('ПРИБЛЬ ОБЩАЯ(СЛОЖНЫЙ %):', 255, 20)
label('ПРИБЛЬ ЧИСТАЯ(ОТ СЛОЖНОГО %):', 255, 50)
label('ПРИБЛЬ ЧИСТАЯ(ЗА КРУГИ):', 255, 80)
label('СПРЕД В %:', 255, 110)


# Input fields(txt1, txt2, txt3, txt4).
txt1 = Entry(window_1, width=10)
txt1.grid(column=0, row=0)
txt1.place(x=192, y=20)

txt2 = Entry(window_1, width=10)
txt2.grid(column=0, row=0)
txt2.place(x=192, y=50)

txt3 = Entry(window_1, width=10)
txt3.grid(column=0, row=0)
txt3.place(x=192, y=80)

txt4 = Entry(window_1, width=10)
txt4.grid(column=0, row=0)
txt4.place(x=192, y=110)


# Message-box.
def manual_1():
    messagebox.showinfo('ПРИБЛЬ ОБЩАЯ(ОТ СЛОЖНОГО %)',
    'ЗДЕСЬ КАЖДЫЙ НОВЫЙ КРУГ РАСЧИТЫВАЕТСЯ\
    \nИСХОДЯ ИЗ СУММЫ ПРЕДЫДУЩЕГО + ПРОФИТ\nА ТАК ЖЕ ВЫЧИТАЕТСЯ КОМИССИЯ.')

def manual_2():
    messagebox.showinfo('ПРИБЛЬ ЧИСТАЯ(ОТ СЛОЖНОГО %)', \
    'ЗДЕСЬ ОТ ОБЩЕЙ ПРИБЫЛИ(ОТ СЛОЖНОГО %),\
    \nВЫЧИТАЕТСЯ СТАРТОВАЯ СУММА И КОМИССИЯ')

def manual_3():
    messagebox.showinfo('ПРИБЛЬ ЧИСТАЯ(ЗА КУРУГИ)', \
    'РАСЧЕТ ВЕДЕТСЯ ПО ФОРМУЛЕ:\nПРИБЛЬ=(КРУГИ * ПРОФИТ)-КОМИССИЯ')

def manual_4():
    messagebox.showinfo('СПРЕД в %', 'РАСЧЕТ ВЕДЕТСЯ ПО ФОРМУЛЕ:\
    \nСПРЕД = P/(S/100) ГДЕ:\nP = ПРОФИТ и S = СТАРТОВАЯ СУММА.')


# Calculation of indicators.
def calculate():
    start_sum = txt1.get()
    profit = txt2.get()
    circles = txt3.get()
    commission = txt4.get()

    precent = float(profit) / (float(start_sum) / 100)
    amount = float(start_sum) * (pow((1 + float(precent) / 100), float(circles)))
    result = float(amount) - float(commission)
    clean_profit = (float(amount) - float(start_sum)) - float(commission)
    profit_circles_total = (float(profit) * float(circles)) - float(commission)

    label(int(result), 490, 20)
    label(int(clean_profit), 490, 50)
    label(int(profit_circles_total), 490, 80)
    label(precent, 490, 110)


# The button for calculating indicators.
def button(TEXT, com, X, Y):
    btn1 = Button(window_1, text=TEXT, command=com)
    btn1.grid(column=0, row=0)
    btn1.place(x=X, y=Y)


# Message-box Buttons.
button("?", manual_1, 545, 20)
button("?", manual_2, 545, 50)
button("?", manual_3, 545, 80)
button("?", manual_4, 545, 110)
button("РАСЧИТАТЬ", calculate, 10, 140)


window_1.mainloop()