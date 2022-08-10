




print("")
def calculate_gross_premium(net_premium_input, tax_percentage_input):
  return net_premium_input * (1 + (tax_percentage_input / net_premium_input))
print("")
def calculate_gross_premium(gross_premium_input, tax_percentage_input):
  return gross_premium_input * (1 + (tax_percentage_input / 100))
print("")