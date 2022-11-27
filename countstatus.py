def status():
  import mysql.connector 

  mydb=mysql.connector.connect( 
        host="localhost", 
        user="root", 
        password="2001", 
        database="Covid_19_management_system"
        ) 
  mycursor = mydb.cursor()
  query = "SELECT count(*) AS New_column_name FROM covid_19 where Status = 'ACTIVE'"
    
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  print("NO of ACTIVE Patients are: ",myresult[-1][-1])

  query = "SELECT count(*) AS New_column_name FROM covid_19 where Status = 'INACTIVE'"
    
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  print("NO of INACTIVE Patients are: ",myresult[-1][-1])

  query = "SELECT count(*) AS New_column_name FROM covid_19"
    
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  print("NO of total Patients are: ",myresult[-1][-1])
  mydb.close()


