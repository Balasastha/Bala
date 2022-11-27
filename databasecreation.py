#SQL Connection
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2001",
    )

mycursor= db.cursor()
mycursor.execute("CREATE DATABASE Covid_19_management_system")
print("Database created successfully")
