import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="2001",
    database="ATM"
)

#database creation
#connectionline
mycursor=mydb.cursor()
#************************************************

mycursor.execute("CREATE TABLE Accountdetails (Name varchar(255),Accountno Bigint(15),Phoneno Bigint(20),Balance Bigint(20))")
print("Table created succesfully")