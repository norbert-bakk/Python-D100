number = int(input("What is your number?"))

# % maradékos osztás 
number_check = int(number % 2)

if number_check == 1:
    print("This is an odd number!")
else:
    print("This is an even number")