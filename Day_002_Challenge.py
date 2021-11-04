# Project: Tip Calculator
import time

print("Welcome to the tip calculator")
time.sleep(0.5)
print("What was the total bill?")
total_bill = input("$")
print("What percentage tip would you like to give?")
percentage = input()
print("How many people would be splitting the bill?")
no_of_friends = input()

try:
    total_bill = float(total_bill)
    percentage = int(percentage)
    no_of_friends = int(no_of_friends)
except ValueError:
    print("There's an error in the values entered")

new_total = ((percentage / 100) * total_bill) + total_bill
amount_each = "{:.2f}".format(new_total / no_of_friends)

print(f"Each person should pay $ {amount_each}")
