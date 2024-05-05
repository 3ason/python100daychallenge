

while(1):
    year = int(input("Check year for leap year"))

    if(year == -1):
        break


    if(year % 4 == 0 ):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print(f"{year} is leap year")
            else:
                print(f"{year} is not a leap year")
        #i forgot if it is divisible by 4 but is not divisible by 100
        else:
            print(f"{year} is a leap yearx  ")

    else:
        print(f"{year} is not a leap year")


