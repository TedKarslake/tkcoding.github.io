print("")
first = input("Insurance Premium Tax Percentage: ")
print("")
second = input("Net Premium: ")
sum = float(second) + (float(first) / float(second) * 100)
print("Gross Premium: " + str(sum))
print("")
third = input("Gross Premium: ")
sum = float(third) - (float(first) / float(third) * 100)
print("Net Premium: " + str(sum))
print("")
fourth = 5
fifth = 7.5
sixth = 10
seventh = 12.5
eighth = 15
ninth = 17.5
tenth = 20
eleventh = 22.5
twelfth = 25
print("")
sum = (float(fourth) / float(second) * 100)
print("5%: " + str(sum))
print("")
sum = (float(fifth) / float(second) * 100)
print("7.5%: " + str(sum))
print("")
sum = (float(sixth) / float(second) * 100)
print("10%: " + str(sum))
print("")
sum = (float(seventh) / float(second) * 100)
print("12.5%: " + str(sum))
print("")
sum = (float(eighth) / float(second) * 100)
print("15%: " + str(sum))
print("")
sum = (float(ninth) / float(second) * 100)
print("17.5%: " + str(sum))
print("")
sum = (float(tenth) / float(second) * 100)
print("20%: " + str(sum))
print("")
sum = (float(eleventh) / float(second) * 100)
print("22.5%: " + str(sum))
print("")
sum = (float(twelfth) / float(second) * 100)
print("25%: " + str(sum))
print("")



sum = (float(second) / float(twelfth) * 100)
print("25%: " + str(sum))

print("")
def percentage(twelfth, second):
  return 100 * float(twelfth)/float(second)

