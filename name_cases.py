print("")
first_name = "Eric"
last_name = "Clapton"
full_name = f"{first_name} {last_name}" # variable values are used by enclosing items in {} in the string
print(first_name)
print(last_name)
print(full_name)
print("")
print(f"Hello, {full_name}, would you like to learn some Python today?")
print("")
message = f"Hello, {full_name}, would you like to learn some Python today?" # there are two ways of using f-strings in Python
print(message)
print("")
print(full_name.title()) # string to format as title, with beginning letters upper case
print(full_name.upper()) # string to format all upper case
print(full_name.lower()) # string to format all lower case
print("")
quote = "'Life is like a box of chocolates, you never know what you're gonna get.'"
celebrity = "Tom Hanks as Forrest Gump "
print((celebrity) + "once said: " + (quote)) # make sure all of the algorithm is within brackets to work
print("")
sentence = f" is one of the greatest guitarists of all time. {last_name} was part of Cream, then had a solo career."
print((full_name) + (sentence))
print("")
print("Charlie Day")
print("\tCharlie Day")
print("\nCharlie Day")
print("")
print("Languages:\n\tPython\n\tC Code\n\tJavascript") # the cmd \n pushes to the left, the cmd \t pushes to the right. \n\t formats new line with spacing
print("")




first_name1 = input("What is your first name? ")
second_name1 = input("What is your second name? ")
full_name1 = f"{first_name1} {second_name1}"
print(f"\nHello, {full_name1}, would you like to learn some Python today?")
message = f"\nHello {full_name1}, would you like to learn some Python today?"

print(full_name1.lower())
print(full_name1.upper())

quote1 = "'Did you touch my drum set?' "
film = "Step Brothers."
print("")
print((quote1) + "from the film " + (film))
print("")

