def find(list, search_number):
    for i in list:
        if i == search_number:
            print('We search this number:', end=' ')
            return search_number
    raise ValueError('This number is not listed')

try:
    search_number = 3
    list = [1, 2, 3, 4, 5, 6]
    found = find(list, search_number)
    print(found)

except ValueError as message:
    print(message)


#------------------------------------------------Task 2------------------------------------------------#


# def delete(lst, delete_num):
#     if delete_num in lst:
#         lst.remove(delete_num)
#         return lst
#     else:
#         raise ValueError('This number is not listed')

# try:
#     my_list = [1, 2, 3, 4, 5]
#     delete_num = 3
#     new_list = delete(my_list, delete_num)

#     print('Deleted:', delete_num)
#     print('Updated list:', new_list)

# except ValueError as message:
#     print(message)




#------------------------------------------------Task 3 ------------------------------------------------#

# def check(num):

#     if num % 2 == 0:
#         return num
#     else:
#         raise ValueError('Wrong number')

# try:
#     number = 3
#     result = check(number)
#     print('the number', result ,  'is even')

# except ValueError as e:
#     print(e)
