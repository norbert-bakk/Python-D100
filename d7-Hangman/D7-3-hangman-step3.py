import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. 
#The loop should only stop once the user has guessed all the letters in the chosen_word 
#and 'display' has no more blanks ("_"). Then you can tell the user they've won.
game_over = False
print(display)

while not game_over:
    underline_count = display.count("_")
    if underline_count > 0: 
        guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
    
    if underline_count == 0:
        game_over = True
    

print(display)