while(1):
    name1 = input("Name One:") 
    name2 = input("Name Two:")

    both = name1 + name2
    both = both.lower()
    t = both.count("t")
    r = both.count("r")
    u = both.count("u")
    e = both.count("e")

    first = t + r + u + e

    l = both.count("l")
    o = both.count("o")
    v = both.count("v")

    second = l + o + v + e 

    score = int(str(first) + str(second))

    if(score < 10) or (score > 90):
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif(score >= 40) and (score <= 50):
        print(f"Your score is {score}, you are alright together.")
    else: 
        print(f"Your score is {score}.") 