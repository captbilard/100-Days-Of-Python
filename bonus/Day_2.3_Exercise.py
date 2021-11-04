# Your life in days, weeks, months if you live to 90 years

# Get the users age
age = input("What is your current age?\n")
# Check input is valid
if not age.isnumeric():
    print("Enter a valid number from 0-90")
elif int(age) > 90:
    print("Enter a valid number from 0-90")

age_difference = 90 - int(age)
days, weeks, months = 365 * age_difference, 52 * age_difference, 12 * age_difference

print(f"You have {days} days, {weeks} weeks and {months} months left.")
