def deleting():
    import mysql.connector

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="2001",
        database="Covid_19_management_system"
    )
    mycursor=mydb.cursor()
    try:
      Phoneno=int(input("Enter Phone no: "))
    except:
      print("Enter valid Phoneno")
      Phoneno=int(input("Enter Phone no: "))
    sql = "DELETE FROM covid_19 WHERE Phoneno = '{}'".format(Phoneno)

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")
