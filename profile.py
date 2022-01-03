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

  if user_gender=='M':
    user_gender='MALE'
   
  elif user_gender=='F':
    user_gender='FEMALE'
    
  elif user_gender=='O':
    user_gender='OTHERS'
    
  #LABELS
  Label(profile_screen,text="NAME           :"+user_name,font=("calibri",17)).grid(row=2,sticky=N,pady=10)
  Label(profile_screen,text="AGE            :"+user_age,font=("calibri",17)).grid(row=4,sticky=N,pady=10)
  Label(profile_screen,text="GENDER         :"+user_gender,font=("calibri",17)).grid(row=6,sticky=N,pady=10)
  Label(profile_screen,text="MOBILE NUMBER   :"+user_phno,font=("calibri",17)).grid(row=8,sticky=N,pady=10)
  Label(profile_screen,text="BALANCE  :"+user_balance,font=("calibri",17)).grid(row=10,sticky=N,pady=10)

  profile_screen.mainloop()
