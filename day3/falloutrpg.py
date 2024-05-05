print("Method 2: Using a Raw String")
print(r"""
  _______________________________________
 /                                       \
/   _   _   _                 _   _   _   \
|  | |_| |_| |   _   _   _   | |_| |_| |  |
|   \   _   /   | |_| |_| |   \   _   /   |
|    | | | |     \       /     | | | |    |
|    | |_| |______|     |______| |_| |    |
|    |              ___              |    |
|    |  _    _    (     )    _    _  |    |
|    | | |  |_|  (       )  |_|  | | |    |
|    | |_|       |       |       |_| |    |
|   /            |_______|            \   |
|  |___________________________________|  |
\                                         /
 \_______________________________________/
""")

print("Welcome to Fallout 510")
print("Please choose your stats")
print("There are a total of 4 stats to choose from, the total amount of points to allot is 20 ") 
statcheck = False
strength = 0
dexterity = 0
charisma = 0
luck = 0
while(not statcheck):
    limit = 20
    s = int(input("Strength:"))
    d = int(input("Dexterity:"))
    c = int(input("Charisma:"))
    l = int(input("Luck:"))

    if(s+d+c+l<=20):
        strength = s
        dexterity = d
        charisma = c 
        luck = l 
        statcheck = True
    else:
        print("Error, stats entered exceeded 20 ")


# 4 options choose this or that.. this is going to be complicated.. do again another day

print("Welcome to the wastelands of Fallout 510. \nYour mission revolves around scouring the ruins for a rare Germanium Transistor. This archaic piece is vital for repairing your vintage radio—a cherished relic predating the Great War. Amidst the dust of a world forgotten, your dying spouse clings to a final wish: to hear the haunting tunes of 'In the Shadow of the Valley' by the Lost Weekend Western Swing Band echo through the radio one last time. Time is running out, and the echoes of the old world are fading. Will you brave the dangers that lurk in the wasteland to bring a moment of solace to your loved one?")







