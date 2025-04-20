
AllowedVehiclesList = [ "Ford F-150", 
                       "Chevrolet Silverado", 
                       "Tesla CyberTruck", 
                       "Toyota Tundra", 
                       "Nissan Titan" ]
vehicleOption2 = ""
vehicleOption3 = ""

f = open('C:COP1000_Project-0-4\\data\\car.txt')
cars = f.read()
print(cars)
f.close()

db = open('C:COP1000_Project-0-4\\data\\car.txt', 'a')





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
 while True:
     vehicleOption3 = input("Please Enter the full Vehicle name you would like to add: ")    
     db.write("\n" + vehicleOption3)
     break          
 print("You have added '", vehicleOption3,"' as an authorized vehicle" ) 
if choice == 4:
 vehicleOption4 = input("Please Enter the full Vehicle name you would like to REMOVE:" )
 if vehicleOption4 != "":
     confirmation = input("Are you sure you want to remove ", vehicleOption4, " from the Authorized Vehicles List?:")
     if confirmation == "yes":
          for car in cars:
               if car == vehicleOption4:
                dl = open('C:COP1000_Project-0-4\\data\\car.txt', 'w')  
               elif car != vehicleOption4:
                    db.write(cars)         
               break
     elif confirmation == "no":
         quit()
elif choice == 5: 
        
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
      quit()



#Ford F-150
#Chevrolet Silverado
#Tesla CyberTruck
#Toyota Tundra
#Nissan Titan
#Rivian R1T
#Ram 1500
#practice1
#practice2