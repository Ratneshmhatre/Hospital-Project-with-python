from tkinter import*
from tkinter import messagebox


top=Toplevel()
top.geometry('1920x1080')
top.title("Registration Form")

canvas = Canvas(top, width = 1700, height =1500 )      
canvas.pack()      
img4 = PhotoImage(file='pat2.png')
canvas.create_image(700,500, image=img4)

labelhead = Label(top, text="INFORMATION OF THE PATIENT'S",width=50,font=("bold", 40),bg='orange',fg='white')
labelhead.place(x=0,y=10)



fname = Label(top, text="First name:",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=130)
fentry = Entry(top)
fentry.place(x=290,y=130)
fname = Label(top, text="Middle name:",width=20,font=("bold", 10),bg='yellow')
fname.place(x=500,y=130)
mentry = Entry(top)
mentry.place(x=690,y=130)
fname = Label(top, text="Last name:",width=20,font=("bold", 10),bg='yellow')
fname.place(x=900,y=130)
lentry = Entry(top)
lentry.place(x=1090,y=130)





label_3 = Label(top, text="Gender:",width=20,font=("bold", 10),bg='yellow')
label_3.place(x=100,y=180)
var1 = IntVar()
Radiobutton(top, text="Male",padx = 5, variable=var1, value=1,width=10,bg='yellow').place(x=300,y=180)
Radiobutton(top, text="Female",padx = 20, variable=var1, value=2,bg='yellow').place(x=400,y=180)
Radiobutton(top, text="Other",padx = 20, variable=var1, value=3,bg='yellow').place(x=500,y=180)


label4 = Label(top, text="Nationality",width=20,font=("bold", 10),bg='yellow')
label4.place(x=100,y=240)
var2 = IntVar()
Radiobutton(top, text="India", padx = 5, variable=var2, value=1,width=10,bg='yellow').place(x=300,y=220)
Radiobutton(top, text="Iran",padx = 20, variable=var2, value=2,width=10,bg='yellow').place(x=400,y=220)
Radiobutton(top, text="Iraq",padx = 20, variable=var2, value=3,width=10,bg='yellow').place(x=500,y=220)
Radiobutton(top, text="Nepal",padx = 20, variable=var2, value=4,width=10,bg='yellow').place(x=600,y=220)
Radiobutton(top, text="Russia",padx = 20, variable=var2, value=5,width=5,bg='yellow').place(x=704,y=220)
Radiobutton(top, text="Bangladesh",padx = 20, variable=var2, value=6,bg='yellow').place(x=930,y=220)

Radiobutton(top, text="Pakistan",padx = 20, variable=var2, value=15,width=10,bg='yellow').place(x=805,y=220)
Radiobutton(top, text="UAE",padx = 20, variable=var2, value=9,width=10,bg='yellow').place(x=500,y=245)
Radiobutton(top, text="Singapore",padx = 20, variable=var2, value=8,bg='yellow').place(x=415,y=245)
Radiobutton(top, text="Saudi Arabia",padx = 20, variable=var2, value=7,bg='yellow').place(x=300,y=245)


Radiobutton(top, text="Thailand",padx = 20, variable=var2, value=10,bg='yellow').place(x=605,y=245)
Radiobutton(top, text="Philippines",padx = 20, variable=var2, value=11,bg='yellow').place(x=700,y=245)
Radiobutton(top, text="Qatar",padx = 20, variable=var2, value=12,width=10,bg='yellow').place(x=800,y=245)
Radiobutton(top, text="Syra",padx = 20, variable=var2, value=13,width=12,bg='yellow').place(x=910,y=245)



fname = Label(top, text="Patient's department:",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=290)
fentry = Entry(top)
fentry.place(x=290,y=290)

fname = Label(top, text="Patient's Bill:",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=350)
fentry = Entry(top)
fentry.place(x=290,y=350)

fname = Label(top, text="Patient's bed no. :",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=410)
fentry = Entry(top)
fentry.place(x=290,y=410)

fname = Label(top, text="Patient's mobile number :",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=470)
fentry = Entry(top)
fentry.place(x=290,y=470)

fname = Label(top, text="Patient's bed no. :",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=530)
fentry = Entry(top)
fentry.place(x=290,y=530)

fname = Label(top, text="Patient's discharge date :",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=590)
fentry = Entry(top)
fentry.place(x=290,y=590)

def message():
    msgbox=messagebox.showinfo("Successful","You're form is successfully submitted")
b1=Button(top,text="Submit",width=20,bg='brown',fg='white',activebackground='yellow',activeforeground='black',command=message)
b1.place(x=200,y=650)





def maipage():
    top.destroy()

b1=Button(top,text="Go to main page",width=20,bg='brown',fg='white',activebackground='yellow',activeforeground='black',command=maipage) 
b1.place(x=400,y=650)



 

