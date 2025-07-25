def calculate_age(current_age, current_year, future_year):
    future_age = current_age + (future_year - current_year)
    print("You will be", future_age, "years old in", future_year)

# Take input from user
name = input("Enter your name: ")
age = int(input("Enter your current age: "))
year = int(input("Enter the current year: "))
target = int(input("Enter the future year: "))

print("Hello", name + "!")
calculate_age(age, year, target)
