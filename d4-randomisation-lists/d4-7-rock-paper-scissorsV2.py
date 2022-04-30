import random
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
game_images = [rock, paper, scissors]
user_choice = int(input("Welcome to the Rock-Paper-Scissors game! choose [0]Rock, [1]Paper or [2]Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed and invalid number. You lose!")
else:    
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose: \n" + game_images[computer_choice])
    
    if user_choice == 0 and computer_choice == 2 :
        print("You won!")    
    elif computer_choice == 0 and user_choice == 2:
        print("You lost.")
    elif computer_choice > user_choice :
        print("You lost.")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw.")