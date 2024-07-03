# Я захотів попробувати виконати д/з за допомогою графічної бібліотеки, яку раніше вчив надіюсь це не змінить сильно суть д/з

from tkinter import *

def main():
    aaa = entry.get()
    bbb = len(aaa)
    lab1.config(text=aaa)
    lab2.config(text=f'Symbols in text : {bbb}')

win = Tk()
win.geometry('500x600+600+200')
win.title("Tkinter Input Example")

entry = Entry(win, font='arial 20')
entry.pack(pady=20)

But1 = Button(win, text='Click to run the program', command=main, font='arial 20')
But1.pack(pady=10)

lab1 = Label(win, font='arial 30')
lab1.pack(pady=20)

lab2 = Label(win, font='arial 30')
lab2.pack(pady=20)

win.mainloop()


#ПРОСТА ДЗ
#  def string():
#     string = str(input('Введіть рядок для підрахунку довжини: '))
#     string_letters = len(string)
#     print(f'В довжина вашого рядку {string_letters}')
# string()