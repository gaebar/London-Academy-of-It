'''
Exercise 1
'''

name = "Gaetano"
student_number = "ST012"
email_address = "gaetanobarreca@gmail.com"

print(name)
print(student_number)
print(email_address)

"""
Exercise 2
"""

print("\nExercise 2 \n")

multiply = (14 + 7)
subtract = (14-7)
multiply = (14 * 7)
divide = int(14/7)

print(multiply)
print(subtract)
print(multiply)
print(divide)

"""
Exercise 3 and 3.1
"""

print("\nExercise 3 \n")


print("1")
print("  2")
print("   3")
print("    4")
print("     5")

print("\nExercise 3.1\n")

for num in range(1, 6):
    for space in range(1, num):
        print(' ', end='')
    print(num)

"""
Exercise 4
"""
print("\nExercise 4 \n")

print('"SDK" stands for "Software Development Kit", whereas \n"IDE" stands for "Integrated Development Enviroment".')

"""
Exercise 5
"""
print("\nExercise 5 \n")

born_year = input("Please enter the year you were born: ")
age_2020 = 2020 - int(born_year)

print("You are born in " + str(born_year))
print("In the year 2020, you will be " + str(age_2020) + " years old!")

print("\nExercise 5.1 - using import\n")
import datetime

born_year = input("Please enter the year you were born: ")

now = datetime.datetime.now()
current_year = now.year
age_2020 = 2020 - int(born_year)

print("You are born in " + str(born_year))
print("In the year 2020, you will be " + str(age_2020) + " years old!")







