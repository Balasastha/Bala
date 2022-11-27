def update():
  print("What to you want to update?")
  print("\n 1.Name\n 2.Age\n 3.Bloodgroup\n 4.Phoneno\n 5.Address\n 6.District\n 7.State\n 8.Aadharno\n 9.Vaccination\n 10.Admit\n 11.Discharge\n 12.Status\n")
  option=int(input("Enter a option: "))
  import mysql.connector 

  mydb=mysql.connector.connect( 
        host="localhost", 
        user="root", 
        password="2001", 
        database="Covid_19_management_system"
        ) 
  mycursor = mydb.cursor()
  
  if option==1:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     Name=input("Enter Name: ")
     query = "update covid_19 set Name='{}' where Phoneno={}".format(Name,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==2:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     try: 
        Age=int(input("Enter Age: "))
     except:
        print("Enter valid Phoneno")
        Age=int(input("Enter Age: ")) 
     query = "update covid_19 set Age={} where Phoneno={}".format(Age,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==3:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     Bloodgroup=input("Enter Bloodgroup: ")
     query = "update covid_19 set Bloodgroup='{}' where Phoneno={}".format(Bloodgroup,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==4:
     try:
        Aadharno=int(input("Enter patient Aadharno to update details: "))
     except:
        print("Enter valid Aadharno")
        Aadharno=int(input("Enter patient Aadharno to update details: ")) 
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     query = "update covid_19 set Phoneno='{}' where Aadharno={}".format(Phoneno,Aadharno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==5:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     Address=input("Enter Address: ")
     query = "update covid_19 set Address={} where Phoneno={}".format(Address,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==6:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     District=input("Enter District: ")
     query = "update covid_19 set District='{}' where Phoneno={}".format(District,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==7:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     State=input("Enter State: ")
     query = "update covid_19 set State='{}' where Phoneno={}".format(State,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==8:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     try:
        Aadharno=int(input("Enter patient Aadharno to update details: "))
     except:
        print("Enter valid Aadharno")
        Aadharno=int(input("Enter patient Aadharno to update details: ")) 
     query = "update covid_19 set Aadharno={} where Phoneno={}".format(Aadharno,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==9:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     Vaccinationdetails=input("Enter vaccination details (Yes[Y]/No[N]): ")
     if Vaccinationdetails=="Y":
        Vaccination=int(input("How many doses: "))
     elif Vaccinationdetails=="N":
        Vaccination="NA"
     else:
      print("Please enter only 'Y' or 'N'")
     query = "update covid_19 set Vaccination={} where Phoneno={}".format(Vaccination,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==10:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     try:
        Admit=input("Enter Date of Admit 'YYYY-MM-DD': ")
     except:
      print("Enter valid date 'YYYY-MM-DD'")
      Admit=input("Enter Date of Admit 'YYYY-MM-DD': ")
     query = "update covid_19 set Admit='{}' where Phoneno={}".format(Admit,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==11:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     try:
      Discharge=input("Enter Date of Discharge: ")
     except:
      print("Enter valid date 'YYYY-MM-DD'")
      Discharge=input("Enter Date of Discharge 'YYYY-MM-DD': ")
     query = "update covid_19 set Discharge='{}' where Phoneno={}".format(Discharge,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  elif option==12:
     try:
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     except:
        print("Enter valid Phoneno: ")
        Phoneno=int(input("Enter patient Phoneno to update details: "))
     Statusofpatient=input("Enter patient status Alive[A]/Dead[D]: ")
     if Statusofpatient=="A":
        Status="ACTIVE"
     elif Statusofpatient=="D":
      Status="INACTIVE"
     else:
      print("Please enter only 'A' or 'D'")
     query = "update covid_19 set Status='{}' where Phoneno={}".format(Status,Phoneno)
     mycursor.execute(query)
     mydb.commit()
     print("Updated successfully")
  else:
     print("Print only 1 to 10")
