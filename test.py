test3word = input("Tell me your lucky number: ")

try:
    test3num = int(test3word)
    print("This is a valid number! Your lucky number is: ", test3num)
except ValueError:
    print("This is not a valid number. It isn't a number at all! This is a string, go and try again. Better luck next time!")