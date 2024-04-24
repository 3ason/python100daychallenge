height = input("Height in Meters e.g. 165")
weight = input("Weight in Kilograms e.g. 72")
weight = int(weight)
height = float(height)

bmi = weight / height**2 
print(bmi)

bmi = weight / (height * height)
print(bmi)


print(int(bmi))
