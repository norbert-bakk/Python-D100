# a python a mersenne twister random technikát használja
import random
import my_module

#randint(a, b) a és b között random szám
random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)

#basic .random() is betweeen 0.000000 - 0.999999...
random_float = random.random()
print(random_float)

#to extend it's range from 0.000 to x it needs to be multiplies by x e.g.
random_float = random_float * 5 #--> anything between 0.0000 and 4.99999

love_score = random.randint(1, 100)
print(f"Your livescore is {love_score}")