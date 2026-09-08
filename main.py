from tkinter import *
import sqlite3
from datetime import datetime, timedelta
import webbrowser


def enter_color(event):
    lbl5.config(fg='Red')


def leave_color(event):
    lbl5.config(fg='#0000FF')


def website_click(event):
    cur.execute(f'''SELECT info,url,ad FROM tasks WHERE info = "{list1.get(list1.curselection())}"''')
    txt = cur.fetchall()
    webbrowser.open(txt[0][1])


def click1():
    cur.execute(
        f'''INSERT INTO tasks VALUES ('{entr1.get()}','{entr2.get()}','{entr3.get()}','{str(datetime.now() + timedelta(days=1)).split(" ")[0]}','{str(datetime.now() + timedelta(weeks=1)).split(" ")[0]}','{str(datetime.now() + timedelta(days=30)).split(" ")[0]}','{str(datetime.now() + timedelta(days=90)).split(" ")[0]}')''')
    entr1.delete(first=0, last=END)
    entr2.delete(first=0, last=END)
    entr3.delete(first=0, last=END)
    db.commit()


def click2():
    cur.execute(f'''SELECT info,url,ad FROM tasks WHERE info = "{list1.get(list1.curselection())}"''')
    txt = cur.fetchall()
    lbl4.config(text=txt[0][0])
    lbl5.config(text=txt[0][1])
    lbl6.config(text=txt[0][2])


root = Tk()

db = sqlite3.connect('data.db')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS tasks (info TEXT,url TEXT,ad TEXT,p1 TEXT,p2 TEXT,p3 TEXT,p4 TEXT)''')
db.commit()

# инициализация окна
root.geometry("900x600")
root.title("EduHelper")
root.resizable(height=False, width=False)
root.iconbitmap('icon.ico')
root.config(bg='#ab9379')

# инициализация полей ввода
entr1 = Entry(root, bg='#cbb29e', font=('Times New Roman', 12))
lbl1 = Label(root, text="Информация о изученном материале:", bg='#c9d0a4', font=('Builder Sans', 10, "bold"))

entr2 = Entry(root, bg='#cbb29e', font=('Times New Roman', 12))
lbl2 = Label(root, text="Ссылка на ресурс:", bg='#c9d0a4', font=('Builder Sans', 10, "bold"))

entr3 = Entry(root, bg='#cbb29e', font=('Times New Roman', 12))
lbl3 = Label(root, text="Заметки:", bg='#c9d0a4', font=('Builder Sans', 10, "bold"))

btn1 = Button(root, text="Внести данные", command=click1, fg='Black', font=('Builder Sans', 15, "bold"),
              background='#e8ddaf', activebackground='#ab9379', activeforeground="grey")

# размещение виджетов на окне
lbl1.place(height=30, width=300, y=310)
entr1.place(height=50, width=300, y=340)

lbl2.place(height=30, width=300, y=390)
entr2.place(height=50, width=300, y=420)

lbl3.place(height=30, width=300, y=470)
entr3.place(height=50, width=300, y=500)

btn1.place(height=50, width=300, y=550)

# инициализация listbox и button для показа информации
list1 = Listbox(root, width=50, height=10, bg='#cbb29e', font=('Times New Roman', 12))
btn2 = Button(root, text="Получить информацию", command=click2, width=27, height=3, fg='Black',
              font=('Builder Sans', 15, "bold"), bg='#e8ddaf', activebackground='#ab9379', activeforeground="grey")

btn2.place(height=50, width=300, x=600, y=550)
list1.place(height=240, width=300, x=600, y=310)

# инициализация label с информацией
lbl4 = Label(root, bg='#cbb29e', font=('Times New Roman', 12))

lbl5 = Label(root, bg='#cbb29e', fg='#0000FF', font=('Times New Roman', 12))
lbl5.bind("<Button-1>", website_click)
lbl5.bind("<Enter>", enter_color)
lbl5.bind("<Leave>", leave_color)

lbl6 = Label(root, bg='#cbb29e', font=('Times New Roman', 12))

# размещение label с информацией
lbl4.place(height=70, width=450, x=225)
lbl5.place(height=70, width=450, x=225, y=70)
lbl6.place(height=70, width=450, x=225, y=140)

cur.execute(
    f'''SELECT info FROM tasks WHERE p1 = "{str(datetime.now()).split(" ")[0]}" OR p2 = "{str(datetime.now()).split(" ")[0]}" OR p3 = "{str(datetime.now()).split(" ")[0]}" OR p4 = "{str(datetime.now()).split(" ")[0]}" ''')
text_db = cur.fetchall()

k = 0
for i in text_db:
    list1.insert(k, i[0])
    k += 1

root.mainloop()
db.close()
