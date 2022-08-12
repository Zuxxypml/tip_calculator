print("Welcome to Tip Calculator")
total_bill = input("What's the total bill? $")
total_bill = float(total_bill)
tip_percentage = input("What's the tip percentage ? $")
number_of_people = int(input("How many people to split the bill ?"))
tip_percentage = round(int(tip_percentage))
tip = (tip_percentage / 100)
tip_amount = tip * total_bill
total_bill_plus_tip = total_bill + tip_amount
each_person_bill = round(total_bill_plus_tip / number_of_people, 2)
print(f"Each person pays {each_person_bill}")

