print("\nExercise 10\n")
print("Doctor Who Festival - Price Calculator \nNote: enter 0 if none\n")

# ask for user input and convert to integer
individuals = int(input("Enter total number of individuals: "))
youngsters = int(input("Enter total number of under 16s: "))
families = int(input("Enter total number of families: "))

# set ticket prices
individual_price = 68
youngsters_price = 32.25
families_price = 42.75

# calculates totals by category
individuals_total = individuals * individual_price
youngsters_total = youngsters * youngsters_price
families_total = families*families_price

# calculates totals
total_persons = individuals + youngsters + families * 4
total_event = individuals_total + youngsters_total + families_total

# display totals to the users
print("\nCategory Price Breakdown: ")
print("Price is £" + str(individuals_total) + " for individuals")
print("Price is £" + str(youngsters_total) + " for under 16async")
print("Price is £" + str(families_total) + " for families\n")

print("Total Persons are", total_persons)
print("Total Event Price is £" + str(total_event))
print("More info and booking visit our website")