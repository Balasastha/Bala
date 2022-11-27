class main:
  def values():
    
    import mysql.connector 

    mydb=mysql.connector.connect( 
          host="localhost", 
          user="root", 
          password="2001", 
          database="Covid_19_management_system"
          ) 

#value insertion 

#connection line 

    mycursor=mydb.cursor() 

#inserting values into database
    sql="insert into covid_19 (Name,Age,Bloodgroup,Phoneno,Address,District,State,Aadharno,Vaccination,Admit,Discharge,Status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 

    Name=input("Enter Name: ")
    try:
      Age=int(input("Enter Age: "))
    except:
      print("Type valid age")
      Age=int(input("Enter Age: "))
    Bloodgroup=input("Enter Bloodgroup: ")
    try:
      Phoneno=int(input("Enter Phone no: "))
    except:
      print("Enter valid Phoneno")
      Phoneno=int(input("Enter Phone no: "))
    Address=input("Enter Address: ")
    District=input("Enter district: ")
    State=input("Enter state: ")
    try:
      Aadharno=int(input("Enter aadhar no: "))
    except:
      print("Enter valid Aadharno")
      Aadharno=int(input("Enter aadhar no: "))
    Vaccinationdetails=input("Enter vaccination details (Yes[Y]/No[N]): ")
    if Vaccinationdetails=="Y":
      Vaccination=int(input("How many doses: "))
    elif Vaccinationdetails=="N":
        Vaccination="NA"
    else:
      print("Please enter only 'Y' or 'N'")
    try:
      Admit=input("Enter Date of Admit 'YYYY-MM-DD': ")
    except:
      print("Enter valid date 'YYYY-MM-DD'")
      Admit=input("Enter Date of Admit 'YYYY-MM-DD': ")
    try:
      Discharge=input("Enter Date of Discharge: ")
    except:
      print("Enter valid date 'YYYY-MM-DD'")
      Discharge=input("Enter Date of Discharge 'YYYY-MM-DD': ")
    Statusofpatient=input("Enter patient status Alive[A]/Dead[D]: ")
    if Statusofpatient=="A":
      Status="ACTIVE"
    elif Statusofpatient=="D":
      Status="INACTIVE"
    else:
      print("Please enter only 'A' or 'D'")


    val=(Name,Age,Bloodgroup,Phoneno,Address,District,State,Aadharno,Vaccination,Admit,Discharge,Status) 

    mycursor.execute(sql,val) 

    mydb.commit() 

    print("Row added suucessfully...")

# Continuation of adding another patient
  def extra():
    extra=input("Do You want to add another Patient Yes[Y]/No[N]: ")
    if extra=="Y":
      object.values()
      object.extra()
    elif extra=="N":
      import os
      import sys
      import covid
    else:
      print("Please enter only 'Y' or 'N'")
      
object=main
object.values()
object.extra()