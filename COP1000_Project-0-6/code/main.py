import json
import os
vehicleOption2 = ""
vehicleOption3 = ""
vehicleOption4 = ""
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan',]
with open("COP1000_Project-0-6/data/vehicles.json", 'w') as file:
        json.dump(AllowedVehiclesList, file)

def create(obj):
     if (not os.path.exists('COP1000_Project-0-6\\data\\car.json')):
        open('COP1000_Project-0-6\\data\\vehicles.json', mode='x')
     with open('COP1000_Project-0-6\\data\\vehicles.json', mode="w") as db:
          json.dump(obj, db)

def read():
     with open('COP1000_Project-0-6\\data\\vehicles.json', mode='r') as db:
         return json.load(db)

def update(vehicleOption3):
    with open('COP1000_Project-0-6\\data\\vehicles.json', mode="a") as db:
        json.dump(vehicleOption3, db)  

db = open('C:COP1000_Project-0-6\\data\\vehicles.json', 'a')

def deleteByName(obj):
     cars(AllowedVehiclesList)

cars = read()
#filtered_cars = deleteByName(obj = {"olist": cars, 'make': 'Chevy'})
#create(filtered_cars)

def menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print()
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

menu()
choice = int(input("Select Choice:"))


if choice == 1:
     print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
     print(cars)
elif choice == 2: 
     vehicleOption2 = str(input("Please Enter the full Vehicle name:"))
if vehicleOption2 == "":
     print()
elif vehicleOption2 in cars:
     print(vehicleOption2,"is an authorized vehicle" )
elif vehicleOption2 not in cars:
     print(vehicleOption2,"is not an authorized vehicle, if you received this in error please check the spelling and try again")
if choice == 3:      
     vehicleOption3 = input("Please Enter the full Vehicle name you would like to add: ") 
     if vehicleOption3 == "":
         print()
     elif vehicleOption3 != "": 
          update(vehicleOption3)  
if choice == 4:
 vehicleOption4 = input("Please Enter the full Vehicle name you would like to REMOVE:" )
 confirmation = input("Are you sure you want to remove ", vehicleOption4, " from the Authorized Vehicles List?:")
if vehicleOption4 == "yes":
     deleteByName(vehicleOption4)
elif vehicleOption4 == "no":
    quit()
elif choice == 5: 
        
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
      quit()
   
print("You have added '", vehicleOption3,"' as an authorized vehicle" ) 
