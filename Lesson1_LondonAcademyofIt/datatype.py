print ("Hello world") #comments a statemant, disables
a = 5 # int
b = 10
c = 5.5 #float
d = True #boolean
e = "London" #string
f = "united kingdom"
g = "'London' is capital of 'united kingdom'"
h = '''London is capital of
united kingdom'''

print (a) ; print (b) #writing multiple statements in the same line, terminate the former witha semicolon
print (a, b) #multiple values in the same line
print (a, b, sep =':') #sep - separator
print (d, end = " / ") #end - replacement of newlline character at the end
print (e)

print (g)
print (h)

print (type(a))
print (type(c))
print (type(d))
print (type(h))

a = 20
print (a) #scalar variable, holds single value at all times

i = [6,12,34,56] #list - mutable (changeable)
j = (9,23,45,21,9) #tuple - immutable
k = {5,10,45,34,5,91} #set - eliminate duplicates - it doesn't keep order
m = {"id":1, "name": "Andrew"} # dictionary - key and valuepair with unique keys

#compone variable, holds one or more values

print (type(i))
print (type(j))
print (type(k))
print (type(m))

print (i)
print (j)
print (k)
print (m)


