import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2001",
    database="Covid_19_management_system"
)

#database creation
#connectionline
mycursor=mydb.cursor()
#************************************************

mycursor.execute("CREATE TABLE covid_19 (Name varchar(255),Age int(3),Bloodgroup varchar(255),Phoneno Bigint(20),Address varchar(255),District varchar(255),State varchar(255),Aadharno Bigint(15),Vaccination varchar(255),Admit DATE,Discharge DATE,Status varchar(255))")
print("Table created succesfully")