#Personal details
print("Name: Balasatha P")
print("Email: balasastha1002@gmail.com")
print("Phone no: 9514281390")
print("Batch: Python")
print("Batch no:74")

import os
import sys
import countstatus
import updating
import view
import delete

def menu_details():
  print("\n*****COVID-19 MANAGEMENT SYSTEM*****")
  print("\nChoose the option from below menu")
  print("\n 1.Add patient details\n 2.Update patient details\n 3.Count status of active and inactive patients\n 4.Delete a patient\n 5.View particular patient details\n 6.Exit")
  option=int(input("Enter a number: "))
  if option==1:
    import insert
    insert.main
  elif option==2:
    updating.update()
  elif option==3:
    countstatus.status()
  elif option==4:
    delete.deleting()
  elif option==5:
    view.views()
  elif option==6:
    print()
  else:
    print ("Enter only 1 to 6")

menu_details()







