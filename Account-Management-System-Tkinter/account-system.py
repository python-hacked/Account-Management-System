from tkinter import *
from tkinter import messagebox
import database_account

window = Tk()
window.title("Account Management System")
window.config(bg="navajo white")
window.geometry('1350x750')

def view():
    lb.delete(0,END)
    for row in database_account.viewall():
        lb.insert(END, row)

def search():
    lb.delete(0, END)
    for row in database_account.search(firstname=firstname.get(), lastname=lastname.get(), username=username.get(), password=password.get(), position=position.get()):
        lb.insert(END, row)

def add():
    database_account.add(firstname.get(), lastname.get(), username.get(), password.get(), position.get(), date.get())
    messagebox.showinfo("Add", "New Account Added Successfully")
    lb.delete(0, END)
    lb.insert(END, firstname.get(), lastname.get(), username.get(), password.get(), position.get(), date.get())

def get_selected_row(event):
    try:
        global selected_tuple
        index = lb.curselection()[0]
        selected_tuple = lb.get(index)
        EntryFirstName.delete(0,END)
        EntryFirstName.insert(END,selected_tuple[1])

        EntryLastName.delete(0,END)
        EntryLastName.insert(END,selected_tuple[2])

        EntryUsername.delete(0,END)
        EntryUsername.insert(END,selected_tuple[3])

        EntryPassword.delete(0,END)
        EntryPassword.insert(END,selected_tuple[4])

        EntryPosition.delete(0,END)
        EntryPosition.insert(END,selected_tuple[5])

        EntryDate.delete(0, END)
        EntryDate.insert(END, selected_tuple[6])
    except IndexError:
        pass

def update():
    database_account.update(selected_tuple[0], firstname.get(), lastname.get(), username.get(), password.get(), position.get(), date.get())
    messagebox.showinfo("Update", "Account Has Been Updated Successfully")
    view()

def delete():
    database_account.delete(selected_tuple[0])
    messagebox.showinfo("Delete Account", 'Account Has Been Deleted Successfully')
    view()
    #lb.delete(END,get_selected_row.selected_tuple)
def clear():
    lb.delete(0,END)
    EntryFirstName.delete(0,END)
    EntryLastName.delete(0,END)
    EntryUsername.delete(0,END)
    EntryPassword.delete(0,END)
    EntryPosition.delete(0,END)
    EntryDate.delete(0, END)

lblfirstname = Label(window, text="First Name", font=("Calibri", 14, "bold"), fg="black", bg="navajo white")
lblfirstname.grid(row=0, column=0, columnspan=2)

lbllastname = Label(window,text="Last Name", font=("Calibri", 14, "bold"), fg="black", bg="navajo white")
lbllastname.grid(row=1,column=0,columnspan=2)

lblusername = Label(window,text="Username", font=("Calibri", 14, "bold"), fg="black", bg="navajo white")
lblusername.grid(row=2,column=0,columnspan=2)

lblpassword = Label(window, text="Password", font=("Calibri", 14, "bold"), fg="black", bg="navajo white")
lblpassword.grid(row=3, column=0, columnspan=2)

lblposition = Label(window,text="Position", font=("Calibri", 14, "bold"), fg="black", bg="navajo white")
lblposition.grid(row=4,column=0,columnspan=2)

lbldate = Label(window,text="Date", font=("Calibri", 14, "bold"), fg="black", bg="navajo white")
lbldate.grid(row=5,column=0,columnspan=2)

firstname=StringVar()
EntryFirstName = Entry(window,textvariable=firstname, font=("Calibri", 14, "italic"), width=30)
EntryFirstName.grid(row=0,column=0,columnspan=10)

lastname=StringVar()
EntryLastName = Entry(window,textvariable=lastname, font=("Calibri", 14, "italic"), width=30)
EntryLastName.grid(row=1,column=0,columnspan=10)

username=StringVar()
EntryUsername = Entry(window,textvariable=username, font=("Calibri", 14, "italic"), width=30)
EntryUsername.grid(row=2,column=0,columnspan=10)

password=StringVar()
EntryPassword = Entry(window,textvariable=password, font=("Calibri", 14, "italic"), width=30)
EntryPassword.grid(row=3,column=0,columnspan=10)

position=StringVar()
EntryPosition = Entry(window,textvariable=position, font=("Calibri", 14, "italic"), width=30)
EntryPosition.grid(row=4,column=0,columnspan=10)

date = StringVar()
EntryDate = Entry(window,textvariable=date, font=("Calibri", 14, "italic"), width=30)
EntryDate.grid(row=5,column=0,columnspan=10)

AddButton = Button(window,text="Add",width=12,command=add, font=("Calibri", 10, "italic"), fg="black", bg="navajo white", relief=RIDGE, bd=10)
AddButton.grid(row=6,column=0)

UpdateButton = Button(window,text="Update",width=12,command=update, font=("Calibri", 10, "italic"), fg="black", bg="navajo white", relief=RIDGE, bd=10)
UpdateButton.grid(row=6,column=1)

SearchButton = Button(window,text="Search",width=12,command=search, font=("Calibri", 10, "italic"), fg="black", bg="navajo white", relief=RIDGE, bd=10)
SearchButton.grid(row=6,column=2)

ViewAllButton = Button(window,text="View All",width=12,command=view, font=("Calibri", 10, "italic"), fg="black", bg="navajo white", relief=RIDGE, bd=10)
ViewAllButton.grid(row=6,column=3)

DeleteButton = Button(window,text="Delete",width=12,command=delete, font=("Calibri", 10, "italic"), fg="black", bg="navajo white", relief=RIDGE, bd=10)
DeleteButton.grid(row=6,column=4)

ClearAllButton = Button(window,text="Clear All",width=12,command=clear, font=("Calibri", 10, "italic"), fg="black", bg="navajo white", relief=RIDGE, bd=10)
ClearAllButton.grid(row=6,column=5)

lb=Listbox(window,height=20,width=94)
lb.grid(row=7,column=0,columnspan=6)

sb=Scrollbar(window)
sb.grid(row=7,column=6,rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop()
