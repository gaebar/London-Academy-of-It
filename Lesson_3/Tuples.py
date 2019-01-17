t1 = (5, 10, 30, 25, 6)
t2 = ("London", 5.5, 10)
print(t1)
print(t2)
print(len(t1))
print(len(t2))
print(t1 + t2)
print(t1 * 3)
print(max(t1))
print(min(t1))

print(t1[2:4])
print(t1[-1])

#t1.append(202) # no possible! Tuple sono invariabili non possono essere cambiate o cancellate


list1 = list(t1) # cambiare il tuple in una lista e poi modificarla
list1.sort()
t1 = tuple(list1)
del list1
print(t1)


