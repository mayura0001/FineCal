multiply = 12
amount= 20000
intrest_rate = 3
income_tax_presentage = 4

print()
for i in range(1, multiply + 1):
    income = amount * intrest_rate / 1200
    income = income - ( income *4 / 100 ) 
    new_amount = amount + income
    print(str(i) + " month:", "Rs." + str(int(new_amount)))
    amount = new_amount
print()