first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
print("\nYour full name is " + first_name + " " + last_name)

# Firsts and lasts letters given

x = str(len(first_name))
print("Your first name length is " + x + " letters")

y = str(len(last_name))
print("Your last name length is " + y + " letters")

z = int(x) + int(y)

print("Your full name length is " + str(z) + " letters")

initial_name= first_name[:1]
print("\nFirst name starts with: ", initial_name)

initial_lastname= last_name[:1]
print("Last name starts with: ", initial_lastname)

end_name= first_name[-1:]
print("\nFirst name ends with: ", end_name)

end_lastname= last_name[-1:]
print("Last name ends with: ", end_lastname)

print("\nYour initials are: ", initial_name, initial_lastname)


