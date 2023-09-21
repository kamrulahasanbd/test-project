
try:
    def division(x):

        if x % 2 == 0:
            return x
        # z = x / y
        # return z
    
except ZeroDivisionError as a:
    print(a)   
except TypeError as a:
    print(a)
else:
    try:
        y = int(input(" enter any number between 0 to 10: "))
        result = division(y)
        if result:
            print("this is even number: ")
        else:
            print("this is odd number: ")
        #print(result)
    except:
        print(" must be put int value")
finally:
    print("end of exception")