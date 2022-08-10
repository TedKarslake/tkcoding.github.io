from def_round import custround

allowed_char1 = ['y', 'n'] #these are the allowed characters to begin

x = 1
y = 1

print("")
while True:
    question = input("Would you like to calculate your Insurance Premium? (press 'y' then [Enter key] to continue, input 'n' then [Enter key] to exit): ")
    if any(x not in allowed_char1 for x in question): #to prevent errors, this is to prompt user to key 'y' or 'n'
        print("")
        print("Error! Invalid character. Please input 'y' then [Enter] to continue, or 'n' then [Enter] to exit.")
        print("")
        continue
    else:
        break

while question == "y":
    print("")
    pcnt = input("Insurance Premium Tax Percent (number only): ")
    print("")
    while x == 1:
        try:
            pcntnum = float(pcnt)
            x = 0
        except ValueError:
            pcnt = input("Error! Invalid character. Please enter an Insurance Premium Tax Percent number to continue: ")
            print("")

    print("IPT: " + pcnt + "%")
    print("")
    
    broker = input("Brokerage Percent (number only): ")
    print("")
    while y == 1:
        try:
            brokernum = float(broker)
            y = 0
        except ValueError:
            broker = input("Error! Invalid character. Please enter a Brokerage Percent number to continue: ")
            print("")
    
    allowed_char2 = ['p', 'g', 'n'] #as before
    
    print("Brokerage: " + broker + "%")
    print("")

    while True:
        question2 = input("Press 'p' then [Enter key] for Net Premium input, 'g' then [Enter key] for Gross Premium input. Enter 'n' then [Enter key] at any time to stop: ")
        if any(x not in allowed_char2 for x in question2): #to prevent errors, this is to prompt user to key 'p', 'g' or 'n'
            print("")
            print("Error! Invalid character. Please input 'p' then [Enter] for Net Premium, or 'g' then [Enter] for Gross Premium. 'n' then [Enter] will exit.")
            print("")
            continue
        else:
            break

    if  question2 == "p":
        pcnt_dec = float(pcnt / 100)
        broker_dec = float(broker / 100)
        print("")
        net = input("Net Premium: £")
        try:
            netnum = float(net)
        except ValueError:
            print("")
            print("Error! Invalid character. Please enter a number to continue.")
            print("")
        print("")
        sum = float(pcnt_dec * net)
        broker_sum = float(broker_dec * net)
        print("")
        print("Insurance Premium Tax Amount: £" + str(custround(sum)))
        print("")
        gross = net + sum
        print(gross)
        print("Gross Premium: £" + str(custround(gross)))
        print("")
        print(broker_sum)
        print("Brokerage due: £" + str(custround(broker_sum)))
        print("")
        print("Press 'n' at any time to stop")

    elif question == "g":
        broker_dec = float(broker / 100)
        print("")
        gross = input("Gross Premium: £")
        try:
            grossnum = float(gross)
        except ValueError:
            print("")
            print("Error! Invalid character. Please enter a number to continue.")
            print("")
        pcnt_dec2 = float(pcnt / 100)
        x = float(1 + pcnt_dec2)
        sum2 = float(gross / x)
        sum3 = float(sum2 - gross)
        sum4 = float(sum3 * -1)
        sum5 = float(gross - custround(sum4))
        broker_sum = float(broker_dec * sum5)
        print("")
        print("Insurance Premium Tax Amount: £" + str(custround(sum4)))
        print("")
        print("Net Premium: £" + str(custround(sum5)))
        print("")
        print("Brokerage due: £" + str(custround(broker_sum)))
        print("")
        print("Press 'n' at any time to stop")

    elif question == "n":
        break
    
    
else:
    print("")
    print("Enter 'n' the [Enter key] at any time to stop.")