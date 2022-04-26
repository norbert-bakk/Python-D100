height = float(input("enter you height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
print(bmi)

if bmi < 18.5 :
    print(f"You are underweight! Your BMI index is {bmi}.")
elif bmi < 25 :
    print(f"You are normal weight! Your BMI index is {bmi}.")
elif bmi < 30 :
    print(f"You are overweight! Your BMI index is {bmi}.")
elif bmi < 35 :
    print(f"You are obese weight! Your BMI index is {bmi}.")
else :
    print(f"You are clinically obese! Your BMI index is {bmi}.")
