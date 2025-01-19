# I have created a simple tip calculator to use when you're out to dinner!
import math

print("Welcome to the Tip Calculator, let's get started.")
bill = float(input("How much is your bill? $"))
tip = int(input("Please select a tip percentage: 15 18 20. "))
people = int(input("How many people are splitting the bill? "))

tip_amount = (tip / 100) + 1
bill_with_tip = (bill * tip_amount)
bill_per_person = round((bill_with_tip / people),2)
print(bill_per_person)