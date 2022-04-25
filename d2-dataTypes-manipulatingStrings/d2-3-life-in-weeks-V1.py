#rounding a number --> round() --> coma, number of decimal places
print(round(8/3, 2))
# // is jó "flaw division" -> float nem lehet ---> / clean division
# different datatypes dont work well with each other

score = 0
height = (float(1.75))
#f-String #curly braces
print(f"your score is {score}, your height is {height}.") #converted into strings

#d2 gyakorlat
age = input("What is your age?")
months_in_one_year = int(12)
weeks_in_one_year = int(52)
days_in_one_year = int(365)

months_lived = int(age) * int(months_in_one_year)
weeks_lived = int(age) * int(weeks_in_one_year)
days_lived = int(age) * int(days_in_one_year)

perfect_age = int(90)
perfect_months = int(perfect_age * months_in_one_year)
perfect_weeks = int(perfect_age * weeks_in_one_year)
perfect_days = int(perfect_age * days_in_one_year)

print(f"You have {perfect_days - days_lived} days, {perfect_weeks - weeks_lived} weeks, and {perfect_months - months_lived} months left.")
