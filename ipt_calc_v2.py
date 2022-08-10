from def_round import custround

print("")
pcnt = float(input("Insurance Premium Tax Percent: "))
broker = float(input("Brokerage Percent: "))

print("")

question = input("Press 'y' then [Enter key] for Net Premium input, 'n' then [Enter key] for Gross Premium input: ")

if  question == "y":
    pcnt_dec = float(pcnt / 100)
    broker_dec = float(broker / 100)
    print("")
    net = float(input("Net Premium: £"))
    sum = float(pcnt_dec * net)
    broker_sum = float(broker_dec * net)
    print("")
    print(sum)
    print("Insurance Premium Tax Amount: £" + str(custround(sum)))
    print("")
    gross = net + sum
    print(gross)
    print("Gross Premium: £" + str(custround(gross)))
    print("")
    print(broker_sum)
    print("Brokerage due: £" + str(custround(broker_sum)))
    print("")

elif question == "n":
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

else:
    print("Sorry, please enter lowercase 'y' or lowercase 'n'.")

q2 = input("Would you like to calculate another? (press 'y' to continue, 'n' to exit): ")

while q2 == "y":

    print("")
    question = input("Press 'y' then [Enter key] for Net Premium input, 'n' then [Enter key] for Gross Premium input. Enter 'exit' at any time to stop: ")

    if  question == "y":
        pcnt_dec = float(pcnt / 100)
        broker_dec = float(broker / 100)
        print("")
        net = float(input("Net Premium: £"))
        sum = float(pcnt_dec * net)
        broker_sum = float(broker_dec * net)
        print("")
        print("Insurance Premium Tax Amount: £" + str(sum))
        print("")
        gross = net + sum
        print("Gross Premium: £" + str(gross))
        print("")
        print("Brokerage due: £" + str(broker_sum))
        print("")

    elif question == "n":
        broker_dec = float(broker / 100)
        print("")
        gross2 = float(input("Gross Premium: £"))
        pcnt_dec2 = float(pcnt / 100)
        x = float(1 + pcnt_dec2)
        sum2 = float(gross2 / x)
        sum3 = float(sum2 - gross2)
        sum4 = float(sum3 * -1)
        sum5 = float(gross2 - round(sum4))
        broker_sum = float(broker_dec * sum5)
        print("")
        print("Insurance Premium Tax Amount: £" + str(sum4))
        print("")
        print("Net Premium: £" + str(sum5))
        print("")
        print("Brokerage due: £" + str(broker_sum))
        print("")

    elif question == "exit":
        break

    else:
        print("")
        print("Enter 'exit' at any time to stop.")
