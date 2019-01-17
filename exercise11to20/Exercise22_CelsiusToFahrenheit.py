first_number = int(input("Enter the first amount in Celsius: "))
last_number = int(input("Enter the last amount in Celsius: "))


def celsiustof(degree):
    return degree * 9 / 5 + 32

for degree in range(first_number, last_number):
    print(degree, celsiustof(degree))