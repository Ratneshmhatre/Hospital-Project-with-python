from tkinter import*
from tkinter import messagebox

top=Toplevel()
top.geometry('1920x1080')
top.title("Registration Form for booking an appointment")

canvas = Canvas(top, width = 1600, height =1000 )      
canvas.pack()      
img5 = PhotoImage(file='regis5.png')
canvas.create_image(800,500, image=img5)

labelhead = Label(top, text="Registration Form for Booking an Appointment :",width=40,font=("bold", 50),bg='#00304e',fg='white')
labelhead.place(x=-10,y=10)

fname = Label(top, text="First name:",width=20,font=("bold", 10),bg='yellow')
fname.place(x=120,y=130)
fentry = Entry(top)
fentry.place(x=400,y=130)
entry=fentry.get()
fname = Label(top, text="Middle name:",width=20,font=("bold", 10),bg='yellow')
fname.place(x=600,y=130)
fentry = Entry(top)
fentry.place(x=800,y=130)
fname = Label(top, text="Last name:",width=20,font=("bold", 10),bg='yellow')
fname.place(x=1000,y=130)
fentry = Entry(top)
fentry.place(x=1200,y=130)

label_3 = Label(top, text="Gender:",width=20,font=("bold", 10),bg='yellow')
label_3.place(x=120,y=180)
var = IntVar()
Radiobutton(top, text="Male",padx = 5, variable=var, value=1,bg='yellow').place(x=400,y=180)
Radiobutton(top, text="Female",padx = 20, variable=var, value=2,bg='yellow').place(x=460,y=180)
Radiobutton(top, text="Other",padx = 20, variable=var, value=3,bg='yellow').place(x=560,y=180)

adno = Label(top, text="Enter your addhaar number:",width=20,font=("bold", 10),bg='yellow')
adno.place(x=120,y=220)
adentry = Entry(top,width=30)
adentry.place(x=400,y=220)

state = Label(top, text="Enter your state:",width=20,font=("bold", 10),bg='yellow')
state.place(x=120,y=250)
state = Entry(top)
state.place(x=400,y=250)

state = Label(top, text="Enter your town/city:",width=20,font=("bold", 10),bg='yellow')
state.place(x=125,y=280)
state = Entry(top)
state.place(x=400,y=280)


state = Label(top, text="Enter your full address:",width=20,font=("bold", 10),bg='yellow')
state.place(x=125,y=310)
text=Text(top,heigh=3,width=40)
text.place(x=400,y=310)

state = Label(top, text="Enter your Mobile Number:",width=20,font=("bold", 10),bg='yellow')
state.place(x=120,y=380)
state = Entry(top)
state.place(x=400,y=380)

state = Label(top, text="Enter your another Number:",width=20,font=("bold", 10),bg='yellow')
state.place(x=120,y=410)
state = Entry(top)
state.place(x=400,y=410)

state = Label(top, text="Select your Date of Birth:",width=20,font=("bold", 11),bg='yellow')
state.place(x=120,y=450)

DOB=Label(top,text="Select Date:",width=20,font=("bold",10),bg='yellow')
DOB.place(x=400,y=485)

def show():
    label.config(text=clicked.get())

options=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
clicked=StringVar()
clicked.set("Date")
drop=OptionMenu(top,clicked,*options)
drop.place(x=570,y=480)

DOM=Label(top,text="Select Month:",width=20,font=("bold",10),bg='yellow')
DOM.place(x=670,y=485)

def show():
    label.config(text=clicked.get())

options=["January","February","March","April","May","June","July","August","September","October","November","December"]
clicked=StringVar()
clicked.set("Month")
drop=OptionMenu(top,clicked,*options)
drop.place(x=850,y=480)

DOM=Label(top,text="Select Year:",width=20,font=("bold",10),bg='yellow')
DOM.place(x=980,y=485)




def show():
    label.config(text=clicked.get())

options=[1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
clicked=StringVar()
clicked.set("Year")
drop=OptionMenu(top,clicked,*options)
drop.place(x=1150,y=480)


email = Label(top, text="Enter your Email ID:",width=20,font=("bold", 10),bg='yellow')
email.place(x=120,y=530)
emailentry = Entry(top)
emailentry.place(x=400,y=530)

email = Label(top, text="Re-conform your Email ID:",width=20,font=("bold", 10),bg='yellow')
email.place(x=120,y=560)
emailentry = Entry(top)
emailentry.place(x=400,y=560)

label_3 = Label(top, text="Are you suffering \nfrom any other disease:",width=20,font=("bold", 10),bg='yellow')
label_3.place(x=120,y=590)
var = IntVar()
Radiobutton(top, text="YES",padx = 5, variable=var, value=1,bg='yellow').place(x=400,y=595)
Radiobutton(top, text="NO",padx = 20, variable=var, value=2,bg='yellow').place(x=460,y=595)


DOM=Label(top,text="Select Department:",width=20,font=("bold",10),bg='yellow')
DOM.place(x=120,y=655)

def show():
    label.config(text=clicked.get())

options=["Radiation Oncology","haematology","Breast Surgery","General & Laparoscopy Surgery","spine Surgery","Cardiovascular & Thoracic Surgery","Urology Surgery","ENT","Health Check","Cardiology","Pulmonology","Neurology","Dermatology","Rheumatology","Plastic Surgery","Homeopathy","Diabetology","Psykchology","Nephrology","Gastroenterology","Dentistry"]
clicked=StringVar()
clicked.set("Department")
drop=OptionMenu(top,clicked,*options)
drop.place(x=400,y=655)

def message():
    msgbox=messagebox.showinfo("Successful","You're form is successfully submitted")

b1=Button(top,text="Submit",width=20,bg='brown',fg='white',activebackground='yellow',activeforeground='black',command=message)
b1.place(x=200,y=700)




def mpage():
    top.destroy()
    
b1=Button(top,text="Go to main page",width=20,bg='brown',fg='white',activebackground='yellow',activeforeground='black',command=mpage)
b1.place(x=400,y=700)







