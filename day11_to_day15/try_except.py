#Try and excpet example:


try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input! Please enter a numeric value for age.")
    age = int(input("Enter your age: "))

if age >= 18:
    print(f"You can drive at age {age}")

