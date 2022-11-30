from tkinter import *
from tkinter import messagebox
import ast

root=Tk()
#label_declarations
#title_1 = tk.Title('FORM_882)
#root.attributes('-fullscreen',True)
#root.maxsize(2000,2000)
root.geometry('800x800')
conf_1 = root.configure(bg='#fff')
root.resizable(False,False)
#img = PhotoImage(file='Img.jpeg')
Label(root,border=0,bg='white').place(x=50,y=90)
frame = Frame(root,width=350,height='390',bg='red')
frame.place()
heading=Label(frame,text='Payment Registeration',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

####################
##NAME#####

def on_enter(e):
    Name.delete(0,'end')
def on_leave(e):
    if Name.get() =='':
        Name.insert(0,'Name')
Name=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
Name.place(x=30,y=80)
Name.insert(0,'Enter Your Name')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
Name.bind("<FocusIn>",on_enter)
Name.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


##email id#####

def on_enter(e):
    email.delete(0,'end')
def on_leave(e):
    if email.get() =='':
        email.insert(0,'enter Your Email Id')
email=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
email.place(x=30,y=80)
email.insert(0,'Enter Your Email id')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
email.bind("<FocusIn>",on_enter)
email.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


##Phone Number#####

def on_enter(e):
    phn.delete(0,'end')
def on_leave(e):
    if phn.get() =='':
        phn.insert(0,'Phone Number')
phn=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
phn.place(x=30,y=80)
phn.insert(0,'Enter Your Phone Number')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
phn.bind("<FocusIn>",on_enter)
phn.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


##Age#####

def on_enter(e):
    age.delete(0,'end')
def on_leave(e):
    if age.get() =='':
        age.insert(0,'Age')
age=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
age.place(x=30,y=80)
age.insert(0,'Enter Your Age')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
age.bind("<FocusIn>",on_enter)
age.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


##Gender#####

def on_enter(e):
    gender.delete(0,'end')
def on_leave(e):
    if gender.get() =='':
        gender.insert(0,'Gender')
gender=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
gender.place(x=30,y=80)
gender.insert(0,'Enter Your Gender')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
gender.bind("<FocusIn>",on_enter)
gender.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


##Mode Of Payment#####

def on_enter(e):
    md.delete(0,'end')
def on_leave(e):
    if md.get() =='':
        md.insert(0,'Cash/Credit Card/Debit Card/GooglePay/other epay')
md=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
md.place(x=30,y=80)
md.insert(0,'Enter Your Payment Amount')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
md.bind("<FocusIn>",on_enter)
md.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


#Cash_Payment#####

def on_enter(e):
    csh.delete(0,'end')
def on_leave(e):
    if csh.get() =='':
        csh.insert(0,'Cash Payment Only!')
csh=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
csh.place(x=30,y=80)
csh.insert(0,'Enter Your CashAmount')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
csh.bind("<FocusIn>",on_enter)
csh.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


##Credit_card####

def on_enter(e):
    crid_crd.delete(0,'end')
def on_leave(e):
    if crid_crd.get() =='':
        crid_crd.insert(0,'Credit Card Only!')
crid_crd=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
Name.place(x=30,y=80)
crid_crd.insert(0,'Enter Your Credit Card Number')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
crid_crd.bind("<FocusIn>",on_enter)
crid_crd.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


#Debit_card#####

def on_enter(e):
    db_crd.delete(0,'end')
def on_leave(e):
    if db_crd.get() =='':
        db_crd.insert(0,'Debit Card Only!!')
db_crd=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
db_crd.place(x=30,y=80)
db_crd.insert(0,'Enter Your Debit Card Number')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
db_crd.bind("<FocusIn>",on_enter)
db_crd.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##gpay#####

def on_enter(e):
    gpy.delete(0,'end')
def on_leave(e):
    if gpy.get() =='':
        gpy.insert(0,'GPAY Only!')
gpy=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
gpy.place(x=30,y=80)
gpy.insert(0,'Scan GPay QR Code')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
gpy.bind("<FocusIn>",on_enter)
gpy.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#root.configure(bg='light green')
entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)
entry_4 = Entry(root)
entry_5 = Entry(root)
entry_6 = Entry(root)
entry_7 = Entry(root)
entry_8 = Entry(root)

entry_1.grid(row=1,column=1,)
entry_2.grid(row=2,column=1)
entry_3.grid(row=3,column=1)
entry_4.grid(row=4,column=1)
entry_5.grid(row=5,column=1)
entry_6.grid(row=6,column=1)
entry_7.grid(row=7,column=1)
entry_8.grid(row=8,column=1)

btn_=Button(root,text='Submit',bg='blue',font='Raleway')
btn_.grid(row=9,column=1)
root.mainloop ()