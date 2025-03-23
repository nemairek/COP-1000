"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 35
numChars = 8
color = "gold" 
woodType = "oak"

numChars = input("enter character amt: ")
color = input("enter color: ")
woodType = input("enter wood type: ")

# Charge for this sign.
# Number of characters.
# Color of characters.
# Type of wood.charge = 0
# Write assignment and if statements here as appropriate.
if int(numChars) > 5:
    charge = int(charge + 4 * (int(numChars) - 5))
elif int(numChars) <= 5:
    charge = int (charge + 0)

if str(woodType) == "oak": 
    charge = int(charge + 20)
elif str(woodType) != "oak":
    charge = int (charge + 0)

if str(color) == "gold":
    charge = int(charge + 15)
elif str(color) != "gold":
    charge = int(charge + 0)
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
