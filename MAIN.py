from tkinter import *
import os
from PIL import ImageTk,Image
from tkinter import messagebox
#from playsound import playsound

import profile


#OPENING SCREEN

master=Tk()
master.title("BANKING PAGE")
master.configure(bg="orange")
master.geometry("1275x800")
global dashboard_1
def changepass():

   b1=b.get()
   r1=r.get()
   l1=l.get()
   all_accounts=os.listdir()
   if b1=="" or r1=="" or l1=="" :
      #playsound("C:/Users/Darshan V/Downloads/ALLFIELDS.mp3")
      pin_change_notif_2.config(text="ALL FIELDS REQUIRED*",fg="red",font="stencil")
      
      return     
   if b1 in all_accounts :
         file=open(b1,"r")
         file_data=file.read()
         file_data=file_data.split('\n')
         mob_number=file_data[3]
      
         if not r1==mob_number:
           pin_change_notif_2.config(text="MOBILE NUMBER IS  INCORRECT!!!",fg="red",font=("stencil"))
           return
         if len(l1)<=4:
           pin_change_notif_2.config(text="PASSWORD SHOULD BE MORE THAN 4 CHARACTERS",fg="red",font=("stencil",17),bg="sky blue")
           return
         for i in l1:
              if not((ord(i)>=65 and ord(i)<=90) or( ord(i)>=97 and ord(i)<=122 ) or ord(i)==46 or ( ord(i)>=48 and ord(i)<=57 ) or ord(i)==64 ):
                pin_change_notif_2.config(fg='red',text="ENTER VALID PASSWORD \n PASSWORD CAN CONTAIN CAPITAL OR SMALL ALPHABETS \n, OR NUMBERS , AND ONLY '.' or '@' ARE ALLOWED",font=("calibri",15),bg="sky blue")
                return
        
         else:
                     
           file=open(b1,'r+')
           file_data=file.read()
           details=file_data.split('\n')
           current_pin=details[4]
           new_pin=l1
                  
           file_data=file_data.replace(current_pin,new_pin)
           file.seek(0)
           file.truncate(0)
           file.write(file_data)
           file.close()

           pin_change_notif_2.config(text="PIN CHANGED SUCCESSFULLY \n LOGIN WITH NEW CREDENTIALS TO CONTINUE",fg="green")
           Button(modify_screen,text="OK",command=lambda: [login(),modify_screen.destroy() ],font=("times new roman",20),borderwidth=4,bg="gold",fg="red").grid(row=9,sticky=W,pady=10,column=1)
            
   else :            
           pin_change_notif_2.config(text=" NO USER FOUND",fg="red")
           return
      
def modifypin():
  global modify_screen
  modify_screen=Tk()
  modify_screen.title("PIN CHANGE")
  modify_screen.configure(bg="sky blue")
  modify_screen.geometry("920x550")

  global c_name
  global c_num
  global n_pin
  global pin_change_notif_2
  global b
  global r
  global l
  
  
  c_name=StringVar()
  c_num =StringVar()
  n_pin=StringVar()

  Label(modify_screen,text="ENTER YOUR DETAILS TO CONTINUE",font=("calibri",26),bg="gold",fg="brown").grid(row=1,sticky=W,pady=10)
  Label(modify_screen,text="NAME           :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=2,sticky=W,pady=10)
  Label(modify_screen,text="MOBILE NUMBER  :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=4,sticky=W,pady=10)
  Label(modify_screen,text="PIN            :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=6,sticky=W,pady=10)

  pin_change_notif_2=Label(modify_screen,font=("calibri",17),bg="sky blue")
  pin_change_notif_2.grid(row=9,sticky=N,pady=10)
  
  b=Entry(modify_screen,textvariable=c_name,fg="green",font=("times new roman",25),borderwidth=4)
  b.grid(row=2,sticky=N,pady=10,column=1)
  r=Entry(modify_screen,textvariable=c_num,fg="green",font=("times new roman",25),borderwidth=4)
  r.grid(row=4,sticky=N,pady=10,column=1)
  l=Entry(modify_screen,textvariable=n_pin,fg="green",font=("times new roman",25),show="*",borderwidth=4)
  l.grid(row=6,sticky=N,pady=10,column=1)

  b.focus_set()
  
  Button(modify_screen,text="CHANGE PIN",command=changepass,fg="white",bg="green",font=("stencil",24)).grid(row=8,pady=50,sticky=E)

  modify_screen.mainloop()
def alterpin():

   g1=g.get()
   h1=h.get()
   j1=j.get()
   all_accounts=os.listdir()
   if g1=="" or h1=="" or j1=="" :
      #playsound("C:/Users/Darshan V/Downloads/ALLFIELDS.mp3")
      pin_change_notif.config(text="ALL FIELDS REQUIRED*",fg="red")
      
      return      
   if g1 in all_accounts :
         file=open(g1,"r")
         file_data=file.read()
         file_data=file_data.split('\n')
         mob_number=file_data[3]
      
         if not h1==mob_number:
           pin_change_notif.config(text="MOBILE NUMBER IS  INCORRECT!!!",fg="red")
           return
         if len(j1)<=4:
           pin_change_notif.config(text="PASSWORD SHOULD BE MORE THAN 4 CHARACTERS",fg="red",font=("stencil",17),bg="sky blue")
           return
         for i in j1:
              if not((ord(i)>=65 and ord(i)<=90) or( ord(i)>=97 and ord(i)<=122 ) or ord(i)==46 or ( ord(i)>=48 and ord(i)<=57 ) or ord(i)==64 ):
                pin_change_notif.config(fg='red',text="ENTER VALID PASSWORD \n PASSWORD CAN CONTAIN CAPITAL OR SMALL ALPHABETS \n, OR NUMBERS , AND ONLY '.' or '@' ARE ALLOWED",font=("calibri",15),bg="sky blue")
                return
        
         else:           
           file=open(g1,'r+')
           file_data=file.read()
           details=file_data.split('\n')
           current_pin=details[4]
           new_pin=j1
                  
           file_data=file_data.replace(current_pin,new_pin)
           file.seek(0)
           file.truncate(0)
           file.write(file_data)
           file.close()

           pin_change_notif.config(text="PIN CHANGED SUCCESSFULLY \n LOGIN WITH NEW CREDENTIALS TO CONTINUE",fg="green")
           Button(change_screen,text="OK",command=lambda: [login(),change_screen.destroy() or dashboard_1.destroy()],font=("times new roman",20),borderwidth=4,bg="gold",fg="red").grid(row=9,sticky=W,pady=10,column=1)
            
   else :            
           pin_change_notif.config(text=" NO USER FOUND",fg="red")
           return
      
def pinchange():
  global change_screen
  change_screen=Tk()
  change_screen.title("PIN CHANGE")
  change_screen.configure(bg="sky blue")
  change_screen.geometry("920x550")

  global Cname
  global Cnum
  global Npin
  global pin_change_notif
  global g
  global h
  global j
  
  
  Cname=StringVar()
  Cnum =StringVar()
  Npin=StringVar()

  Label(change_screen,text="ENTER YOUR DETAILS TO CONTINUE",font=("calibri",26),bg="gold",fg="brown").grid(row=1,sticky=W,pady=10)
  Label(change_screen,text="NAME           :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=2,sticky=W,pady=10)
  Label(change_screen,text="MOBILE NUMBER  :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=4,sticky=W,pady=10)
  Label(change_screen,text="PIN            :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=6,sticky=W,pady=10)

  pin_change_notif=Label(change_screen,font=("calibri",17),bg="sky blue")
  pin_change_notif.grid(row=9,sticky=N,pady=10)
  
  g=Entry(change_screen,fg="green",font=("times new roman",25),borderwidth=4)
  g.grid(row=2,sticky=N,pady=10,column=1)
  h=Entry(change_screen,textvariable=Cnum,fg="green",font=("times new roman",25),borderwidth=4)
  h.grid(row=4,sticky=N,pady=10,column=1)
  j=Entry(change_screen,textvariable=Npin,fg="green",font=("times new roman",25),show="*",borderwidth=4)
  j.grid(row=6,sticky=N,pady=10,column=1)

  g.focus_set()

  Button(change_screen,text="CHANGE PIN",command=alterpin,fg="white",bg="green",font=("stencil",24)).grid(row=8,pady=50,sticky=E)

  change_screen.mainloop()
  
#FUNCTIONS TO BE CALLED FROM DASHBOARD

def profile():
  file=open(login_name,"r")
  file_data=file.read()
  user_details=file_data.split('\n')
  user_name=user_details[0]
  user_age=user_details[1]
  user_gender=user_details[2]
  user_phno=user_details[3]
  user_balance=user_details[5]

  profile_screen=Tk()
  profile_screen.title("PERSONAL DETAILS>>")
  profile_screen.geometry("650x870")
  profile_screen.configure(bg="sky blue")

  if user_gender=='M':
    user_gender='MALE'
   
  elif user_gender=='F':
    user_gender='FEMALE'
    
  elif user_gender=='O':
    user_gender='OTHERS'
    
  #LABELS
  Label(profile_screen,text="PROFILE",font=("times new roman",30),fg="black",bg="gold").grid(row=1,sticky=E,pady=20)
  Label(profile_screen,text="NAME                     :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=2,sticky=W,pady=20)
  Label(profile_screen,text="AGE                         :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=4,sticky=W,pady=19)
  Label(profile_screen,text="GENDER                 :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=6,sticky=W,pady=19)
  Label(profile_screen,text="MOBILE NUMBER  :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=8,sticky=W,pady=19)
  Label(profile_screen,text="BALANCE              :",font=("times new roman",30),fg="sky blue",bg="black").grid(row=10,sticky=W,pady=19)

  Label(profile_screen,text=user_name,font=("times new roman",30),bg="sky blue").grid(row=2,sticky=W,pady=10,column=1,padx=10)
  Label(profile_screen,text=user_age,font=("times new roman",30),bg="sky blue").grid(row=4,sticky=W,pady=10,column=1,padx=10)
  Label(profile_screen,text=user_gender,font=("times new roman",30),bg="sky blue").grid(row=6,sticky=W,pady=10,column=1,padx=10)
  Label(profile_screen,text=user_phno,font=("times new roman",30),bg="sky blue").grid(row=8,sticky=W,pady=10,column=1,padx=10)
  Label(profile_screen,text="₹"+str(user_balance),font=("times new roman",30),bg="sky blue").grid(row=10,sticky=W,pady=10,column=1,padx=10)

  b1=Button(profile_screen,text="<<<BACK",command=profile_screen.destroy,font=("times new roman",30),fg="white",bg="purple")
  b1.grid(row=16,pady=10,sticky=E)

class withdraw:
    def debit():
      global debit_screen
      global v
      
      global debit_amount
      global debit_notif
      global current_balance_notif
      debit_amount=StringVar()
      file = open(login_name,"r")
      file_data=file.read()
      user_details=file_data.split('\n')
      balance_details=user_details[5]

      debit_screen=Toplevel(master)
      debit_screen.title("debit")
      debit_screen.geometry("850x550")
      debit_screen.configure(bg="sky blue")

      Label(debit_screen,text="DEBIT",fg="blue",font=("calibri",50)).grid(row=1,sticky=E)
      Label(debit_screen,text="AMOUNT :  ₹",font=("calibri",33),fg="sky blue",bg="black").grid(row=3,sticky=W,pady=35)
      Label(debit_screen,text="CURRENT BALANCE :",font=("calibri",33),fg="sky blue",bg="black").grid(row=4,sticky=W,pady=15)
      v=Label(debit_screen,text="₹"+user_details[5],font=("calibri",33),fg="sky blue",bg="black")
      v.grid(row=4,sticky=W,pady=15,column=1,padx=20)

      debit_notif=Label(debit_screen,font=("calibri",30),bg="sky blue")
      debit_notif.grid(row=7,sticky=W,pady=10,column=1,columnspan=2)

      en=Entry(debit_screen,textvariable=debit_amount,fg="green",font=("calibri",22),borderwidth=4)
      en.grid(row=3,sticky=W,pady=10,column=1,padx=20)
      en.focus_set()
      #Button(debit_screen,text="←BACK TO MAIN MENU",command=deposit_screen.destroy,font=("times new roman",22),fg="white",bg="purple").grid(row=5,sticky=W,pady=20,padx=80)
      x=Button(debit_screen,text="FINISH  ",command=withdraw.finish_debit,font=("calibri",28),fg="white",bg="green",borderwidth=4)
      x.grid(row=5,sticky=W,pady=40,column=1)
    def finish_debit():
      
        file=open(login_name,'r+')              #opening a file just to check if debiting amount less than the exixting balance before entering  else part 
        file_data=file.read()
        b=file_data.split('\n')
        a=b[5]
        for i in debit_amount.get():
           if not( ord(i)>=48 and ord(i)<=57 or ord(i)==46 and ord(i)==0):
            debit_notif.config(text="ENTER VALID AMOUNT*",fg="red",font=("stencil",18))
            return
           
        if debit_amount.get()=="" or float(debit_amount.get())<=0:
            debit_notif.config(text="ENTER VALID AMOUNT*",fg="red",font=("stencil",18))
            return

        elif float(debit_amount.get())>float(a):
             debit_notif.config(text="INSUFFICIENT BALANCE!!",fg="red")
             return
        else:
             file=open(login_name,'r+')
             file_data=file.read()
             details=file_data.split('\n')  
             current_balance=details[5]

             new_balance=current_balance
             new_balance=float(current_balance)-float(debit_amount.get())
             file_data=file_data.replace(current_balance,str(new_balance))
             file.seek(0)
             file.truncate(0)
             file.write(file_data)
             file.close()
             v.destroy()
            
             Label(debit_screen,text="₹"+str(new_balance),font=("calibri",33),fg="sky blue",bg="black").grid(row=4,sticky=W,pady=15,column=1,padx=20)
             
             debit_notif.config(text="AMOUNT DEBITED/WITHDRAWED",fg="green",font=("stencil",17))
class credit: 

    def deposit():
      global amount
      global deposit_notif
      global current_balance_notif

      global deposit_screen
      amount=StringVar()
      file = open(login_name,"r")
      file_data=file.read()
      user_details=file_data.split('\n')
      balance_details=user_details[5]

      deposit_screen=Toplevel(master)
      deposit_screen.title("DEPOSIT")
      deposit_screen.geometry("920x550")
      deposit_screen.configure(bg="sky blue")

      Label(deposit_screen,text="  DEPOSIT IN YOUR ACCOUNT Mr/Mrs "+login_name,fg="blue",font=("times new roman",18),bg="gold").grid(row=2,pady=20,sticky=E)
      Label(deposit_screen,text="AMOUNT :    ₹",font=("calibri",33),fg="sky blue",bg="black").grid(row=3,sticky=N,pady=10)
      Label(deposit_screen,text="CURRENT BALANCE :",fg="sky blue",bg="black",font=("calibri",33)).grid(row=4,sticky=N,pady=7)
      Label(deposit_screen,text="₹ "+user_details[5],fg="sky blue",bg="black",font=("calibri",33)).grid(row=4,sticky=N,pady=7,column=1)
      #Label(deposit_screen,text="  mm",bg="sky blue",fg="black",font=("calibri",33)).grid(row=,sticky=N,pady=7)

      current_balance_notif=Label(deposit_screen,font=("calibri",14),bg="sky blue")
      current_balance_notif.grid(row=6,sticky=N,pady=10)

      deposit_notif=Label(deposit_screen,font=("calibri",19),bg="sky blue")
      deposit_notif.grid(row=7,sticky=N,pady=20,padx=100)

      en=Entry(deposit_screen,textvariable=amount,fg="green",font=("calibri",20),relief="raised",borderwidth=4)
      en.grid(row=3,sticky=N,pady=10,padx=20,column=1)

      en.focus_set()

      x=Button(deposit_screen,text="PAY  ",command=credit.finish_deposit,font=("times new roman",25),fg="white",bg="purple",borderwidth=4)
      x.grid(row=5,sticky=W,pady=15,padx=180,column=1)
      Button(deposit_screen,text="←BACK TO MAIN MENU",command=deposit_screen.destroy,font=("times new roman",22),fg="white",bg="purple").grid(row=5,sticky=W,pady=20,padx=80)
  
  #deposit_screen.bind('<Return>',finish_deposit)


    def finish_deposit():
      global new_balance

      for i in amount.get():
        if not( ord(i)>=48 and ord(i)<=57 or ord(i)==46 and ord(i)==0):
          deposit_notif.config(text="ENTER VALID AMOUNT*",fg="red",font=("stencil",21),bg="sky blue")
          return
           
      if amount.get()=="" or float(amount.get())<=0:
        deposit_notif.config(text="ENTER VALID AMOUNT*",fg="red",font=("stencil",21),bg="sky blue")
        return
    
      else:
        file=open(login_name,'r+')
        file_data=file.read()
        details=file_data.split('\n')
        current_balance=details[5]
        new_balance=current_balance
        new_balance=float(current_balance)+float(amount.get())
        file_data=file_data.replace(current_balance,str(new_balance))
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        file.close()
        
        Label(deposit_screen,text="CURRENT BALANCE :",fg="sky blue",bg="black",font=("calibri",33)).grid(row=4,sticky=N,pady=7)
                                                                                                         
        Label(deposit_screen,text="₹ "+str(new_balance),fg="sky blue",bg="black",font=("calibri",33)).grid(row=4,sticky=N,pady=7,column=1)

        deposit_notif.config(text="BALANCE UPDATED",fg="dark blue",font=("stencil",23),bg="sky blue")

#FUNCTIONS TO BE CALLED


  
def dashboard(event):
    global login_name
    global login_password
    global dashboard_1


    login_password=temp_login_password.get()
    login_name=temp_login_name.get()
    all_accounts=os.listdir()
    for i in all_accounts:
      if login_name==i:
        file=open(i,"r")
        file_data=file.read()
        file_data=file_data.split('\n')
        password=file_data[4]

        if login_password==password:
             login_screen.destroy()
             dashboard_1=Tk()
             dashboard_1.title("DASHBOARD")
             dashboard_1.geometry("1280x800")
             dashboard_1.configure(bg="brown")


             #label
             Label(dashboard_1,text="WELCOME    "+login_name.upper(),font=("times new roman",45),fg="black",bg="sky blue").grid(row=0,sticky=N,pady=50,padx=400)

             #buttons
             Button(dashboard_1,text="  DEPOSIT ",command=credit.deposit,font=("stencil",30),relief="raised",borderwidth=6).grid(row=4,sticky=N,pady=10,padx=20)
             Button(dashboard_1,text="    DEBIT   ",command=withdraw.debit,font=("stencil",30),relief="raised",borderwidth=6).grid(row=6,sticky=N,pady=10,padx=20)
             Button(dashboard_1,text="  PROFILE ",command=profile,font=("stencil",30),relief="raised",borderwidth=6).grid(row=8,sticky=N,pady=10,padx=20)
             Button(dashboard_1,text="PIN CHANGE",command=pinchange,font=("stencil",26),relief="raised",borderwidth=6).grid(row=10,sticky=N,pady=10,padx=20)
             dashboard_1.mainloop()
             return
            
        else:
             error.config(text="PASSWORD INCORRECT!!!",fg="red")
             return
      else:
             error.config(text="ACCOUNT NOT FOUND  !!",fg="red")
      
        
  #LOGIN PAGE
def login():
    
    global temp_login_name
    global temp_login_password
    global error
    global login_screen
    
    temp_login_name=StringVar()
    temp_login_password=StringVar()
    
    login_screen=Toplevel(master)
    login_screen.title("LOGIN PAGE")
    login_screen.configure(bg="sky blue")
    login_screen.geometry("700x470")

    Label(login_screen,text="USERNAME :",font=("times new roman",25),fg="sky blue",bg="black").grid(row=1,sticky=W,pady=100,padx=100)
    Label(login_screen,text="PASSWORD :",font=("times new roman",25),fg="sky blue",bg="black").grid(row=2,sticky=W,pady=10,padx=100)

    u=Entry(login_screen,textvariable=temp_login_name,font=("Imprint MT Shadow",17),fg="dark blue",borderwidth=4)
    u.grid(row=1,column=1,sticky=N,pady=105)
    u.focus_set()
    Entry(login_screen,textvariable=temp_login_password,show="*",font=("MS Sans Serif",16),borderwidth=4).grid(row=2,column=1,sticky=N,pady=20)

    error=Label(login_screen,font=("stencil",17),bg="sky blue")
    error.grid(row=5,sticky=W,pady=10,padx=80)

    Button(login_screen,text="NEXT>>>",fg="white",bg="green",command=lambda:dashboard(1),font=("stencil",20)).grid(row=4,column=0,sticky=E,pady=20)
    login_screen.bind('<Return>',dashboard)
    

def check(x):
  try:
    type(int(x))=='int'
  except ValueError:
    notify.config(fg="red",text="MOBILE NUMBER MUST BE 10 DIGITS")
  
class signup:

    def register():
        #making temporary variables as global
        global temp_name
        global temp_age
        global temp_gender
        global temp_password
        global temp_mobileno
        global notify
        global temp_balance

        #assigning temp variables
        temp_name       =StringVar()
        temp_age        =StringVar()
        temp_gender     =StringVar()
        temp_password   =StringVar()
        temp_mobileno   =StringVar()
        temp_balance    =StringVar()
    #new window
    
        register_screen=Toplevel(master)
        register_screen.title("REGISTRATION SCREEN")
        register_screen.configure(bg="sky blue")
        register_screen.geometry("1290x800")
    
    #LABELS
        Label(register_screen,text="ENTER   YOUR   DETAILS   TO   CONTINUE",font=("ENGRAVERS MT",17),bg="sky blue",fg="black").grid(row=0,sticky=N,pady=5,padx=150)
        Label(register_screen,text="NAME",font=("times new roman",30),bg="black",fg="white").grid(row=1,sticky=W,pady=10,padx=100)
        Label(register_screen,text="AGE",font=("times new roman",30),bg="black",fg="white").grid(row=2,sticky=W,pady=10,padx=100)
        Label(register_screen,text="GENDER ",font=("times new roman",30),bg="black",fg="white").grid(row=3,sticky=W,pady=10,padx=100)
        Label(register_screen,text="MOBILE NUMBER",font=("times new roman",30),bg="black",fg="white").grid(row=4,sticky=W,pady=10,padx=100)
        Label(register_screen,text="PASSWORD",font=("times new roman",30),bg="black",fg="white").grid(row=5,sticky=W,pady=10,padx=100)
        Label(register_screen,text="INITIAL DEPOSIT",font=("times new roman",30),bg="black",fg="white").grid(row=6,sticky=W,pady=10,padx=100)
        

    #LABEL WITH NO TEXT --
        notify=Label(register_screen,font=("stencil",20),bg="sky blue")
        notify.grid(row=13,sticky=N)
        
    
    #ENTRY BOXES TO ENTER THE DETAILS REQUIRED
        a=Entry(register_screen,textvariable=temp_name,fg="blue",font=("Imprint MT Shadow",17),borderwidth=3,relief="raised")
        a.grid(row=1,sticky=N,pady=10,column=1)                                             #NAME ENTRY
        Entry(register_screen,textvariable=temp_age,fg="blue",font=("Imprint MT Shadow",17),relief="raised",borderwidth=3).grid(row=2,sticky=N,pady=10,column=1)    #AGE ENTRY
        Entry(register_screen,textvariable=temp_gender,fg="blue",font=("Imprint MT Shadow",17),borderwidth=3,relief="raised").grid(row=3,sticky=N,pady=10,column=1)#GENDER ENTRY
        m=Entry(register_screen,textvariable=temp_mobileno,fg="blue",font=("Imprint MT Shadow",17),borderwidth=3,relief="raised")
        m.grid(row=4,sticky=N,pady=10,column=1)
        a.focus_set()
   # m.focus_set()

        Entry(register_screen,textvariable=temp_password,show="*",font=("Imprint MT Shadow",17),borderwidth=3,fg="blue",relief="raised").grid(row=5,sticky=N,pady=10,column=1) #PASSWORD/PIN ENTRY
        Entry(register_screen,textvariable=temp_balance,font=("Imprint MT Shadow",17),fg="blue",relief="raised",borderwidth=3).grid(row=6,sticky=N,pady=10,column=1)
    
   #REGISTER BUTTON
        Button(register_screen,text="REGISTER",command=signup.after_reg,font=("candara",19),fg="white",bg="green").grid(row=8,sticky=N,pady=9,padx=400)
        Button(register_screen,text="←BACK",command=register_screen.destroy,font=("candara",19),fg="white",bg="green").grid(row=9,sticky=N,pady=6,padx=400)


    def after_reg():
        global name
        global age
        global gender
        global password
        global mobilenumber
        global init_deposit

        name=temp_name.get()
        age=temp_age.get()
        gender=temp_gender.get()
        password=temp_password.get()
        mobilenumber=temp_mobileno.get()
        init_deposit=temp_balance.get()

        all_accounts=os.listdir()
                
        for i in name:
              if not((ord(i)>=65 and ord(i)<=90) or( ord(i)>=97 and ord(i)<=122 ) or ord(i)==46):
                notify.configure(fg='red',text="ENTER VALID NAME",font=("stencil",17),bg="sky blue")
                return
               
        for i in gender:
              if not( ord(i)==77  or ord(i)==70 or ord(i)==79  ):
                notify.configure(fg='red',text="ENTER VALID GENDER 'M' for MALE ,'F' for FEMALE , 'O' for OTHERS",font=("stencil",17),bg="sky blue")
                return
               
        for i in init_deposit:
            if not( ord(i)>=48 and ord(i)<=57 or ord(i)==46):
              notify.config(text="ENTER VALID AMOUNT*",fg="red",font=("stencil",17),bg="sky blue")
              return
            
        for i in password:
              if not((ord(i)>=65 and ord(i)<=90) or( ord(i)>=97 and ord(i)<=122 ) or ord(i)==46 or ( ord(i)>=48 and ord(i)<=57 ) or ord(i)==64 ):
                notify.config(fg='red',text="ENTER VALID PASSWORD \n PASSWORD CAN CONTAIN CAPITAL OR SMALL ALPHABETS \n, OR NUMBERS , \n AND ONLY '.' or '@' ARE ALLOWED",font=("stencil",13),bg="sky blue")
                return
               
        if name=="" or age=="" or gender=="" or password=="" or mobilenumber=='' or init_deposit=='':

            notify.config(fg="red",text="ALL FIELDS ARE REQUIRED*",font=("stencil",17))
            #playsound("C:/Users/Darshan V/Downloads/ALLFIELDS.mp3")            
            return
         
        if len(password)<=4:
            notify.config(text="PASSWORD SHOULD BE MORE THAN 4 CHARACTERS",fg="red",font=("stencil",17),bg="sky blue")
            return
         
        if not mobilenumber.isdigit():
            notify.config(fg='red',bg="sky blue",text="MOBILE NUMBER MUST BE in digits",font=("stencil",17))
            return
         
        elif not age.isdigit():
            notify.config(fg='red',bg="sky blue",text="AGE MUST BE IN NUMBERS!!",font=("stencil",17))
            return
        
        elif int(age)<17 or int(age)>100:
            notify.configure(fg='red',text="SORRY!! IF YOUR AGE IS BELOW 17 or ABOVE 100, YOU ARE NOT ALLOWED TO REGISTER",font=("stencil",15))
            return
         

        elif len(mobilenumber)<10  or len(mobilenumber)>10:
            
            notify.config(fg='red',bg="sky blue",text="MOBILE NUMBER MUST BE 10 DIGITS!!",font=("stencil",17))
            return
                
        elif init_deposit=="0":
            notify.config(text="INITIAL DEPOSIT CANNOT BE EMPTY OR ZERO",fg="red",font=("stencil",17))
            return

        else:
            
            notify.config(fg="green",text="WAIT FOR A MOMENT , PROCESSING...")
            for name_check in all_accounts:
        
               if name==name_check:
                   notify.config(fg="red",text="USER ALREADY EXIST",font=("stencil",17))
                   return
               else:
                        
                new_file=open(name,'w')
                new_file.write(name+'\n')
                new_file.write(age+'\n')
                new_file.write(gender+'\n')
                new_file.write(mobilenumber+'\n')
                new_file.write(password+'\n')
                new_file.write(init_deposit+'\n')
                
                new_file.close()
                notify.config(fg="green",text="ACCOUNT HAS BEEN CREATED",font=("stencil",14))


#FOR IMAGE
img=Image.open('bank.jpg')

img=ImageTk.PhotoImage(img)
#Image.resize((450,450),Image.ANTIALIAS)
#labels

l1=Label(master,text="WELCOME TO OUR BANKING SITE", font=("calibri",35),bg="orange")
l1.grid(row=4,sticky=N,pady=10,padx=10)

l2=Label(master,text="MOST SECURE SITE",font=("times new roman",35),bg="orange")
l2.grid(row=2,sticky=N,pady=10,padx=10)

l1=Label(master,image=img ,font=("calibri",40),bg="orange")
l1.grid(row=1,sticky=NW,pady=10,padx=450)

#buttons
b1=Button(master,text="REGISTER WITH US",command=signup.register,font=('stencil',25),relief="raised",bg="green",fg="white",borderwidth=4)
b1.grid(row=6,sticky=N,pady=40,padx=1)

b2=Button(master,text="LOGIN ",command=login,font=("stencil",26),relief="raised",bg="green",fg="white",borderwidth=4)
b2.grid(row=7,pady=20,sticky=W,padx=350)

b3=Button(master,text="FORGOT PASSWORD ",command=modifypin,font=("stencil",24),relief="raised",bg="green",fg="white",borderwidth=4)
b3.grid(row=7,pady=20,sticky=E,padx=190)

master.mainloop()



