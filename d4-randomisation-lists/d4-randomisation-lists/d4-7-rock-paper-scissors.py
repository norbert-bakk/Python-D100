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
print("Welcome to the Rock-Paper-Scissors game! choose [1]Rock, [2]Paper or [3]Scissors.\n")
player_choice = int(input())
computer_choice = random.randint(1, 3)

if computer_choice == 1 :
    computer_choice = "rock"
elif computer_choice == 2:
    computer_choice = "paper"
elif computer_choice == 3:
    computer_choice = "scissors"

if player_choice == 1 :
    player_choice = "rock"
elif player_choice == 2 :
    player_choice = "paper"
elif player_choice == 3 :
    player_choice = "scissors"

if player_choice == "rock" and computer_choice == "rock" : # Player : ROCK 
    print(f"You chose {rock}")
    print(f"The computer chose {rock}")
    print("It's a draw")
elif player_choice == "rock" and computer_choice == "paper" :
    print(f"You chose {rock}")
    print(f"The computer chose {paper}")
    print("The computer wins")
elif player_choice == "rock" and computer_choice == "scissors" :
    print(f"You chose {rock}")
    print(f"The computer chose {scissors}")
    print("You win!")
elif player_choice == "paper" and computer_choice == "paper" : # Player: PAPER
    print(f"You chose {paper}")
    print(f"The computer chose {paper}")
    print("It's a draw")
elif player_choice == "paper" and computer_choice == "scissors" :
    print(f"You chose {paper}")
    print(f"The computer chose {scissors}")
    print("The computer wins")
elif player_choice == "paper" and computer_choice == "rock" :
    print(f"You chose {paper}")
    print(f"The computer chose {rock}")
    print("You win!")
elif player_choice == "scissors" and computer_choice == "scissors" : # Player: SCISSORS
    print(f"You chose {scissors}")
    print(f"The computer chose {scissors}")
    print("It's a draw")
elif player_choice == "scissors" and computer_choice == "rock" :
    print(f"You chose {scissors}")
    print(f"The computer chose {rock}")
    print("The computer wins")
elif player_choice == "scissors" and computer_choice == "paper" :
    print(f"You chose {scissors}")
    print(f"The computer chose {paper}")
    print("You win!")