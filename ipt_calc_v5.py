from def_round import custround #custround will round the numbers to the second decimal place, for currency

allowed_char1 = ['y', 'n'] #this defines the acceptable inputs

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
    while x == 1: #this is to prevent errors, so people can only input an int/float
        try:
            pcntnum = float(pcnt)
            x = 0
        except ValueError:
            pcnt = input("Error! Invalid character. Please enter an Insurance Premium Tax Percent number to continue: ")
            print("")
    
    pcnt_float = float(pcnt) #we had a problem where the input function above (to stop rogue inputs) would return a str not a float (messing up the sums below). This is to translate
    print("Insurance Premium Tax: " + pcnt + "%")
    print("")

    broker = input("Brokerage Percent (number only): ")
    print("")
    while y == 1: #as was used for Insurance Premium Tax above
        try:
            brokernum = float(broker)
            y = 0
        except ValueError:
            broker = float(input("Error! Invalid character. Please enter a Brokerage Percent number to continue: "))
            print("")

    broker_float = float(broker) #as above
    print("Brokerage: " + broker + "%")
    print("")

    allowed_char2 = ['p', 'g', 'n'] #this defines the acceptable inputs

    while True:
        question2 = input("Press 'p' then [Enter key] for Net Premium input, 'g' then [Enter key] for Gross Premium input. Enter 'n' then [Enter key] at any time to stop: ")
        if any(x not in allowed_char2 for x in question2): #to prevent errors, this is to prompt user to key 'p', 'g' or 'n'
            print("")
            print("Error! Invalid character. Please input 'p' then [Enter] for Net Premium, or 'g' then [Enter] for Gross Premium. 'n' then [Enter] will exit.")
            print("")
            continue
        else:
            break

    if  question2 == "p": #'n' was already defined above to exit, so 'p' is for net 'p'remium
        pcnt_dec = float(pcnt_float / 100)
        broker_dec = float(broker_float / 100)
        print("")
        net = float(input("Net Premium: £"))
        try:
            netnum = float(net)
        except ValueError:
            print("")
            print("Error! Invalid character. Please enter a number to continue.")
            print("")
        sum = float(pcnt_dec * net)
        broker_sum = float(broker_dec * net)
        print("")
        print("Insurance Premium Tax Amount: £" + str(custround(sum)))
        print("")
        gross = net + sum
        print("Gross Premium: £" + str(custround(gross)))
        print("")
        print("Brokerage due: £" + str(custround(broker_sum)))
        print("")
        print("Press 'n' at any time to stop")

    elif question2 == "g":
        broker_dec = float(broker_float / 100)
        print("")
        gross = input("Gross Premium: £")
        try:
            grossnum = float(gross)
        except ValueError:
            print("")
            print("Error! Invalid character. Please enter a number to continue.")
            print("")

        gross_float = float(gross) #as before to convert str to float

        pcnt_dec2 = float(pcnt_float / 100)
        x = float(1 + pcnt_dec2)
        sum2 = float(gross_float / x)
        sum3 = float(sum2 - gross_float)
        sum4 = float(sum3 * -1)
        sum5 = float(gross_float - custround(sum4))
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