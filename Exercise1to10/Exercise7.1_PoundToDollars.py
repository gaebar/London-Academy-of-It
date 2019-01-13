# amount_pounds= input("Please enter amount in pounds: £ ")
# conversion_rate = 1.28
# amount_dollars= conversion_rate * int(amount_pounds)
# amount_dollars_approx = round(amount_dollars * 100)/100
# print("£", amount_pounds, "are $",amount_dollars_approx)

amount_pounds = input("Please enter amount in pounds: £ ")
conversation_rate = 1.28
amount_dollars = conversation_rate * int(amount_pounds)
amount_dollars_approx = round(amount_dollars * 100)/100
print(("£ d% are $ d%") % (amount_pounds))