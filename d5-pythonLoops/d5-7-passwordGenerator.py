import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) #52
nr_symbols = int(input(f"How many symbols would you like?\n")) #10
nr_numbers = int(input(f"How many numbers would you like?\n")) #9
#print(len(letters))
#print(len(numbers))
#print(len(symbols))
random_index = 0

random_letters = str()
random_symbols = str()
random_numbers = str()

full_password_easy = str()


#--------------------EASY LEVEL------------------------------------------------------------------


#legenerálja a random betűket -> amennyit kívánt a felhasználó
for i in range(0, nr_letters):
    random_index = random.randint(0, 51)
    random_letters += letters[random_index]

#legenerálja a random speciális karaktereket -> amennyit kívánt a felhasználó
for i in range(0, nr_symbols):
    random_index = random.randint(0, 8)
    random_symbols += symbols[random_index]

#legenerálja a random számokat karaktereket -> amennyit kívánt a felhasználó
for i in range(0, nr_numbers):
    random_index = random.randint(0, 9)
    random_letters += numbers[random_index]

#összeadja szekvenciálisan a random legenerált karaktereket, azokat kinyomtatja
full_password_easy = random_letters + random_symbols + random_numbers
print(full_password_easy)
#validálás miatt tettem be, összehasonlításképpen a nehéz jelszóval
print(len(full_password_easy))


#--------------------HARD LEVEL------------------------------------------------------------------


#felesleges változó létrehozása --> csak a név miatt csináltam
full_password_hard = str(full_password_easy)
#meghatározom a legenerált karakterek számát
f_pass_hard_char_count = len(full_password_hard)
#karaktereknek létrehozom a listáját --> egyelőre üres
f_pass_hard_chars = []

#feltöltöm a listát, külön-külön karakterekként 
for i in range(0, f_pass_hard_char_count):
    f_pass_hard_chars.append(full_password_hard[i])
print(f_pass_hard_chars)

#létrehozom a végleges, kevert nehéz jelszó változót
mixed_hard_password = str()
#print(len(f_pass_hard_chars))

#legenerálok egy random index-számot, majd ez alapján kiveszem a karakteres listából,
#majd ezt a random karaktert hozzáadom a végeles nehéz jelszó változójához,
#aztán pedig kitörlöm a megjelölt karaktert a listából,
#majd egyel kevesebbé teszem a karakterek számának változóját tartalmazó össezgnek
for i in range(0, f_pass_hard_char_count):
    random_index = random.randint(0, f_pass_hard_char_count -1)
    mixed_hard_password += f_pass_hard_chars[random_index]
    f_pass_hard_chars.pop(random_index)
    f_pass_hard_char_count -=1

print(mixed_hard_password)
#validálás miatt tettem be, összehasonlításképpen a könnyű jelszóval
print(len(mixed_hard_password))
