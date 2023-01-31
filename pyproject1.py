import tkinter as tk
from tkinter import *


root = Tk()
root.geometry('1920x1080')
root.title("Main Page")


canvas1 = Canvas(root, width = 1920, height =400 )      
canvas1.pack()      
img = PhotoImage(file='hosp4.png')
canvas1.create_image(0,50, anchor=NW, image=img)

canvas2= Canvas(root, width = 1700, height =1500 )      
canvas2.pack()      
img1 = PhotoImage(file='hospbg9.png')
canvas2.create_image(970,200, image=img1) 

labelhead=Label(root,text="STAR HOSPITAL",width=39,font=("bold",50),bg='#f9dcb4')

labelhead.place(x=0,y=10)

name=Label(root,text="Name:-\nKFBSC(IT)031:Ratnesh Mhatre",width=25,font=("bold",15),bg="#f9dcb4")
name.place(x=1240,y=91)

def rapage():
    import pyproject4

b1=Button(root,text="Register Appoinment",height=4,width=20,font=("bold",10),bg='#ff726f',fg = 'white',activebackground='#0bfc08',activeforeground='white',command=rapage)
b1.place(x=530,y=590)

def rpage():
    import pyproject2

b2=Button(root,text="Registered Appoinment",height=4,width=20,font=("bold",10),bg='#0e2c4e',fg = 'white',activebackground='#0bfc08',activeforeground='white',command=rpage)
b2.place(x=1050,y=650)

def dpage():
    import pyproject6


b3=Button(root,text="Home Visit",height=4,width=20,font=("bold",10),bg='#eaf076',activebackground='#0bfc08',activeforeground='white',command=dpage)
b3.place(x=60,y=500)

def npage():
    import pyproject3
    

b4=Button(root,text="Vaccine Registration",height=4,width=20,font=("bold",10),bg='#eaf076',activebackground='#0bfc08',activeforeground='white',command=npage)
b4.place(x=60,y=660)



     

