from tkinter import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import Booking_Back
#===================================getting selected row==============================
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
#====================================View method==============================================
def view_command():
    list1.delete(0,END)
    for row in Booking_Back.view():
        list1.insert(END,row)
#====================================Search method==============================================
def search_command():
    list1.delete(0,END)
    for row in Booking_Back.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)
#====================================Add method==============================================
def add_command():
    Booking_Back.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
#====================================Delete method==============================================
def delete_command():
    Booking_Back.delete(selected_tuple[0])
#====================================Update method==============================================
def update_command():
    Booking_Back.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
#====================================close method==============================================
def Clo_Open():
    window.destroy()
    import Login_window
    
#====================================Generation of window==============================================
window=Tk()

window.wm_title("Make Booking") #Window title
#====================================lables==============================================
l1=Label(window,text="Surname")
l1.grid(row=0,column=0)

l2=Label(window,text="Num of People")
l2.grid(row=0,column=2)

l3=Label(window,text="Date")
l3.grid(row=1,column=0)

l4=Label(window,text="Time")
l4.grid(row=1,column=2)
#====================================entry boxes==============================================
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)
#====================================list box==============================================
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)
#====================================scrollbar==============================================
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)
#====================================Buttons==============================================
b1=Button(window,text="View all Bookings", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Bookings", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Booking", width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Booking", width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Booking", width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close Bookings", width=12,command=Clo_Open)
b6.grid(row=7,column=3)


window.mainloop()
