s1 = '''python is multi purpose programming language'''
print(s1)
print(len(s1))  # conta il numero dei caratteri e gli spazi

print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())
print(s1.swapcase())  # converte upper o lower
print("*" * 50)
print(s1)

# strings are immutable

print(s1.find("m"))  # da la posizione di prima occorrenza
print(s1.find("purpose"))

print(s1.find("m", 11))  #search from position 11 onwards

print(s1.find("m", 11, 30))  # from position 11 to 29

print(s1.startswith("python"))
print(s1.endswith("language"))
print(s1.endswith("x"))


print(s1.replace(' ', "-"))
print(s1)

print(s1.split())
print(s1.split("s"))
print("-".join(s1))

s2 = 'united kingdom'
v1, v2 = s2.split()
print(v1)
print(v2)

s3 = "radar"
s4 = "abcd1234"
s5 = "99999"

print(s3.lstrip("r"))  # l sta per left, rimuove il carattere da sinistra
print(s3.rstrip("r"))  # r sta per right
print(s3.strip("r"))  # rimuove tutti

print(s4.isalpha())  # alphabet
print(s4.isalnum())  # alphabet and numeric
print(s5.isdigit())  # numbers
print(s5.isalpha())


print(s1[-1])
print(s1[11:25])
print(s1[-10:-5])


