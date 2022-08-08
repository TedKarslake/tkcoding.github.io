print(" ")
print("Welcome.")
print(" ")
first_name = input("What is your first name? ")
print(" ")
print("Hello " + first_name + ".")
print(" ")
last_name = input("What is your last name? ")
full_name = (first_name + " " + last_name)
print(" ")
print("Excellent - thank you, " + full_name + ".")
print(" ")
print("Age verification is required to access the vault.")
birth_year = input("Enter your birth year to continue: ")
print(" ")
x = 1
while x == 1:
    try:
        age = 2020 - float(birth_year)
        x = 0
    except:
        birth_year = input("Please only enter the numerical digit YEAR. Enter your birth year to continue: ")
        print(" ")
if age >= 21:
    print("Age verified. Access granted.")
    print(" ")
    print(f"Hello {full_name}, welcome to the Guinness Factory Vault.")
elif age < 21:
    print("Access Denied.")
print(" ")