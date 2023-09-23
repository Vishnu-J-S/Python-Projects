print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

response = input("Upon following a path for a certain distance you scratch your head upon arriving at a  crossroads,you scratch your head,left or right? Type left or right ")
response = response.lower()
if response == "left":
  response_1 = input("""All you see is the vast expanse of the ocean,you sigh hoping you wouldn't regret your 
 decision,just like people regret joining college,you're unsure what to do,wait or swim? Type wait or swim """)
  response_1 = response_1.lower()
  if response_1 == "wait":
    print("""You wait thinking about why nobody wanted to look at you, not even a kidnapper who screamed after 
    he looked at your face, and ran away leaving you bound, and how you would gag everyday morning just by 
    looking at your own reflection in the mirror, then you see a boat arriving, 
    although they dont seem bothered by your ugliness, they just want to get you on board and move on. When 
    you arrive at the island and get down one of the person hands you a mask and says 'For virus, not 
    ugliness' and speed away laughing.""")
    response_2 = input("""You then see three huts next to each with a red door, a yellow door,and a blue door 
    respectively,you didn't have any lucky or favourite colours but you could only go through one door at a 
    time, you stand there thinking, red, blue, or yellow? Type Red, Blue, Yellow """)
    
    response_2 = response_2.lower()
    if response_2 == "red":
      print("""You enter the hut to find it absolutely empty and then out of nowhere a circle of fire erupts 
      around you at the center, a skull likes shape made out of fire emerges from the fire in front of you, 
      and starts singing every cringe song you've known in your life and the fire slowly closes 
      around you.You dont know which burns you more the cringe songs or the fire, but both of them kill you. 
      Game over.""")
    elif response_2 == "blue": 
      print("""You almost think you found the treasure as soon as you open the door, only to realize that they 
      were piles of bones,just as you're about to close the door the door swings open and a strong force of 
      suction pulls you in. The hut itself transforms into a jaw of sorts, the house itself is a flippin' 
      beast!!! you struggle for balance and fall, a hole what might be a windpipe forms and from it oozes 
      acid,you try to get up but the whole jaw tilts and it crushes you with its teeth.Game Over""")
    elif response_2 == "yellow":
      print("""You open the door and glimpse a faint yellow glow to the hut inside you see nothing but a giant 
      chest made out of gold you cautiously enter peering for any traps, and slowly open the treasure a 
      glowing yellow ball comes out and says 'HA!Ya made it, despite the clone pop-stars and singin' trouts 
      and the cringe fire and the monstrous house, by god ya made it!' You scowl and shrug having no idea what 
      it's talking about or that what it is,'You dont know what I'm talking about, eh? Well, take the treasure 
      and be on your way!', you peer in to see an autographed record of Elvis Presley on a bunch of gold.You 
      leave(albeit walking a bit slowly carrying a decent sized gold chest) thankful knowing that you have a 
      present for grandma coming christmas.""")
    else:
      print("""oh you thought you could outsmart me did you? Typing something else? Well,you did not! Game 
      Over! Now go and rethink our life choices!""")
  else:
    print ("""At first you seem to enjoy it, then out of nowhere a trout pops up out of the sea and starts 
    loudly screaming 'Baby! Baby! Baby! OOOOHHHHH!' in such a shrill voice that your head explodes leaving 
    behind an ugly mess...Game Over.""")

else:
  print("You're hounded by a bunch of male teenage pop - star clones and their scent is enough to kill you, you try running away but end up falling in a hole.You regretted making this decision, just like you regretted joining college.Game Over.")



