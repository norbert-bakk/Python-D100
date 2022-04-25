print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm?"))
age = int(input("What's your age"))

#indentation
#nesting
if height >= 120:
    if age < 12:
        print("Ticket price is 5$")
    elif age <= 18:
        print("Ticket price is 7$")
    else:
        print("Ticket price is 12$")
else:
    print("You can't take a ride!")