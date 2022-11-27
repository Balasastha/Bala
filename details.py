import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2001",
  database="ATM"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Accountdetails (Name,Accountno,Phoneno,Balance) VALUES (%s,%s,%s,%s)"
val = [
 ('Peter', '456743257890', '9514281390','1000'),
 ('Amy','345632148976', '9047417989','10000'),
 ('Hannah','453265437865', '9976486470','100000')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record was inserted.")