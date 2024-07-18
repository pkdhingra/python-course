price = int(input("Enter the price of a meal: "))

tax = price * 0.08
total_price = price + tax
tip = total_price * 0.18
grand_total = total_price + tip

print("A 16\% tip would be", tip)
print("The total including tip would be", total)
