rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
player = int( input ("Type 0 for rock 1 for paper and 2 for scissors.") )
if player == 0:
  print(f"You chose:\n {rock}")
elif player == 1:
  print(f"You chose:\n {paper}")
elif player == 2:
  print(f"You chose:\n {scissors}") 
  
computer = random.randint(0, 2)
if computer == 0:
  print(f"Computer chose:\n {rock}")
elif computer == 1:
  print(f"Computer chose:\n {paper}")
elif computer == 2:
  print(f"Computer chose:\n {scissors}")  

if player ==0 and computer == 0:
  print("It's a draw!")
elif player == 0 and computer == 1:
  print("Computer wins!")
elif player == 0 and computer == 2:
  print("You win!")
elif player == 1 and computer == 0:
  print( "You win!")
elif player == 1 and computer == 1:
  print("It's a draw!")
elif player == 1 and computer == 2:
  print("Computer wins!")
elif player == 2 and computer == 0:
  print("Computer wins!")
elif player == 2 and computer == 1:
  print( "You win!")
elif player == 2 and computer == 2:
  print("It's a draw!")
else:
  print("Invalid number, you lose")