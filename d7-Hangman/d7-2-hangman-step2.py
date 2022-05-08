#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" 
#representing each letter to guess.

display = []
for letter in chosen_word:
    display.append("_")
print(display)

#TODO-1.1: - Use a while loop to let the user guess again. The loop should only stop 
#once the user has guessed all the letters in the chosen_word and 'display' 
#has no more blanks ("_"). Then you can tell the user they've won.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display 
#at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be 
# ["_", "p", "p", "_", "_"].

guess = input("Guess a letter: ").lower()

indexing = 0
for letter in chosen_word:
    indexing += 1
    if guess == letter:
        display[indexing -1] = letter
indexing = 0

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and 
# every other letter replace with "_".
print(display)