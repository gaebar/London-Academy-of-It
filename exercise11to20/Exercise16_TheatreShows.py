preference = input("Would you like to see a comedy (yes/not)? ")
if preference == 'yes':
    print("You might like either ...")
else:
    preference = input("Would you like to see a musical (yes/not)? ")
    if preference == "yes":
        print("You might like ...")
    else:
        print("You might like either The woman in black or Macbeth")