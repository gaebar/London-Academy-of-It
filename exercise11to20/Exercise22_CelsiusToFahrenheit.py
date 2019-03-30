#Alberto's way:

#first_number = int(input("Enter the first amount in Celsius: "))
#last_number = int(input("Enter the last amount in Celsius: "))


#def celsiustof(degree):
#    return degree * 9 / 5 + 32

#for degree in range(first_number, last_number):
#    print(degree,'\t', celsiustof(degree))

#professor's way:
x = int(input("first value "))
y = int(input("second value "))
print('celsius \t\tFarenheit')
for n in range(x, y+1):
    print(x, '\t\t', n * 9/5 + 32)