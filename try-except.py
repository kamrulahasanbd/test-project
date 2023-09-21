try: 
    while True:
        try:
            user_n1=float(input("enter 1st num here: "))
            user_n2=float(input("enter 2nd num here: "))
            result = user_n1 / user_n2
            print(result)
            if result:
                break
            else:
                continue
        except ZeroDivisionError:
            print("division by zero not allowed")
except ValueError:
        print("please enter correct value")