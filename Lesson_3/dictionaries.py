#  SymbolToName=""
symbol_to_name = {
"H": "hydrogen",  # key and(:) value
"He": "helium",
"Li": "lithium",
"C": "caron",
"O": "oxygen",
"N": "nitrogen",
"N": "nitrogen2"  # se aggiungiamo un secondo valore, il secondo prende il posto del primo. Lo sostituisce
}

print(symbol_to_name)
print(len(symbol_to_name))

print(symbol_to_name.keys())  # list of keys only
print(symbol_to_name.values())  # list of values
print(symbol_to_name.items())  # list of key, value tuple


print(symbol_to_name["He"])

symbol_to_name.update({"Mg": "Magnesium", "Ni": "Nichel"})
print(symbol_to_name)  # adding elements at runtime

symbol_to_name["N"] = "Nitrogen"  # sostituisce il valore
print(symbol_to_name)

del symbol_to_name["Mg"]
print(symbol_to_name)

for key, value in symbol_to_name.items():
    print("Key is %s and Value is %s" % (key, value))


