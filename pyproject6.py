from tkinter import*
from tkinter import messagebox


top=Toplevel()
top.geometry('1920x1080')
top.title("HSNC Doctor Home Visit")

canvas = Canvas(top, width = 1700, height =1500 )      
canvas.pack()      
img4 = PhotoImage(file='home visit2.png')
canvas.create_image(700,500, image=img4)

labelhead = Label(top, text="HSNC Doctor Home Visit",width=50,font=("bold", 40),bg='blue',fg='white')
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




fname = Label(top, text="Patient's department:",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=250)
fentry = Entry(top)
fentry.place(x=290,y=250)

fname = Label(top, text="Patient's Address",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=320)
fentry = Text(top,width=50,height=4)
fentry.place(x=290,y=320)

fname = Label(top, text="Patient's mobile no.:",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=410)
fentry = Entry(top)
fentry.place(x=290,y=410)

fname = Label(top, text="Patient's another mobile number :",width=25,font=("bold", 10),bg='yellow')
fname.place(x=80,y=470)
fentry = Entry(top)
fentry.place(x=290,y=470)

fname = Label(top, text="Doctor's Name :",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=520)

def show():
    label.config(text=clicked.get())

options=["Dr. Abdul S. Ansari","Dr. Abhijeet Soni","Dr. Abhishek Wadkar","Dr. Abhishek A. Karadkar","Dr. Aditi Shah","Dr. Anjali Patki","Dr. Anuja Pethe","Dr. Anup Chaudhari","Dr Chaitali Trivedi","Dr. Darshana Rane","Dr. Deepak P. Patkar","Dr. Devayani B. Venkat","Dr. Dilip D. Shah"]
clicked=StringVar()
clicked.set("Doctor's Name")
drop=OptionMenu(top,clicked,*options)
drop.place(x=300,y=520)


def message():
    msgbox=messagebox.showinfo("Successful","You're form is successfully submitted")

b1=Button(top,text="Submit",width=20,bg='brown',fg='white',activebackground='yellow',activeforeground='black',command=message)
b1.place(x=200,y=650)

fname = Label(top, text="Age :",width=20,font=("bold", 10),bg='yellow')
fname.place(x=100,y=570)
mentry = Entry(top)
mentry.place(x=290,y=570)



def maipage():
    top.destroy()

b1=Button(top,text="Go to main page",width=20,bg='brown',fg='white',activebackground='yellow',activeforeground='black',command=maipage) 
b1.place(x=400,y=650)



 

