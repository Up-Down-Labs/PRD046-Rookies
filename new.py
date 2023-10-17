import os
import csv
import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk as tt
from tkinter import *
from hashlib import sha256
from datetime import date


win=tk.Tk()
wWidth=win.winfo_screenwidth()
wHeight=win.winfo_screenheight()
win.geometry("%dx%d"%(wWidth,wHeight))
win['bg']="white"
win.title("PASSWORD MANAGER")

reg=Toplevel()
reg.withdraw() 
report=Toplevel()
report.withdraw()

bg1=PhotoImage(file="C:\PROJECT\PasswordManager\images\header1.png")
Label(win,image=bg1).place(x=10,y=24)

def c1():
     s=Toplevel()
     
     s.title("Details")
     wWidth=s.winfo_screenwidth()
     wHeight=s.winfo_screenheight()
     s.geometry("%dx%d"%(wWidth,wHeight))
     s['bg']="white"
     s.deiconify()
     def getsex():
          return Gender.get()
     
     def commit():
          
          rowcount=0
          #read data from PMdata
          l=[]
          for i in open("C:\PROJECT\PMSigndata.csv"):
               l.append(i[0])
               
          file=open("C:\PROJECT\PMSigndata.csv","a+",newline='')
          # get input data
          fname=t1.get()
          lname=t2.get()
          ph=t3.get()
          ps=t4.get()
          email=t5.get()
          dob=t6.get()
          gen=getsex()


          #validate input data
          if len(fname)==0:
               messagebox.showwarning("Empty","Enter First Name")
          elif not(fname.isalpha()):
               messagebox.showwarning("Invalid ","Enter Valid First Name")     
          elif len(lname)==0:
               messagebox.showwarning("Empty","Enter Last Name")
          elif not(lname.isalpha()):
               messagebox.showwarning("Invalid ","Enter Valid Last Name")               
          elif len(ph)==0:
               messagebox.showwarning("Empty","Enter Mobile Number")
          elif not(ph.isdigit()) or len(ph)!=10:
               messagebox.showwarning("Invalid ","Enter Valid Mobile Number ")
          elif len(email)==0:
               messagebox.showwarning("Empty","Enter Email")
          elif '@'not in email or '.'not in email:
               messagebox.showwarning("Invalid ","Enter Valid Email")
          elif len(dob)==0:
               messagebox.showwarning("Empty","Enter Date of birth")
          elif not(dob.isdigit()):
               messagebox.showwarning("Invalid ","Enter Valid Date of birth")
          else:
                    #generate random user id
                    while True:
                         userID=random.randint(1,1000)
                         if userID not in l:
                              break

                    #encrypt passwd and save it
                    ems=sha256(email.encode('utf-8')).hexdigest()

                    #write user input to file    
                    wobj=csv.writer(file)
                    wobj.writerow([userID,fname,lname,ph,email,dob,gen,ems])
                    messagebox.showinfo("Success","Kindly note the Registration ID")
                    messagebox.showinfo("Success"," Registration ID : "+str(userID))

          #clears user input
          e1.delete(0,END)
          e2.delete(0,END)
          e3.delete(0,END)
          e5.delete(0,END)
          e6.delete(0,END)
                    
          file.close()
          regcard=Toplevel()
                   
          regcard.mainloop()
     
     def close():
          s.withdraw()
          win.deiconify()
          
     #_____________________ ___________________________________________________________________________________________________________
          
     t1=tk.StringVar()
     t2=tk.StringVar()
     t3=tk.StringVar()
     t4=tk.StringVar()
     t5=tk.StringVar()
     t6=tk.StringVar()  
     Gender=tk.StringVar()
     Gender.set('')
     s['bg']='lavender'

     Label(s,text="Registration form",font=("agency FB",46), bg="lavender", fg="black").place(x=455,y=50)
     
     a,b=100,200
     Label(s,text="First Name ",font=("agency FB",25), bg="lavender", fg="Black").place(x=a,y=b) 
     b=b+50
     Label(s,text="Last Name ",font=("agency FB",25), bg="lavender", fg="Black").place(x=a,y=b)
     b=b+50
     Label(s,text="Mobile Number ",font=("agency FB",25), bg="lavender", fg="Black").place(x=a,y=b)
     b=b+50
    
     a=675
     b=200
     Label(s,text="Email ID ",font=("agency FB",25), bg="lavender", fg="Black").place(x=a,y=b)
     b=b+50
     Label(s,text="Date of birth ",font=("agency FB",25), bg="lavender", fg="Black").place(x=a,y=b)
     b=b+50
     Label(s,text="Gender ",font=("agency FB",25), bg="lavender", fg="Black").place(x=a,y=b)
     b=b+50
     
     a=325
     b=210
     e1=Entry(s,textvariable=t1,font=("Arial",16))
     e1.place(x=a,y=b)
     
     b=b+50
     e2=Entry(s,textvariable=t2,font=("Arial",16))
     e2.place(x=a,y=b)
     
     b=b+50
     e3=Entry(s,textvariable=t3,font=("Arial",16))
     e3.place(x=a,y=b)

     a=875
     b=210
     e5=Entry(s,textvariable=t5,font=("Arial",16))
     e5.place(x=a,y=b)
     
     b=b+50
     e6=Entry(s,textvariable=t6,font=("Arial",16))
     e6.place(x=a,y=b)
     
     b=b+50
     rb=Radiobutton(s,text="Male", value="M", variable=Gender,bg="lavender",font=("agency FB",25), command=getsex)
     rb.place(x=a,y=b)    
     a=a+80
     rb2=Radiobutton(s,text="Female", value="F", variable=Gender,bg="lavender", font=("agency FB",25),command=getsex)
     rb2.place(x=a,y=b)
          
     a=875
     b=475
     Button(s,text="Commit",borderwidth=5,font=("Comic sans serif",12),height=1,command=commit, width=10).place(x=a,y=b)
     a=a+120
     Button(s,text="Close",width=10,font=("Comic sans serif",12), height=1,borderwidth=5,command=close).place(x=a,y=b)
#______________________________________________________________________________________________________________________________________________________

def c2():
     s=Toplevel()     
     s.title("LOG IN")
     w1=s.winfo_screenwidth()
     h1=s.winfo_screenheight()
     s.geometry("%dx%d"%(w1,h1))
     s['bg']="white"
     s.deiconify()

     def p3():
          s=Toplevel()
          s.title("Password Management")
          w1=s.winfo_screenwidth()
          h1=s.winfo_screenheight()
          s.geometry("%dx%d"%(w1,h1))
          s['bg']='lavender'
          s.deiconify()

          Label(s,text="Welcome Back !!",font=("agency FB",38), bg="lavender", fg="Black").place(x=50,y=8)
          Button(s,text="Add Password",borderwidth=5,font=("Comic sans serif",18),height=1,width=13, command=p4).place(x=50,y=100)
          Button(s,text="Edit Password",borderwidth=5,font=("Comic sans serif",18),height=1,width=13, command=p5).place(x=50,y=160)
          Button(s,text="Logout",borderwidth=5,font=("Comic sans serif",18),height=1,width=13, command=p2).place(x=50,y=220)
 
          Label(s,text="Application",font=("agency FB",30), bg="lavender", fg="Black").place(x=290,y=100)
          Label(s,text="Account Name",font=("agency FB",30), bg="lavender", fg="Black").place(x=470,y=100)
          Label(s,text="Password",font=("agency FB",30), bg="lavender", fg="Black").place(x=690,y=100)
          Label(s,text="Last Updated",font=("agency FB",30), bg="lavender", fg="Black").place(x=850,y=100)

          a=290
          b=170
              
          with open("C:\PROJECT\PasswordManager\Data.csv","r") as f:
            re=csv.reader(f)
            k=0

            for i in re:
               if i[0]==flag:
                 Label(s, text=i[1],bg="lavender", fg="Black", font=("agency FB",20)).place(x=a,y=b)
                 Label(s, text=i[2],bg="lavender", fg="Black", font=("agency FB",20)).place(x=470,y=b)
                 Label(s, text=i[3],bg="lavender", fg="Black", font=("agency FB",20)).place(x=690,y=b)
                 Label(s, text=i[4],bg="lavender", fg="Black", font=("agency FB",20)).place(x=850,y=b)
               
                 b=b+50
                 k=k+1        
                    
          regcard=Toplevel()
          regcard.mainloop()
          
     def p1():
          global flag
          rowcount=0
          l=[]
          for i in open("C:\PROJECT\PMSigndata.csv"):
               l.append(i[0])
               
          file=open("C:\PROJECT\PMSigndata.csv","a+",newline='')    
          reg=t4.get()
          email=t5.get()
     
          
          if len(email)==0:
               messagebox.showwarning("Empty","Enter Email")
          elif '@'not in email or '.'not in email:
               messagebox.showwarning("Invalid ","Enter Valid Email")
          elif len(reg)==0:
               messagebox.showwarning("Empty","Enter Registration ID")
          else:
                    
                    file.close()

                    #to do
                    isvalidEmail=0
                    isvalidReg=0

                    with open("C:\PROJECT\PMSigndata.csv","r") as f:
                      re=csv.reader(f)
                      k=0
          
                      for i in re:
                         if i[4]==email:
                              isvalidEmail=1
                              if i[0]==reg:
                                   isvalidReg=1
                                   flag=reg
                                   messagebox.showinfo("Valid", "Login Success")
                                   s.withdraw()
                                   p3()
                                   break
                    if isvalidEmail==0:
                         messagebox.showwarning("Warning", "Invalid Email.")
                    elif isvalidReg==0:
                         messagebox.showwarning("Warning", "Registeration ID is not found.")
                         
     def p2():
          s.withdraw()
          win.deiconify()

     def p6():
          #read data from PMPassword
          l=[]
          for i in open("C:\PROJECT\PasswordManager\PMPassword.csv"):
               l.append(i[0])
               
          file1=open("C:\PROJECT\PasswordManager\PMPassword.csv","a+",newline='')
          file2=open("C:\PROJECT\PasswordManager\Data.csv","a+",newline='')
          # get input data
          app=t1.get()
          acc=t2.get()
          ps=t3.get()

          #validate input data
          if len(app)==0:
               messagebox.showwarning("Empty","Enter Application")
          elif not(app.isalpha()):
               messagebox.showwarning("Invalid ","Enter Valid Application")     
          elif len(acc)==0:
               messagebox.showwarning("Empty","Enter Account Name")
          elif not(acc.isalpha()):
               messagebox.showwarning("Invalid ","Enter Valid Account Name")     
          elif len(ps)==0:
               messagebox.showwarning("Empty","Enter Password")
          else:

               #encrypt passwd and save it
               eps=sha256(ps.encode('utf-8')).hexdigest()

               #datetime
               d=date.today()
               
               #write user input to file    
               wobj1=csv.writer(file1)
               wobj1.writerow([flag,app,acc,eps,d])
               messagebox.showinfo("Success","Password Added")

               wobj2=csv.writer(file2)
               wobj2.writerow([flag,app,acc,ps,d])

          #clears user input
          e1.delete(0,END)
          e2.delete(0,END)

          file1.close()
          file2.close()
          regcard=Toplevel()
          regcard.mainloop()

          s.withdraw()
          s.deiconify()
          
     def p4():
          
          s=Toplevel()
          s.title("Add Password")
          w1=s.winfo_screenwidth()
          h1=s.winfo_screenheight()
          s.geometry("%dx%d"%(w1,h1))
          s['bg']='lavender'
          s.deiconify()

          Label(s,text="Add Password",font=("agency FB",46), bg="lavender", fg="Black").place(x=500,y=60)
          a,b=370,190
          Label(s,text="Application ", font=("agency FB",30), bg="lavender", fg="Black").place(x=a,y=b) 
          b=b+50
          Label(s,text="Account Name ", font=("agency FB",30), bg="lavender", fg="Black").place(x=a,y=b)
          b=b+50
          Label(s,text="Password", font=("agency FB",30), bg="lavender", fg="Black").place(x=a,y=b)
          b=b+50
     
          a=590
          b=210
          e1=Entry(s,textvariable=t1,font=("Arial",16))
          e1.place(x=a,y=b)
          b=b+50
          e2=Entry(s,textvariable=t2,font=("Arial",16))
          e2.place(x=a,y=b)
          b=b+50
          e3=Entry(s,textvariable=t3,font=("Arial",16))
          e3.place(x=a,y=b)
          b=b+50

          a=575
          b=400
          Button(s,text="Add",borderwidth=5,font=("Comic sans serif",13),height=1, width=10, command=p6).place(x=a,y=b)
          a=a+140
          Button(s,text="Close",width=12,font=("Comic sans serif",13),height=1,borderwidth=5, command=p3).place(x=a,y=b)

     def p5():
          
          s=Toplevel()
          s.title("View")
          w1=s.winfo_screenwidth()
          h1=s.winfo_screenheight()
          s.geometry("%dx%d"%(w1,h1))
          s['bg']='lavender'
          s.deiconify()

          Label(s,text="Password",font=("agency FB",46), bg="lavender", fg="Black").place(x=500,y=60)
          a,b=370,190
          Label(s,text="Application ", font=("agency FB",30), bg="lavender", fg="Black").place(x=a,y=b) 
          b=b+50
          Label(s,text="Account Name ", font=("agency FB",30), bg="lavender", fg="Black").place(x=a,y=b)
          b=b+50
          Label(s,text="Password", font=("agency FB",30), bg="lavender", fg="Black").place(x=a,y=b)
          b=b+50
     
          a=590
          b=210
          e1=Entry(s,textvariable=t1,font=("Arial",16))
          e1.place(x=a,y=b)
          b=b+50
          e2=Entry(s,textvariable=t2,font=("Arial",16))
          e2.place(x=a,y=b)
          b=b+50
          e3=Entry(s,textvariable=t3,font=("Arial",16))
          e3.place(x=a,y=b)
          b=b+50

          a=575
          b=400
          Button(s,text="Update",borderwidth=5,font=("Comic sans serif",13),height=1, width=10).place(x=a,y=b)
          a=a+140
          Button(s,text="Delete",width=12,font=("Comic sans serif",13),height=1,borderwidth=5).place(x=a,y=b)
          a=a+140
          Button(s,text="Close",width=12,font=("Comic sans serif",13),height=1,borderwidth=5, command=p3).place(x=a,y=b)

     t1=tk.StringVar()
     t2=tk.StringVar()
     t3=tk.StringVar()
     t4=tk.StringVar()
     t5=tk.StringVar()
     s['bg']='lavender'

     Label(s,text="Login",font=("agency FB",46), bg="lavender", fg="Black").place(x=575,y=50)
     a,b=330,190

     Label(s,text="Email ID ", font=("agency FB",30), bg="lavender", fg="Black").place(x=a,y=b) 
     b=b+50
     Label(s,text="Registration ID", font=("agency FB",30), bg="lavender", fg="Black").place(x=a,y=b)
     b=b+50
     
     a=530
     b=210
     e1=Entry(s,textvariable=t5,font=("Arial",16))
     e1.place(x=a,y=b)
     b=b+50
     e2=Entry(s,textvariable=t4,font=("Arial",16))
     e2.place(x=a,y=b)
     b=b+50
   
     a=525
     b=350
     Button(s,text="Submit",borderwidth=5,font=("Comic sans serif",12),height=1,command=p1, width=10).place(x=a,y=b)
     a=a+120
     Button(s,text="Close",width=10,font=("Comic sans serif",12),height=1,borderwidth=5, command=p2).place(x=a,y=b)
#____________________________________________________________________________________________________________________________________________________
     
Button(win, text="LOG IN",font=("Comic sans serif",19), height=1, width=8,borderwidth=5, command=c2).place(x=1110,y=465)
Button(win, text="SIGN UP",font=("Comic sans serif",19), height=1, width=8,borderwidth=5,command=c1).place(x=1110,y=525)

