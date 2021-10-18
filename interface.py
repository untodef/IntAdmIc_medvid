from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


def insert():
    id = e_id.get()
    film = e_film.get()
    budget = e_budget.get()

    if(id=="" or film=="" or budget==""):
        MessageBox.showinfo("Insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="Studio")
        cursor = con.cursor()
        cursor.execute("insert into project values('"+ id +"','"+ film +"','"+ budget +"')")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_film.delete(0, 'end')
        e_budget.delete(0, 'end')
        show()
        MessageBox.showinfo("Insert status", "Inserted successfully")
        con.close()


def delete():
    if(e_id.get() == ""):
        MessageBox.showinfo("Delete status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="Studio")
        cursor = con.cursor()
        cursor.execute("delete from project where id='"+ e_id.get() +"'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_film.delete(0, 'end')
        e_budget.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete status", "Deleted successfully")
        con.close()


def update():
    id = e_id.get()
    film = e_film.get()
    budget = e_budget.get()

    if(id=="" or film=="" or budget==""):
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="Studio")
        cursor = con.cursor()
        cursor.execute("update project set film='"+ film +"', budget='"+ budget +"' where id='"+ id +"'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_film.delete(0, 'end')
        e_budget.delete(0, 'end')
        show()
        MessageBox.showinfo("Update status", "Updated successfully")
        con.close()


def get():
    if(e_id.get() == ""):
        MessageBox.showinfo("Fetch status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="Studio")
        cursor = con.cursor()
        cursor.execute("select * from project where id='"+ e_id.get() +"'")
        rows = cursor.fetchall()
        
        for row in rows:
            e_film.insert(0, row[1])
            e_budget.insert(0, row[2])

        con.close()


def show():
    con = mysql.connect(host="localhost", user="root", password="", database="Studio")
    cursor = con.cursor()
    cursor.execute("select * from project")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = str(row[0])+ '         '+ row[1]
        list.insert(list.size()+1, insertData)

    con.close()


root = Tk()
root.geometry("600x250")
root.title("Studio")

id = Label(root, text='Enter ID', font=('bold', 10))
id.place(x=20, y=30)

film = Label(root, text='Enter film', font=('bold', 10))
film.place(x=20, y=60)

budget = Label(root, text='Enter films budget', font=('bold', 10))
budget.place(x=20, y=90)

e_id = Entry()
e_id.place(x=150, y=30)

e_film = Entry()
e_film.place(x=150, y=60)

e_budget = Entry()
e_budget.place(x=150, y=90)

insert = Button(root, text="Insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
delete.place(x=100, y=140)

update = Button(root, text="Update", font=("italic", 10), bg="white", command=update)
update.place(x=180, y=140)

get= Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=260, y=140)


list = Listbox(root)
list.place(x=360, y=30)
show()

root.mainloop()
