try:
    user_age = input("Enter your age: ")
    convert_int = int(user_age)
    print("your age is: ", convert_int)
except ValueError:
    print("wrong input")

    