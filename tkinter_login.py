# TKinter and database


from tkinter import *
from tkinter import messagebox
from tkinter import  ttk
from functools import partial
import tkinter.font as font

import mysql.connector as m

mydatabase = m.connect(host="localhost", user="root", password="rootsql123", database="turfBS")
query1 = "insert into turf_users(username,password) values(%s,%s)"  # must be "s"
query2 = "insert into turf_users(username,password) values(%s,%s)"
query3 = "SELECT username, password FROM turf_users"


def register():
    try:
        myFont = font.Font(family='Arial', size=24)
        name_1 = usernameEntry.get()
        password_1 = passwordEntry.get()
        # print(name_1,address_1,age_1)
        cursor = mydatabase.cursor()
        cursor.execute(query1, [name_1, password_1])  # second argument has to be list or tuple or dictionary
        mydatabase.commit()
        resultlabel.config(fg="black", font=myFont)
        resultlabel["text"] = "Registration Done."
    except m.Error as error:
        error_code = error.errno
        if error_code == 1062:
            # print("User already exists")
            messagebox.showinfo("Error", "User already exists")
        else:
            print("An error occurred:", error)

def validateLogin():
    myFont = font.Font(family='Helvetica', size=16)
    cursor = mydatabase.cursor()
    cursor.execute(query3)
    users = cursor.fetchall()

    # Check if the input username and password match any entry in the database
    input_username = usernameEntry.get()
    input_password = passwordEntry.get()
    valid_user = False
    for user in users:
        if user[0] == input_username and user[1] == input_password:
            valid_user = True
            break

    # Update label based on validation result  # needs to be changed so that it can be fetched to continue to fill more records
    if valid_user:
        resultlabel.config(fg="green", font=myFont)
        resultlabel["text"] = "Valid User"
    else:
        resultlabel.config(fg="red", font=myFont)
        resultlabel["text"] = "Invalid User"


# window
tkWindow = Tk()
tkWindow.geometry('600x350')
tkWindow.title('Turf Booking Portal')

# name label and text entry box
usernameLabel = Label(tkWindow, text="User Name")
usernameLabel.grid(row=0, column=0)
usernameEntry = Entry(tkWindow)
usernameEntry.grid(row=0, column=1)

# Address label and password entry box
passwordLabel = Label(tkWindow, text="Password")
passwordLabel.grid(row=1, column=0)

passwordEntry = Entry(tkWindow, show='*')
passwordEntry.grid(row=1, column=1)

resultlabel = Label(tkWindow)
resultlabel.grid(row=6, column=0)


# login button
saveButton = Button(tkWindow, text="Register", command=register)
saveButton.grid(row=5, column=0)

#register
loginButton = Button(tkWindow, text="Login", command=validateLogin)
loginButton.grid(row=5, column=1)

# dropdown
# options = ["Urban Sports Zone, Juhu", "The Pitch, Yeoor Hills", "Hatrics, Thane", "Sporting Lions, Bandra", "AIM Turf, Nanavati"]
# label_turf = ttk.Label(tkWindow, text="Turf")
# label_turf.grid(row=4, column=0)
# combo = ttk.Combobox(tkWindow, values=options)
# combo.grid(row=4, column=1)

tkWindow.mainloop()
