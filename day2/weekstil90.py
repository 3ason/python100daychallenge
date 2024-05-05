# we know there is 365.25 days in a week 
# meaning there must be 365/7 weeks in a year which is 52.1428571 weeks
# https://waitbutwhy.com/2014/05/life-weeks.html

daysinayear = 365.25 #float 
weeksinayear = daysinayear/7 


while 1:
    age = input("What is your age?")
    difference = 90 - int(age) 
    print(int(weeksinayear * difference))
    print(difference * 52)





