# Let's talk a little about the naming schema really quick 
* I title this document as documentation_day2.md 
* vs day2_documentation.md as I will be in the habit of naming folders into documents. I think I like the first choice better because I already know what folder I'm in so it's the formula is 
    * generic file -> file descriptor 
    * as it will make it easier to read too and also every file in there is likely to have the same file descriptor 


* :tabnew filename 


# 18. Day 2 Goals: What we will make by the end of the day 

* Goals: Data Types, Numbers, Operations, Type Conversion, f-Strings 

* Lesson Goal: be able to make a tip calculator by the end of this lesson. 
    * The tip calculator will prompt you for the price, and then the percentage of the tip, and if there are multiple people splitting the bill. 


# 19. Python Primitive Data Types

* if we tried typing in this code 
    * print(len(123131)) 
    * this will bounce an error back towards me 

* Python has primitive data types such as 

* Integer 
    * real numbers :) 

* String 
    * print("Hello"[1])

    * print("123" + "456") vs print(123 + 456) 


* Float 
    * 3141.59 

* Boolean 
    * True/False 

# 19b. Data Types Quiz 
* something new 
* you can write an int or a float like this I guess lol 
    * mystery = 734_529.678 
    * num = 123_456 

# 20. Type Error, Type Checking and Type Conversion 
* cannot concatnate a string with an int
* thus we must do casting
    * i wonder how non built in casting is programming 
    * looked it up have to put it in the constructor of the object 

num_char = len(input("What is your name?"))
num_char = str(num_char)
print("Your name has " + num_char + " characters.")

# 21. [Interactive Coding Exercise] Data Types 
* 
```
twoDigit = input()

one = int(twoDigit[0])
print(one)
two = int(twoDigit[1])

print(one + two)

```

# 22. Mathematical Operations in Python 

- PEMDASLR 
- () 
- ** 
- * / 
- + - 

* what happens in 
    * print(3 * (3+3)/ 3-3)


# 23 . BMI Calculator 

- Formula
    - BMI = weight(kg)/ height^2(m^2)

- example input: 
    1.75
    80

means weight = 80, and height = 1.75 

- example output 1
    26
since 80 / (1.75x1.75) = 26.122448979

- steps 
variables = input()
- casting weight to int 
weight_var = int(weight)
- cast height to float(decimal point number)
height_var = float(height)
- using the exponent operator
bmi = weight/height**2 
- ** is exponent in python 
- or we can do 
bmi = weight/(height*height)

bmi = int(bmi)
print(bmi)


# 24. Number Manipulation and F Strings in Python

print(8/3) 
out: 2.66666666
what if print(int(8/3))
out: 2
instead of rounding, so to fix this we need to use round function
print(round(8/3,2))
print(round(2.666666666,2))
out: 2.67
- or 
print(8 // 3)
out: 2 
- // is floor division 
print(type(8//3))
out: <class 'int'> 
- whereas
print(type(8/3))
out: <class 'float'>
- print(type(4/2))
has an oout: <class 'float'>    

- can do the shorthand trick where 
result = 4/2
result /= 2 
result is now = to 1 

score = score - 1 
is equivalent to 
score -= 1
or score += 1 

- if we do this here this is a TypeError : can only concatenate str (not "int") to str
score = 0 
print("score:" + score)

- have to do this
print("score:" + str(score))

- to avoid this problem can use f strings 
w_uses = 2 
champion = "shaco" 
kda_avg = 2.2

print(f"{champion} can use box {w_uses} and has {kda_avg} kda")




# [Interactive Coding Exercise] Life in Weeks 

Article by Tim Urban - Your Life in Weeks 
    - realised how little time we have 

requirement: create a program using maths and f-strings that tells us how many weeks we have left, if we live to 90 years old 
input: take current age and output message with this format 
"You have x weeks left" 
x is the calculated amount of weeks you would have left until age 90 

# 26. Day 2 Project: Tip Calculator 
print("Welcome to the tip calculator")
bill = float(input("Bill Total?"))
tip = float(input("Tip Percentage"))
total = bill * (1+tip)
split = input("How many people splitting")

print(total/split)


