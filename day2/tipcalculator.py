print("Welcome to the tip calculator")
bill = float(input("Bill Total?"))
tip = float(input("Tip Percentage"))
tip = tip/100
total = bill * (1+tip)
split = int(input("How many people splitting"))

print(round(total/split,2))