from scipy.optimize import minimize

# Ask for input data: discount rates and corresponding sales

print("Enter the previous sales data and their respective discounts")
print(" ")

discount1 = int(input("Enter the first discount rate: "))
sales1 = int(input("Enter the number of sales made at this discount rate: "))

discount2 = int(input("Enter the second discount rate: "))
sales2 = int(input("Enter the number of sales made at this discount rate: "))

# Calculate the angular coefficient of the line that connects the two data points

M = ((discount2 - discount1)/(sales2 - sales1))

# Define a function that represents the revenue as a function of the discount rate
# Note that we multiply the function by -1 so that the minimize function will find the maximum instead of the minimum

def R(x):
    return -((M*(sales2-x) + discount2)*x)

# Find the optimal discount rate that maximizes revenue
# The minimize function is used to maximize the R function

maxsales = minimize(R,1)

# Calculate the optimal discount rate and expected revenue

Dmaxrevenue = discount2 - M*(int(maxsales.x)-sales2)

print(" ")
print("Suggested discount rate:")
print(float(Dmaxrevenue))
print(" ")
print("Expected number of sales:")
print(int(maxsales.x))
print(" ")
print("Expected revenue:")
print(float(Dmaxrevenue*maxsales.x))



