from functools import total_ordering
from imp import is_frozen


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
count1 = int(0)
count2 = int(0)

# .lower() mindent stringet kisbetűzze
# .count() számot ad vissza
if lower_case_name1.count("t") or lower_case_name2.count("t") > 0 :
    count1 += lower_case_name1.count("t")
    count1 += lower_case_name2.count("t")
if lower_case_name1.count("r") or lower_case_name2.count("r") > 0 :
    count1 += lower_case_name1.count("r")
    count1 += lower_case_name2.count("r")
if lower_case_name1.count("u") or lower_case_name2.count("u") > 0 :
    count1 += lower_case_name1.count("u")
    count1 += lower_case_name2.count("u")
if lower_case_name1.count("e") or lower_case_name2.count("e") > 0 :
    count1 += lower_case_name1.count("e")
    count1 += lower_case_name2.count("e")

if lower_case_name1.count("l") or lower_case_name2.count("l") > 0 :
    count2 += lower_case_name1.count("l")
    count2 += lower_case_name2.count("l")
if lower_case_name1.count("o") or lower_case_name2.count("o") > 0 :
    count2 += lower_case_name1.count("o")
    count2 += lower_case_name2.count("o")
if lower_case_name1.count("v") or lower_case_name2.count("v") > 0 :
    count2 += lower_case_name1.count("v")
    count2 += lower_case_name2.count("v")
if lower_case_name1.count("e") or lower_case_name2.count("e") > 0 :
    count2 += lower_case_name1.count("e")
    count2 += lower_case_name2.count("e")

# print(count1)
# print(count2)
total_count = str(count1) + str(count2)
total_count_as_int = int(total_count)

if total_count_as_int < 10 or total_count_as_int > 90 :
    print(f"Your score is {total_count_as_int}, you go together like coke and mentos.")
if total_count_as_int >= 40 and total_count_as_int <= 50 :
    print(f"Your score is {total_count_as_int}, you are alright together.")
else:
    print(f"Your score is {total_count_as_int}.")