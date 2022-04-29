import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#split --> splits a string into separate components with some sorts of divider --> 
# in this case its a coma (, ) (space is also important)
print(names)
names_number = len(names)
chosen_name_index = random.randint(0, names_number - 1) #-1 mert habár a számolás 1-től kezdődik, 
#az indexelés nullától 3 item --> 1, 2, 3 --> indexelés 0, 1, 2
print(f"{names[chosen_name_index]} is going to pay for the bills today.")