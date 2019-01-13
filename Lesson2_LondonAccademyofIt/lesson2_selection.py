# a = 5
# b = 10
#
# if a > b: # column sta per continuation
#     print("a is bigger") # for indentation you can use tabspace or 4 whitespaces
# else:
# #     print("b is bigger")
# #
# # print("a is bigger") if a>b else print("b is bigger") #another way to use it
#
# a = 5
# b = 10
# c = 15
#
# # if a > b and a > c:
# #     print("a is biggest")
# # elif b > a and b > c: # n numbers of elif / elif must be followed by a condition
# #     print("b is biggest")
# # else: # no condition can be specified in else
# #     print("c is biggest")
#
# if a > b > c:
#     print("a is biggest")
# elif b > a and b > c: # n numbers of elif / elif must be followed by a condition
#     print("b is biggest")
# else: # no condition can be specified in else
#     print("c is biggest")
#
# print("a is biggest") if a >b>c else print ("b is biggest") if b>a>c else("c is biggest")

price = 5000
age = 5

if price <= 5000:
    if age <= 5: #nested if
        print("Let's go for test drive")
    else:
        print("This car is old")
else:
    print("It is expensive")