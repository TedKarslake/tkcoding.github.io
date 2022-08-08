from def_round import custround

print("")
question2 = input("Would you like to calculate your Insurance Premium? (press 'y' then [Enter key] to continue, input 'n' then [Enter key] to exit): ")
print("")
    
while question2 == "y":

    print("")
    
    pcnt = float(input("Insurance Premium Tax Percent: "))
    broker = float(input("Brokerage Percent: "))

    print("")

    question = input("Press 'p' then [Enter key] for Net Premium input, 'g' then [Enter key] for Gross Premium input. Enter 'n' then [Enter key] at any time to stop: ")

    if  question == "p":
        pcnt_dec = float(pcnt / 100)
        broker_dec = float(broker / 100)
        print("")
        net = float(input("Net Premium: £"))
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
        gross2 = float(input("Gross Premium: £"))
        pcnt_dec2 = float(pcnt / 100)
        x = float(1 + pcnt_dec2)
        sum2 = float(gross2 / x)
        sum3 = float(sum2 - gross2)
        sum4 = float(sum3 * -1)
        sum5 = float(gross2 - custround(sum4))
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
