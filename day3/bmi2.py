height = float(input("Height Please"))

weight = int(input("Weight Please"))

bmi = weight / height ** 2 

print(round(bmi,2))
if bmi < 18.5: 
    print("Underweight")
elif bmi < 25: 
    print("Normal Weight")
elif bmi < 30:
    print("Slightly Overweight")
elif bmi < 35:
    print("Obese")
else: 
    print("Clinically Obese")
    