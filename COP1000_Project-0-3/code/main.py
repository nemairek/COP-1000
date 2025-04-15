AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
vehicleOption2 = ""

with open("COP1000_Project-0-3\data\car.txt", "r") as db:
     options = db.read()
     db.close()

def menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print()
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")



menu()
choice = int(input("Select Choice:"))

if choice == 1:
     vehicleOption2 = ""
     print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
     [print(vehicle) for vehicle in AllowedVehiclesList]
     
elif choice == 2: 
     vehicleOption2 = str(input("Please Enter the full Vehicle name:"))
if vehicleOption2 == "":
     print()
elif vehicleOption2 in AllowedVehiclesList:
     print(vehicleOption2, end=" ")
     print("is an authorized vehicle")
elif vehicleOption2 not in AllowedVehiclesList:
     print(vehicleOption2, end=" ")
     print("is not an authorized vehicle, if you received this in error please check the spelling and try again")

if choice == 3:      
     vehicleOption3 = str(input("Please Enter the full Vehicle name you would like to add:"))
     for vehicle in AllowedVehiclesList:
      AllowedVehiclesList.append(vehicleOption3)
     print("You have added")
     print(vehicleOption3)
     print("as an authorized vehicle")
elif choice == 4: 
        
     print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
     quit()



