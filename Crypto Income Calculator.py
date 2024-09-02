start_price = 61400
ending_price = 81000
your_investment = 10

rate = (ending_price - start_price) / start_price * 100
income = your_investment * rate / 100
total = your_investment + income

print()
print("Rate: " + str(rate) + "%")
print("Income for " + str(your_investment) + "$ : " + str(income) + "$" )
print("Total: " + str(total))
print()