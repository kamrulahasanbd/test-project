
try:
     def list_element_access(fun_index):
        index = user_list.index(fun_index)  
        return index

     user_index = int(input("enter your number from the list: "))
     user_list = [21, 12, 43, 24, 15, 6, 17, 68, 9, 10, 11, 12]
     index_number =list_element_access(user_index)
     print(index_number,f"is index number of {index_number} in the list ")

except ValueError as e:
  print("Enter number not found in the list")