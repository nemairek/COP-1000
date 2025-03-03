# input statements
salary = 1250.0
numDependents = 2

# calculate taxes here
stateTax = (.065 * salary)
federalTax = (.28 * salary)
dependentDeduction = (salary * .025) * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding
# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
