
# Alberto's way:

name = input("Please enter your name: ")
name_lenght = len(name)
name_crypto: str = ""

for letter in name:
    if name_crypto == "":
        name_crypto += letter
    elif len(name_crypto) == name_lenght-1:
        name_crypto += letter
    else:
        name_crypto += "*"


print("Encrypted form is ", name_crypto)



# professor's way:
name = input("Please enter your name: ")
print(name[0] + '*' *(len(name)-2) + name[-1])