# An example of how to get even numbers
for i in range(10):
    if i % 2 == 0:
     print(i)
# Create a function which checks
# if a number is even or not
# if even, return True
# if not, return False
##############
# Take a number as an input argument
# create a list of even numbers
# till the number taken as input argument

# even_list_maker(50)
# [2,4,..... 50]

# even_list_maker(7)
# [2,4,6]
def even_checker(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(even_checker(9))
#number = int(input('Input check number:'))
def even_list_maker(number):
    list_even_number = []
    for i in range(number):
        if even_checker(i) == True:
            list_even_number.append(i)
    return list_even_number
print(even_list_maker(5))
# Take a number as an input argument
# create a list of 'THOSE MANY' even
# numbers as the input argument

# even_list_maker(4)
# [2,4,6,8]

# even_list_maker(10)
# [2,4,6,8,10,12,14,16,18,20]
def even_list_maker(number):
    list_even_number = []
    j = 0
    while len(list_even_number) < number:
        if even_checker(j) == True:
            list_even_number.append(j)
        j = j + 1
    return list_even_number
print(even_list_maker(8))
