def true_str(prompt):
    #this is to make sure users enter 'y' or 'n' in IPT Calc v3
    while True:
        try:
            prompt == str('y'), str('n')
        except:
            prompt = input("Please only enter 'y' or 'n' then [Enter] to continue.")
        continue