print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm?"))
bill = 0
#indentation
#nesting
if height >= 120:
    age = int(input("What's your age?"))
    if age < 12:
        bill = 5
        print("Child ticket price is 5$")
    elif age <= 18:
        bill = 7
        print("Youth ticket price is 7$")
    else:
        bill = 12
        print("Adult ticket price is 12$")
    wants_a_photo = input("Do you what a photo printed? +3$ extra fee. [Y]es or [N]o")
    if wants_a_photo == "Y":
        bill += 3
        print(f"Photos selected! Your final bill is {bill}$ Have a nice ride!")
    else:
        print(f"No photos selected! Your final bill is {bill}$ Have a nice ride!")
else:
    print("You can't take a ride!")