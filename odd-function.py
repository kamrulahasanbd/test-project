
# def odd(x):

#     list = []
#     list_odd =[]
#     y = 0
#     while y <= 10:
#         z = input("please type no: ")
#         list.append(z)
        
        
#         if z % 2 != 0:
#             list_odd.append(z)
#             y+=1
#             return z
            

# result = print(odd(list))
# print(result)

def even(args):

    new_list = []
    for x in args:
        if x % 2 == 0:
            new_list.append(x)
            
    return new_list
           #x +=1 

result = even([2, 3, 5, 6, 7, 8,9,11,12,13,14,17])
print(result)