def truefloat(prompt):
    #this is to stop user error when entering something other than a number into IPT Calc v4
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a number.")
            continue

        if value == str():
            continue

        else:
            break
    return value

