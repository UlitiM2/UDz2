import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Menu
import time

def deli():
    p = val2.get()
    pr = []
    connection = sqlite3.connect('transport.db')
    cursor = connection.cursor()
    dost = []
    cursor.execute("SELECT * FROM Hran;")
    res = cursor.fetchall()
    for i in res:
        dost.append(i)
    for i in range(1, len(dost)):
        pr.append(f'{i}')
    if p in pr:
        connection = sqlite3.connect('transport.db')
        cursor = connection.cursor()
        cursor.execute(f"""DELETE FROM Hran WHERE ID = '{p}'""")
        connection.commit()
        cursor.execute(f"""DELETE FROM Svob WHERE ID = '{p}'""")
        connection.commit()
        cursor.execute(f"""DELETE FROM Zan WHERE ID = '{p}'""")
        connection.commit()
        dost = []
        cursor.execute("SELECT * FROM Hran;")
        res = cursor.fetchall()
        for i in res:
            dost.append(i)
        connection.commit()
        cursor.close()
        lbl = Label(window1, text="Удалено!", font=("Arial Bold", 12), bg='grey')
        lbl.pack()
        columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        tree = ttk.Treeview(window1, columns=columns, show="headings")
        tree.pack(ipady=20, ipadx=100, expand=1)
        tree.heading("1", text="ID")
        tree.heading("2", text="Название")
        tree.heading("3", text="Грузопод.")
        tree.heading("4", text="Длина, от")
        tree.heading("5", text="Длина, до")
        tree.heading("6", text="Ширина, от")
        tree.heading("7", text="Ширина, до")
        tree.heading("8", text="Высота, от")
        tree.heading("9", text="Высота, до")
        # добавляем данные
        for i in columns:
            tree.column(f"{i}", width=40)
        for i in dost:
            tree.insert("", END, values=i)
    else:
        print('Error')

def dob():
    a, b, c, d, e, f, g = val3.get(), val4.get(), val5.get(), val6.get(), val7.get(), val8.get(), val9.get()
    h = val43.get()
    pr = []
    for i in range(1, 50):
        pr.append(f'{i}')
    if b in pr and c in pr and d in pr and e in pr and f in pr and g in pr and h in pr:
        connection = sqlite3.connect('transport.db')
        cursor = connection.cursor()
        global dost
        dost = []
        cursor.execute("SELECT * FROM Hran;")
        res = cursor.fetchall()
        for i in res:
            dost.append(i)
        connection.commit()
        f = len(dost)
        dost1 = [(int(f+1), f'{a}', int(h), int(b), int(c), int(d), int(e), int(f), int(g))]
        cursor.executemany("INSERT INTO Hran VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", dost1)
        cursor.executemany("INSERT INTO Svob VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", dost1)
        connection.commit()
        cursor.close()
    else:
        print('Error')

def bron():
    k = val10.get()
    connection = sqlite3.connect('transport.db')
    cursor = connection.cursor()
    dost = []
    cursor.execute("SELECT * FROM Svob;")
    res = cursor.fetchall()
    for i in res:
        dost.append(i)
    pr = []
    for i in range(1, len(dost)):
        pr.append(f'{i}')
    if k in pr:
        connection = sqlite3.connect('transport.db')
        cursor = connection.cursor()
        cursor.execute(f"""Select * FROM Svob WHERE ID = '{k}'""")
        res = cursor.fetchall()
        cursor.executemany("INSERT INTO Zan VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", res)
        cursor.execute(f"""DELETE FROM Svob WHERE ID = '{k}'""")
        connection.commit()
    else:
        print('Error')

def bronir():
    dlo = val12.get()
    mas = val13.get()
    sho = val14.get()
    vd = val17.get()
    pr = []
    for i in range(1, 50):
        pr.append(f'{i}')
    if dlo in pr and mas in pr and sho in pr and vd in pr:
        connection = sqlite3.connect('transport.db')
        cursor = connection.cursor()
        dost = []
        cursor.execute("SELECT * FROM Svob;")
        res = cursor.fetchall()
        for i in res:
            dost.append(i)
        for j in range(len(dost) - 1):
            if not((int(dlo) < dost[j][3]) and (int(sho) < dost[j][5]) and (int(vd) < dost[j][7]) and (int(mas) < dost[j][2])):
                dost.remove(dost[j])
        columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        tree = ttk.Treeview(window5, columns=columns, show="headings")
        tree.pack(ipady=20, ipadx=100, expand=1)
        tree.heading("1", text="ID")
        tree.heading("2", text="Название")
        tree.heading("3", text="Грузопод.")
        tree.heading("4", text="Длина, от")
        tree.heading("5", text="Длина, до")
        tree.heading("6", text="Ширина, от")
        tree.heading("7", text="Ширина, до")
        tree.heading("8", text="Высота, от")
        tree.heading("9", text="Высота, до")
        for i in columns:
            tree.column(f"{i}", width=40)
        for k in dost:
            tree.insert("", END, values=k)
        window6 = Tk()
        window6.geometry('200x200')
        window6.title("Удалить")
        window6.configure(bg='grey')
        name = Label(window6, text=f"Выберите машину(ID):", font=("Arial Bold", 12), bg='grey')
        name.pack(anchor=CENTER)
        global val20
        val20 = Entry(window6, width=12, bg='grey')
        val20.pack()
        Button(window6, text='Отправить', bg='grey', font=("Arial Bold", 11), command=bronir1).place(x=55, y=50, width=85, height=50)
    else:
        print('Error')

def bronir1():
    p = val20.get()
    pr = []
    connection = sqlite3.connect('transport.db')
    cursor = connection.cursor()
    dost = []
    cursor.execute("SELECT * FROM Svob;")
    res = cursor.fetchall()
    for i in res:
        dost.append(i)
    for i in range(1, len(dost)):
        pr.append(f'{i}')
    if p in pr:
        connection = sqlite3.connect('transport.db')
        cursor = connection.cursor()
        cursor.execute(f"""Select * FROM Svob WHERE ID = '{p}'""")
        res = cursor.fetchall()
        cursor.executemany("INSERT INTO Zan VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", res)
        cursor.execute(f"""DELETE FROM Svob WHERE ID = '{p}'""")
        connection.commit()
    else:
        print('Error')

def delibr():
    k = val21.get()
    connection = sqlite3.connect('transport.db')
    cursor = connection.cursor()
    dost = []
    cursor.execute("SELECT * FROM Hran;")
    res = cursor.fetchall()
    for i in res:
        dost.append(i)
    pr = []
    for i in range(1, len(dost)):
        pr.append(f'{i}')
    if k in pr:
        connection = sqlite3.connect('transport.db')
        cursor = connection.cursor()
        cursor.execute(f"""Select * FROM Zan WHERE ID = '{k}'""")
        res = cursor.fetchall()
        cursor.executemany("INSERT INTO Svob VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", res)
        cursor.execute(f"""DELETE FROM Zan WHERE ID = '{k}'""")
        connection.commit()
    else:
        print('Error')

def ns():
    connection = sqlite3.connect('transport.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Hran(
                          ID INT,
                          Name TEXT,
                          massa INT,
                          dl INT,
                          dl1 INT,
                          shr INT,
                          shr1 INT,
                          vys INT,
                          vys1 INT);""")
    connection.commit()
    user = [(1, 'Газель', 2, 3, 3, 2, 2, 1.7, 2.2), (2, 'Бычок', 3, 4.2, 5, 2, 2.2, 2, 2.4),
            (3, 'MAN-10', 10, 6, 8, 2.45, 2.45, 2.3, 2.7), (4, 'Фура', 20, 13.6, 13.6, 2.46, 2.46, 2.5, 2.7)]
    cursor.executemany("INSERT INTO Hran VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
    cursor.execute("""CREATE TABLE IF NOT EXISTS Svob(
                                                 ID INT,
                                                 Name TEXT,
                                                 massa INT,
                                                 dl INT,
                                                 dl1 INT,
                                                 shr INT,
                                                 shr1 INT,
                                                 vys INT,
                                                 vys1 INT);""")
    connection.commit()
    user = [(1, 'Газель', 2, 3, 3, 2, 2, 1.7, 2.2), (2, 'Бычок', 3, 4.2, 5, 2, 2.2, 2, 2.4),
            (3, 'MAN-10', 10, 6, 8, 2.45, 2.45, 2.3, 2.7), (4, 'Фура', 20, 13.6, 13.6, 2.46, 2.46, 2.5, 2.7)]
    cursor.executemany("INSERT INTO Svob VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
    connection.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Zan(
                                      ID INT,
                                      Name TEXT,
                                      massa INT,
                                      dl INT,
                                      dl1 INT,
                                      shr INT,
                                      shr1 INT,
                                      vys INT,
                                      vys1 INT);""")
    connection.commit()
    cursor.close()

class Transort(Frame):
    def __init__(self, window):
        super(Transort, self).__init__(window)
        self.build()

    def build(self):
        btns = ['Добавить', 'Удалить', 'Просмотреть доступный', 'По грузоподъемности', 'Просматривать свободный', 'Вносить заявку на перевоз по габаритам', 'Подобрать и забронировать', 'Занятый транспорт', 'Отмена брони']
        x = 22
        y = 70
        for bt in btns:
            com = lambda x=bt: self.dey(x)
            Button(text=bt, bg='black',
                   font=("Arial Bold", 12),
                   command=com).place(x=x, y=y,
                                      width=255,
                                      height=40)
            y += 40
            if x > 800:
                x = 50
                y += 40

    def dey(self, operation):
        if operation == 'Удалить':
            global window1
            window1 = Tk()
            window1.geometry('700x900')
            window1.title("Удалить")
            window1.configure(bg='grey')
            connection = sqlite3.connect('transport.db')
            cursor = connection.cursor()
            dost = []
            cursor.execute("SELECT * FROM Hran;")
            res = cursor.fetchall()
            for i in res:
                dost.append(i)
            connection.commit()
            cursor.close()
            name = Label(window1, text=f"Введите id машины, которую нужно удалить:", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val2
            val2 = Entry(window1, width=12, bg='grey')
            val2.pack()
            columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            tree = ttk.Treeview(window1, columns=columns, show="headings")
            tree.pack(ipady=20,ipadx=100, expand=1)
            tree.heading("1", text="ID")
            tree.heading("2", text="Название")
            tree.heading("3", text="Грузопод.")
            tree.heading("4", text="Длина, от")
            tree.heading("5", text="Длина, до")
            tree.heading("6", text="Ширина, от")
            tree.heading("7", text="Ширина, до")
            tree.heading("8", text="Высота, от")
            tree.heading("9", text="Высота, до")
            # добавляем данные
            for i in columns:
                tree.column(f"{i}", width=40)
            for i in dost:
                tree.insert("", END, values=i)
            Button(window1, text='Отправить', bg='grey', font=("Arial Bold", 11), command=deli).place(x=308.5, y=50, width=85, height=50)

        elif operation == 'Добавить':
            window2 = Tk()
            window2.geometry('700x700')
            window2.title("Добавить")
            window2.configure(bg='grey')
            name = Label(window2, text=f"Введите название машины, которую нужно добавить:", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val3
            val3 = Entry(window2, width=12, bg='grey')
            val3.pack()
            name = Label(window2, text=f"Введите грузоподъемность машины, которую нужно добавить:", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val43
            val43 = Entry(window2, width=12, bg='grey')
            val43.pack()
            name = Label(window2, text=f"Введите длину машины, которую нужно добавить(от\до):", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val4
            val4 = Entry(window2, width=12, bg='grey')
            val4.pack()
            global val5
            val5 = Entry(window2, width=12, bg='grey')
            val5.pack()
            name = Label(window2, text=f"Введите ширину машины, которую нужно добавить(от\до):", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val6
            val6 = Entry(window2, width=12, bg='grey')
            val6.pack()
            global val7
            val7 = Entry(window2, width=12, bg='grey')
            val7.pack()
            name = Label(window2, text=f"Введите высоту машины, которую нужно добавить(от\до):", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val8
            val8 = Entry(window2, width=12, bg='grey')
            val8.pack()
            global val9
            val9 = Entry(window2, width=12, bg='grey')
            val9.pack()
            Button(window2, text='Отправить', bg='grey', font=("Arial Bold", 11), command=dob).place(x=308.5, y=330, width=85,height=50)

        elif operation == 'Просмотреть доступный':
            dost = []
            connection = sqlite3.connect('transport.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Hran;")
            third_result2 = cursor.fetchall()
            for i in third_result2:
                dost.append(i)
            connection.commit()
            cursor.close()
            window = Tk()
            window.title("Доступный транспорт")
            window.geometry('700x700')
            window.configure(bg='grey')
            name = Label(window, text="Транспорт", font=("Arial Bold", 15), bg='grey')
            name.pack()
            lbl = Label(window, text=f"Доступно:", font=("Arial Bold", 12), bg='grey')
            lbl.pack()
            columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            tree = ttk.Treeview(window, columns=columns, show="headings")
            tree.pack(ipady=20, ipadx=100, expand=1)
            tree.heading("1", text="ID")
            tree.heading("2", text="Название")
            tree.heading("3", text="Грузопод.")
            tree.heading("4", text="Длина, от")
            tree.heading("5", text="Длина, до")
            tree.heading("6", text="Ширина, от")
            tree.heading("7", text="Ширина, до")
            tree.heading("8", text="Высота, от")
            tree.heading("9", text="Высота, до")
            # добавляем данные
            for i in columns:
                tree.column(f"{i}", width=40)
            for i in dost:
                tree.insert("", END, values=i)

        elif operation == 'По грузоподъемности':
            window = Tk()
            window.geometry('700x700')
            window.title("Сортировка")
            window.configure(bg='grey')
            dost = []
            connection = sqlite3.connect('transport.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Hran;")
            third_result2 = cursor.fetchall()
            for i in third_result2:
                dost.append(i)
            connection.commit()
            cursor.close()
            v = sorted(dost)
            u =sorted(dost, reverse=True)
            name = Label(window, text=f"По возрастанию:", font=("Arial Bold", 15), bg='grey')
            name.pack()
            columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            tree = ttk.Treeview(window, columns=columns, show="headings")
            tree.pack(ipady=20, ipadx=100, expand=1)
            tree.heading("1", text="ID")
            tree.heading("2", text="Название")
            tree.heading("3", text="Грузопод.")
            tree.heading("4", text="Длина, от")
            tree.heading("5", text="Длина, до")
            tree.heading("6", text="Ширина, от")
            tree.heading("7", text="Ширина, до")
            tree.heading("8", text="Высота, от")
            tree.heading("9", text="Высота, до")
            # добавляем данные
            for i in columns:
                tree.column(f"{i}", width=40)
            for i in v:
                tree.insert("", END, values=i)
            name = Label(window, text=f"По убыванию:", font=("Arial Bold", 15), bg='grey')
            name.pack()
            columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            tree = ttk.Treeview(window, columns=columns, show="headings")
            tree.pack(ipady=20, ipadx=100, expand=1)
            tree.heading("1", text="ID")
            tree.heading("2", text="Название")
            tree.heading("3", text="Грузопод.")
            tree.heading("4", text="Длина, от")
            tree.heading("5", text="Длина, до")
            tree.heading("6", text="Ширина, от")
            tree.heading("7", text="Ширина, до")
            tree.heading("8", text="Высота, от")
            tree.heading("9", text="Высота, до")
            # добавляем данные
            for i in columns:
                tree.column(f"{i}", width=40)
            for i in u:
                tree.insert("", END, values=i)

        elif operation == 'Просматривать свободный':
            window3 = Tk()
            window3.geometry('700x700')
            window3.title("Свободный транспорт")
            window3.configure(bg='grey')
            connection = sqlite3.connect('transport.db')
            cursor = connection.cursor()
            dost = []
            cursor.execute("SELECT * FROM Svob;")
            res = cursor.fetchall()
            for i in res:
                dost.append(i)
            connection.commit()
            cursor.close()
            columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            tree = ttk.Treeview(window3, columns=columns, show="headings")
            tree.pack(ipady=20, ipadx=100, expand=1)
            tree.heading("1", text="ID")
            tree.heading("2", text="Название")
            tree.heading("3", text="Грузопод.")
            tree.heading("4", text="Длина, от")
            tree.heading("5", text="Длина, до")
            tree.heading("6", text="Ширина, от")
            tree.heading("7", text="Ширина, до")
            tree.heading("8", text="Высота, от")
            tree.heading("9", text="Высота, до")
            # добавляем данные
            for i in columns:
                tree.column(f"{i}", width=40)
            for i in dost:
                tree.insert("", END, values=i)

        elif operation == 'Вносить заявку на перевоз по габаритам':
            global window5
            window5 = Tk()
            window5.geometry('700x700')
            window5.title("Заявка")
            window5.configure(bg='grey')
            name = Label(window5, text=f"Введите длину груза", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val12
            val12 = Entry(window5, width=12, bg='grey')
            val12.pack()
            name = Label(window5, text=f"Введите массу груза", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val13
            val13 = Entry(window5, width=12, bg='grey')
            val13.pack()
            name = Label(window5, text=f"Введите ширину груза:", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val14
            val14 = Entry(window5, width=12, bg='grey')
            val14.pack()
            name = Label(window5, text=f"Введите высоту груза:", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val17
            val17 = Entry(window5, width=12, bg='grey')
            val17.pack()
            Button(window5, text='Отправить', bg='grey', font=("Arial Bold", 11), command=bronir).place(x=308, y=200, width=85, height=50)


        elif operation == 'Подобрать и забронировать':
            window4 = Tk()
            window4.geometry('700x700')
            window4.title("Забронировать")
            window4.configure(bg='grey')
            dost = []
            connection = sqlite3.connect('transport.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Svob;")
            third_result2 = cursor.fetchall()
            for i in third_result2:
                dost.append(i)
            connection.commit()
            cursor.close()
            name = Label(window4, text=f"Выберите машину, которую нужно забронировать:", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val10
            val10 = Entry(window4, width=12, bg='grey')
            val10.pack()
            columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            tree = ttk.Treeview(window4, columns=columns, show="headings")
            tree.pack(ipady=20, ipadx=100, expand=1)
            tree.heading("1", text="ID")
            tree.heading("2", text="Название")
            tree.heading("3", text="Грузопод.")
            tree.heading("4", text="Длина, от")
            tree.heading("5", text="Длина, до")
            tree.heading("6", text="Ширина, от")
            tree.heading("7", text="Ширина, до")
            tree.heading("8", text="Высота, от")
            tree.heading("9", text="Высота, до")
            # добавляем данные
            for i in columns:
                tree.column(f"{i}", width=40)
            for i in dost:
                tree.insert("", END, values=i)
            Button(window4, text='Отправить', bg='grey', font=("Arial Bold", 11), command=bron).place(x=308.5, y=50, width=85, height=50)

        elif operation == 'Занятый транспорт':
            window3 = Tk()
            window3.geometry('700x700')
            window3.title("Занятый транспорт")
            window3.configure(bg='grey')
            connection = sqlite3.connect('transport.db')
            cursor = connection.cursor()
            dost = []
            cursor.execute("SELECT * FROM Zan;")
            res = cursor.fetchall()
            for i in res:
                dost.append(i)
            connection.commit()
            cursor.close()
            columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            tree = ttk.Treeview(window3, columns=columns, show="headings")
            tree.pack(ipady=20, ipadx=100, expand=1)
            tree.heading("1", text="ID")
            tree.heading("2", text="Название")
            tree.heading("3", text="Грузопод.")
            tree.heading("4", text="Длина, от")
            tree.heading("5", text="Длина, до")
            tree.heading("6", text="Ширина, от")
            tree.heading("7", text="Ширина, до")
            tree.heading("8", text="Высота, от")
            tree.heading("9", text="Высота, до")
            # добавляем данные
            for i in columns:
                tree.column(f"{i}", width=40)
            for i in dost:
                tree.insert("", END, values=i)

        elif operation == 'Отмена брони':
            window7 = Tk()
            window7.geometry('700x700')
            window7.title("Отмена брони")
            window7.configure(bg='grey')
            connection = sqlite3.connect('transport.db')
            cursor = connection.cursor()
            dost = []
            cursor.execute("SELECT * FROM Zan;")
            res = cursor.fetchall()
            for i in res:
                dost.append(i)
            connection.commit()
            cursor.close()
            name = Label(window7, text=f"Введите id машины, на которую нужно отменить бронь:", font=("Arial Bold", 12), bg='grey')
            name.pack(anchor=CENTER)
            global val21
            val21 = Entry(window7, width=12, bg='grey')
            val21.pack()
            columns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
            tree = ttk.Treeview(window7, columns=columns, show="headings")
            tree.pack(ipady=20, ipadx=100, expand=1)
            tree.heading("1", text="ID")
            tree.heading("2", text="Название")
            tree.heading("3", text="Грузопод.")
            tree.heading("4", text="Длина, от")
            tree.heading("5", text="Длина, до")
            tree.heading("6", text="Ширина, от")
            tree.heading("7", text="Ширина, до")
            tree.heading("8", text="Высота, от")
            tree.heading("9", text="Высота, до")
            # добавляем данные
            for i in columns:
                tree.column(f"{i}", width=40)
            for i in dost:
                tree.insert("", END, values=i)
            Button(window7, text='Отправить', bg='grey', font=("Arial Bold", 11), command=delibr).place(x=308.5, y=50,width=85,height=50)

    def showinf():
        window = Tk()
        window.title("Справка")
        window.geometry('500x100')
        window.configure(bg='black')
        name = Label(window, text="Справка", font=("Arial Bold", 15), bg='black')
        name.pack()
        lbl = Label(window, text="В случае возникновения ошибок звоните +79091234325 \n Почта:gruzovichok@mail.ru \n Адрес: г.Санкт-Петербург, ул.Рубинштейна, 15", font=("Arial Bold", 12), bg='black')
        lbl.pack()

    def ex():
        exit()

if __name__ == '__main__':
    window = Tk()
    window.title("Транспорт")
    window.geometry('300x500')
    window.configure(bg='grey')

    name = Label(window, text="Транспортная компания", font=("Arial Bold", 20), bg='grey')
    name.pack(anchor=CENTER)
    lbl = Label(window, text="Выберите действие", font=("Arial Bold", 17), bg='grey')
    lbl.pack()
    mainmenu = Menu(window)
    window.config(menu=mainmenu)
    filemenu = Menu(mainmenu, tearoff=0)
    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu2 = Menu(helpmenu, tearoff=0)

    opermenu = Menu(mainmenu, tearoff=0)
    opermenu2 = Menu(mainmenu, tearoff=0)
    opermenu3 = Menu(mainmenu, tearoff=0)
    mainmenu.add_cascade(label="Справка", menu=opermenu2)
    opermenu2.add_command(label="Справка", command=Transort.showinf)
    mainmenu.add_cascade(label="Выход", menu=opermenu)
    opermenu.add_command(label="Выход", command=Transort.ex)
    mainmenu.add_cascade(label="Первый запуск", menu=opermenu3)
    opermenu3.add_command(label="Первый запуск", command=ns)

    app = Transort(window)
    app.pack()
    window.mainloop()