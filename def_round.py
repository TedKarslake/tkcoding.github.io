def custround(num):#this is to round non whole numbers to two decimal places.
    if type(num) != float:
        return(num)
    strnum = str(num)
    split_string_num = strnum.split(".")
    decimals = split_string_num[1]
    if len(decimals) < 3:
        return(num)
    if decimals[1] == "5":
        return(round(float(num + 0.001),2))
    else:
        return(round(num, 2))

if __name__ == "__main__":
    tests = [5.5, 6.15, 7.8654, "58.68", 5, 100541.156, 104172.955]
    for i in tests:
        print(custround(i))
