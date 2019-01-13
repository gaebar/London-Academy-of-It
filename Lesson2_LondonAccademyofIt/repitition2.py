
m = [5, 10, 15, 20, 10]
for n in m:
    print(n)


exit()

for x in range(1, 11):  # loop execution starts drom outer loop but the inner
    # loop has to terminate fro the termination of the other loop

    for y in range(1, 11):  # nested for # 1
        print(x * y, end='\t')
    print()
2
exit()

for x in range(1, 21):
    if x % 2 != 0:
        #break  # force termination
        continue  # skips the remaining statements
    print(x, end='\t')  # replace the newline with a tabspace #escape character

exit()


for x in range(1, 21):
    if x == 15:
        #break  # force termination
        continue  # skips the remaining statements
    print(x, end='\t')  # replace the newline with a tabspace #escape character


exit()



for x in range(10, -1, -1): # starts from 0, the last value provided is excluded(10), the third it works as a steps
    print("Hello - %d" % (x))

exit()

for x in range(1, 10, 2): # starts from 0, the last value provided is excluded(10), the third it works as a steps
    print("Hello - %d" % (x))

exit()

for x in range(1, 10): # starts from 0, the value probidede is excluded(10)
    print("Hello - %d" % (x))

exit() #non viene esecuito il resto con exit

for x in range(10): # starts from 0, the value probidede is excluded(10)
    print("Hello - %d" % (x))