def views():
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
    mycursor.execute("select * from covid_19 where Phoneno='{}'".format(Phoneno))
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    else:
       print("No recors found")
    