#repitition are for repetead execution of statments
#while and for keywords for iteration structs
#
# x = 1 #value assignment #initianaliation statement
# while x <= 10: #conditional / test statement # x loop variable
#     print(x)
#     x += 1 # x = x+1 #modifier statement # modifies value of loop variable

# password = '' #initialization statement, #password is loop variable
# count = 0
# while password != 'abcd1234': # condition statement
#     password = input("Enter the password")
#     count +=1
# print ("Password correct in %d attempts" %(count))


password = ''  # initialization statement, #password is loop variable
count = 0
while password != 'abcd1234' and count <= 4:  # conditional statement
     password = input("Enter the password ")
     count += 1

if password == "abcd1234":
    print("Password correct in %d attempts" %(count))
else:
    print("Suspicious attempts failed")