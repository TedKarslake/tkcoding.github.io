print("")
pcnt = float(input("Insurance Premium Tax Percent: "))
broker = float(input("Brokerage Percent: "))

print("")

question = input("Press 'y' then [Enter key] for Net Premium input, 'N' then [Enter key] for Gross Premium input: ")
print(" ")
x = 1
while x == 1:
    try:
        age = str(question)
        x = 0
    except:
        birth_year = input("Please only enter the numerical digit YEAR. Enter your birth year to continue: ")
        print(" ")

while question == "y":
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
        
while question == "n":
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

