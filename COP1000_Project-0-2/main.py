AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


def menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print()
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")



menu()
choice = int(input("Select Choice:"))




if choice == 1:
     print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
     [print(vehicle) for vehicle in AllowedVehiclesList]

elif choice == 2: 
        vehicleSearch = str(input("Please Enter the full Vehicle name:"))
if vehicleSearch in AllowedVehiclesList:
             print(vehicleSearch, end=" ")
             print("is an authorized vehicle")
elif vehicleSearch not in AllowedVehiclesList:
     print(vehicleSearch, end=" ")
     print("is not an authorized vehicle, if you received this in error please check the spelling and try again")
elif choice == 3: 
        
     print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
     quit()



