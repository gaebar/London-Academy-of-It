counter = 1  # Alberto way

for line in range(3):
    for column in range(3):
        print(counter, end=' ')
        counter +=1
    print(" ")


for x in range(1, 10):  # teacher way
    print(x, end = '\t')
    if x % 3 == 0:
        print()