print("Rollercoaster Ride Price Kiosk")
height = int(input("What is your height in cm?"))
bill = 0

if(height<120):
    print("Too short to ride")
else:
    age = int(input("What is your age?"))
    if(age<12):
        bill+=5
       # print(bill)
    elif(age<18):
        bill+=7
       # print(bill)
    else:
        bill+=12
       # print(bill)
    photo = input("Do you want photo, 'Yes' or 'No'")
    if(photo=='Yes'):
        bill+=3
       # print(bill)
    print(f"The total bill is {bill}")
