weight = float(input("Please enter your weight in (kg): "))
height = float(input("Now, enter your eight in (m): "))

BMI_result = weight / height ** 2

# rounded number to two decimals
#BMI_rounded = round(BMI_result * 100)/100

print("\nYour BMI is: %.2f" % BMI_result)

category = ""

if BMI_result < 18.5:
    category = "underweight"
elif BMI_result < 25:
    category = "normal"
elif BMI_result < 30:
    category = "overweight"
else:
    category = "obese"


print("\nYou are in the \"" + category + "\" range.")
