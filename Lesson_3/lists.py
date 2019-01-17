list1 = [5, 10, 12, 8, 40]  # value in a list are called elements- homogenous list
list2 = [5, 10, "London"]  # heterogenous list

print(list1)
print(list2)

print(len(list1))  # numero degli elementi nella lista
print(len(list2))

print(max(list1))  # maximum value
print(min(list1))  # minimum value

# print(max(list2))  # non funziona con le stringhe presenti, solo con i numeri

print(list1 + list2)

print(list1 * 3)

#  slicing operations

print(list1[0])  # first element
print(list1[-1])  # last element
print(list1[2:])
print(list1[:5])
print(list1[-3:-1])

#  lists are mutable, changable at runtime (when the code is esecuted)


list1.append(101)  # add the element in the ened of the list
print(list1)

list1.insert(2, 202)  # aggiunge alla seconda posizione l'elemento
print(list1)

list1.extend([404, 303])  #  estende - aggiunge alla fine
print(list1)

list1[2:2] = [505, 606]   # aggiuge, inserisce più elementi senza eliminare - in
print(list1)


list1.pop()  # removes the element from the end or the specific position if pecified
print(list1)

x = list1.pop()  # removes the element from the end or the specific position if pecified
print(x)

list1.remove(101) # rimuove solo il primo se ce ne sonon 2 uguali
print(list1)



for x in list1:
    if x == 101:
        list1.remove(x)
print(list1)


del list1[1:5]
print(list1)

list1.clear() #removes all the elements of the list
print(list1)

#del list1 # rimuove dalla memoria
#print(list1)

list1 = [5, 23, 65, 33, 78, 651]
list1.reverse()
print(list1)

list1.sort()
print(list1)

list1.sort(reverse = True)
print(list1)














list2.reverse()
print(list2)

list2.sort()
print(list2)



