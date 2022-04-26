print("Welcome to Pepperoni's Finest!")
pizza_size = input("What sized pizza do you want? S (15$), M (20$) or L (25$)")
add_pepperoni = input("Do you want extra pepperoni? S/M +2$ and L+3$ [Y]es or [N]o")
extra_cheese = input("Do you want extra cheese? That'd be +1$ [Y]es or [N]o")
bill = 0

if pizza_size == "S" :
    bill = int(15)
    if add_pepperoni == "Y" :
        bill += 2
    if extra_cheese == "Y" :
        bill += 1
elif pizza_size == "M" :
    bill = int(20)
    if add_pepperoni == "Y" :
            bill += 2
    if extra_cheese == "Y" :
            bill += 1
elif pizza_size == "L" :
    bill = int(25)
    if add_pepperoni == "Y" :
            bill += 3
    if extra_cheese == "Y" :
            bill += 1

print(f"Your total bill for pizza is {bill}")