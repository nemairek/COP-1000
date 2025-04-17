
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
vehicleOption2 = ""
vehicleOption3 = ""

f = open('C:COP1000_Project-0-3\\data\\car.txt')
cars = f.read()
print(cars)
f.close()






db = open('C:COP1000_Project-0-3\\data\\car.txt', 'a')


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
 while True:
     vehicleOption3 = input("Please Enter the full Vehicle name you would like to add: ")    
     db.write("\n" + vehicleOption3)
     break          
 print("You have added", vehicleOption3,"as an authorized vehicle" )   
elif choice == 4: 
        
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
      quit()



