import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2001",
    )

mycursor= db.cursor()
mycursor.execute("CREATE DATABASE ATM")
print("\nDatabase created successfully")



 