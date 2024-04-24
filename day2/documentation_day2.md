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

    
