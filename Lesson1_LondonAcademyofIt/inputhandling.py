name = input("Enter your name ")
number1 = int(input("Enter a number "))
number2 = int(input ("Enter next number "))
print(number1 + number2)
print("Sum of numbers is " + str(number1 + number2))
print("sum of " + str(number1) + ' and ' + str(number2) + ' is ' + str(number1 + number2))

print("Sum of %d and %d is %d" %(number1, number2, number1 + number2))
print("Hello %s, Sum of %d and %d is %d" %(name, number1, number2, number1 + number2))

# %d - integer
# %f - float
# %s - string
