import random
import sys
import os

chambers = input("Please enter the number of chambers (default = 6): ")

if not chambers:
	chambers = 5

elif not chambers.isdigit():
	quit("Invalid number of chambers!")

fatal_bullet = random.randint(1, int(chambers))

for x in range(1, int(chambers) + 1):
    input("Press enter to pull the trigger! ")
    if x == fatal_bullet:
        print("You just got served!")
        print("Game Over")
        start_again = input("Do you want to start again? (y/n): ")
        if start_again and start_again.lower()[0] == "y":
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            break
    print("You will live to see another day")
