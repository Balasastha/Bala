#Personal details
print("Name: Bala P")
print("Email: balasastha1002@gmail.com")
print("Phone no: 9514281390")
print("Batch: Python")
print("Batch no:74")

print("Welcome to BOI ATM")
print("\nPlease insert your card")
def views():
# connection lines
    import mysql.connector

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="2001",
        database="ATM"
    )
    mycursor=mydb.cursor()
    #Get phone no
    Phoneno=int(input("Enter Phone no: "))
    mycursor.execute("select Phoneno from Accountdetails where Phoneno={}".format(Phoneno))
    myresult = mycursor.fetchall()
    #Choose the language
    for x in myresult:
        print ("Entered Phone no is:",*x,sep='')
        print("\nSelect Language 1.English 2.Tamil")
        Lan=int(input("Enter number: "))
        if Lan==1:
        #Generate OTP
            import random
            otp_no=random.randint(1111,9999)
            print ("Your OTP is: ",otp_no)
            otp=int(input("Enter 4 digit OTP no: "))
            #Check for OTP
            if otp==otp_no:
                print("MENU")
                print("\n1.Quickcash \n2.Withdraw \n3.Balanceenquiry \n4.Cash Deposit")
                Option=int(input("Enter option number: "))
                #1. Quickcash
                if Option==1:
                    print("Choose your amount")
                    print("\n1.1000 \n2.2000 \n3.3000 \n4.4000 \n5.5000")
                #Enter the option for amount to withdraw
                    Choose=int(input("Enter option no: "))
                    if Choose==1:
                        #Fetch balance from database for entered Phoneno
                        mycursor.execute("Select Balance from Accountdetails where Phoneno={}".format(Phoneno))
                        myresult = mycursor.fetchall()
                        for x in myresult:
                        #Converting tuple to string
                            res = int(''.join(map(str, x)))
                            z = (str(res))
                            #Converting String to integer
                            q = int(z)
                            #Checking for enough balance available in account
                            if q>1000:
                                print("Withdraw successful")
                                remainbal=q-1000
                                bal=remainbal
                                #Updating remaining balance after withdraw into database
                                query = "update Accountdetails set Balance='{}' where Phoneno='{}'".format(bal,Phoneno)
                                mycursor.execute(query)
                                mydb.commit()
                                print("Available balance is: ",bal) 
                            else:
                                print("Not enough balance")  
                    #2.2000
                    elif Choose==2:
                        #Fetch balance from database for entered Phoneno
                        mycursor.execute("Select Balance from Accountdetails where Phoneno={}".format(Phoneno))
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            #Converting tuple to string
                            res = int(''.join(map(str, x)))
                            z = (str(res))
                            #Converting String to integer
                            q = int(z)
                            #Checking for enough balance available in account
                            if q>2000:
                                print("Withdraw successful")
                                remainbal=q-2000
                                bal=remainbal
                                #Updating remaining balance after withdraw into database
                                query = "update Accountdetails set Balance='{}' where Phoneno='{}'".format(bal,Phoneno)
                                mycursor.execute(query)
                                mydb.commit()
                                print("Available balance is: ",bal) 
                            else:
                                print("Not enough balance")
                                    #3.3000
                    elif Choose==3:
                        #Fetch balance from database for entered Phoneno
                        mycursor.execute("Select Balance from Accountdetails where Phoneno={}".format(Phoneno))
                        myresult = mycursor.fetchall()
                        for x in myresult:
                        #Converting tuple to string
                            res = int(''.join(map(str, x)))
                            z = (str(res))
                            #Converting String to integer
                            q = int(z)
                            #Checking for enough balance available in account
                            if q>3000:
                                print("Withdraw successful")
                                remainbal=q-3000
                                bal=remainbal
                                #Updating remaining balance after withdraw into database
                                query = "update Accountdetails set Balance='{}' where Phoneno='{}'".format(bal,Phoneno)
                                mycursor.execute(query)
                                mydb.commit()
                                print("Available balance is: ",bal) 
                            else:
                                print("Not enough balance")
                    #4.4000
                    elif Choose==4:
                        #Fetch balance from database for entered Phoneno
                        mycursor.execute("Select Balance from Accountdetails where Phoneno={}".format(Phoneno))
                        myresult = mycursor.fetchall()
                        #Converting tuple to string
                        for x in myresult:
                            res = int(''.join(map(str, x)))
                            z = (str(res))
                            #Converting String to integer
                            q = int(z)
                            #Checking for enough balance available in account
                            if q>4000:
                                print("Withdraw successful")
                                remainbal=q-4000
                                bal=remainbal
                                #Updating remaining balance after withdraw into database
                                query = "update Accountdetails set Balance='{}' where Phoneno='{}'".format(bal,Phoneno)
                                mycursor.execute(query)
                                mydb.commit()
                                print("Available balance is: ",bal) 
                            else:
                                print("Not enough balance")
                    #5.5000
                    elif Choose==5:
                        #Fetch balance from database for entered Phoneno
                        mycursor.execute("Select Balance from Accountdetails where Phoneno={}".format(Phoneno))
                        myresult = mycursor.fetchall()
                        for x in myresult:
                            res = int(''.join(map(str, x)))
                            #Converting tuple to string
                            z = (str(res))
                            #Converting String to integer
                            q = int(z)
                            #Checking for enough balance available in account
                            if q>5000:
                                print("Withdraw successful")
                                remainbal=q-5000
                                bal=remainbal
                                #Updating remaining balance after withdraw into database
                                query = "update Accountdetails set Balance='{}' where Phoneno='{}'".format(bal,Phoneno)
                                mycursor.execute(query)
                                mydb.commit()
                                print("Available balance is: ",bal) 
                            else:
                                print("Not enough balance")
                    else:
                        print ("Type only 1 to 5 only")
                #2. Withdraw
                elif Option==2:
                    withdraw=int(input("Enter amount to withdraw: "))
                    mycursor.execute("Select Balance from Accountdetails where Phoneno={}".format(Phoneno))
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        res = int(''.join(map(str, x)))
                        #Converting tuple to string
                        z = (str(res))
                        #Converting String to integer
                        q = int(z)
                        #Checking for enough balance available in account
                        if q>=withdraw:
                            print("Withdraw successful")
                            remainbal=q-withdraw
                            bal=remainbal
                            #Updating remaining balance after withdraw into database
                            query = "update Accountdetails set Balance='{}' where Phoneno='{}'".format(bal,Phoneno)
                            mycursor.execute(query)
                            mydb.commit()
                            print("Available balance is: ",bal)
                        else:
                            print("Not enough balance")
                #3. Balance Enquiry           
                elif Option==3:
                    #Fetch balance from database for entered Phoneno
                    mycursor.execute("Select Balance from Accountdetails where Phoneno={}".format(Phoneno))
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        res = int(''.join(map(str, x)))
                        #Converting tuple to string
                        z = (str(res))
                        #Converting String to integer
                        q = int(z)
                        print("Available balance is: ",q)
                #4. Cash deposit
                elif Option==4:
                    #Enter amount to be deposited
                    amt=int(input("How much do you want to deposit? "))
                    #Fetch balance from database for entered Phoneno
                    mycursor.execute("Select Balance from Accountdetails where Phoneno={}".format(Phoneno))
                    myresult = mycursor.fetchall()
                    for x in myresult:
                        res = int(''.join(map(str, x)))
                        #Converting tuple to string
                        z = (str(res))
                        #Converting String to integer
                        q = int(z)
                        #Calculating total balance after depositing
                        totalbal=amt+q
                        bal=totalbal
                        #Updating total balance after depositing into database
                        query = "update Accountdetails set Balance='{}' where Phoneno='{}'".format(bal,Phoneno)
                        mycursor.execute(query)
                        mydb.commit()
                        print("Amount deposited successfully")
                        print("Available balance is: ",bal)
                else:
                    print("Type only 1 to 4") 
            else:
                print("Incorrect OTP")
        elif Lan==2:
            print("Sorry!! Currently unavailable")
        else:
            print("Enter 1 or 2 only")
views()