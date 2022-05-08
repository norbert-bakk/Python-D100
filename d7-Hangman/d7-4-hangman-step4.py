#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = len(stages)
letters_found = 0

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(stages[6])
while not end_of_game:
    
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if lives == 1:
        end_of_game = True
        print(f"You lost! You have {lives -1} left. The word was {chosen_word}.")

    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            letters_found += 1
    
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    if letters_found == 0:
        lives -= 1
        print(f"You've got {lives -1} left.")
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number 
    #of 'lives' the user has remaining.    
        print(stages[lives -1])

    letters_found = 0

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")