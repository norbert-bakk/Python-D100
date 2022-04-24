#if the bill was 150, split between 5 ppl with 12% tip
#each person should pay (150/5) * 1.12
# round to result of 2 decimal places

total_bill = float(input("What was the total bill?"))
tip_percentage = float(input("What percentage tip would you like to give?"))
ppl_present = int(input("How many people to split the bill?"))
# tip_percentage_digit1 = tip_percentage[0]
# tip_percentage_digit2 = tip_percentage[1]
# tip_percentage_whole = float(1 + tip_percentage_digit1 + tip_percentage_digit2)
bill_with_tip = tip_percentage / 100 * total_bill + total_bill
final_amount = "{:.2f}".format(bill_with_tip / ppl_present) #to make it 2 decimals
print(f"Each person should pay: {final_amount}")

#reverse engineering!!!