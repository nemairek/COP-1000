bonus = 0
name = "John Smith"
shifts = int(32)
transactions = int(23)
transactionValue = int(00.00)
# productivityScore = int(0)

name = input("Enter Name:")
shifts = input("Enter shift number:")
transactions = input("Enter number of transactions:")
transactionValue = input("Enter value of transactions:")

transactionAverage = int(transactionValue) / int(transactions)

productivityScore = int(transactionAverage) / int(shifts)

if productivityScore <= 30:
     bonus = 50
elif productivityScore >= 31 and productivityScore <= 69:
     bonus = 75
elif productivityScore >= 70 and productivityScore <= 199:
     bonus = 100
elif productivityScore >= 200:
     bonus = 200

print("Employee Name:" + str(name) )
print("Employee Bonus:$" + str(bonus))
