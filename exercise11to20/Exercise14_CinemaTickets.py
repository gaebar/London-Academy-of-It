age = int(input("Enter your age: "))

if age <= 16:
    print("your ticket costs £3")
elif age >= 60:
    print("your ticket costs £2")
else:
    print("your ticket costs £6")

#print("your ticket costs £2") if age <= 16 and >= 60 else print("your ticket costs £6")

#if age <= 16 and age >=60 print("your ticket cost £2") else print("your tickets costs £6")