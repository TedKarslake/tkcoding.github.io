def input_loop():
    while True:
        try:
            value = float(input("Enter your number: "))
            break
        except:
            print("Invalid entry")
            continue
    return value

value = input("enter your number: ")
print(value)