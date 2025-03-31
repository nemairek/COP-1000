AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


def menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print()
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")



menu()
choice = int(input("Select Choice:"))



if choice == 1:
     print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
     [print(vehicle) for vehicle in AllowedVehiclesList]

elif choice == 2: 
        
     print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
     quit()



