num_char = len(input("What's your name?"))
#print("Your name has " + num_char + "characters.") -> intet nem lehet string concatenation-elni
#type -> típus ellenőrző
print(type(num_char))
new_num_char = str(num_char)
print(type(new_num_char))
print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))


#d2-gyakorlat
two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))
number_one = two_digit_number[0]
number_two = two_digit_number[1]
print(type(number_one))
print(type(number_two))
result = int(number_one) + int(number_two)
print(result)