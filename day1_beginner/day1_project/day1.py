import random  # random for looking for different words each time  

file = open('band-names.txt')  # these are all adjectives  
file2 = open('backdoor.txt')   # these are generated nouns for 
file3 = file 

bandnames = file.readlines() #The readlines() method returns a list containing each line in the file as a list item. 
backdoors = file2.readlines()

print(file3.readlines(9))

while(1):

    gen1 = random.randint(0,47) # 1,48 so index 0 to 47  
    gen2 = random.randint(0,49) # 1,50 so index 0 to 49  
    #bug where i forgot to rand int generate 0 as a possible index

    chosen1 = bandnames[gen1] # random word is plucked from the individual lists using the generated number as an index. 
    chosen2 = backdoors[gen2]

    chosen1 = chosen1.strip() # removes the random space, not sure if replace would work, im going to try really quick 
    #chosen1 = chosen1.replace("\n", "") # okay these two lines do effectively the same thing, strip() takes away leading and trailing spaces but doesn't remove any spaces in between.
    chosen2 = chosen2.replace("\n","")

    # i guess an example of the difference of application is if there is \n in between as strip only gets rid of trailing and leading space. but it wouldn't get rid of the space in between 
    # both is necessary only in the case there is new line and trailing and leading sapces


    print("Program Initialization for Band Name Generator")                     # prompt 1 and 2 
    print("Please enter backdoor for a completely random name")
    check = input("What's your favorite animal?")                               # input request in the format of variable = input("Question input")

    if(check == "backdoor"):                                                    # input to check if a random name will be selected
        print(f"******{chosen1} {chosen2}******")                               # to print with variables have to do print(f"{variable_name}")
    else:
        print(f"******{chosen1} {check}******") 





# This is a practice for Printing, Commenting, Debugging , String Manipulation 
# Variable Manipulation

