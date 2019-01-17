for line in range(6):  # Alberto way
    for column in range(line):
        print('* ', end='')
    print("")

for line in range(1, 6):  # teacher way
    print("*" * line)