import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='2001',database='covid-19')
my_cusor=conn.cursor()

conn.commit()
conn.close()

print("connection succesfully created")