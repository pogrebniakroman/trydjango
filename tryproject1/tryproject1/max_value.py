
num_list = [12,43,4,6,34,634,34,13]
max_num = num_list[0]
comparing_number = int(input('Enter comparing number: ')) #enter comparable number
for i in num_list:
    if i > max_num:
        max_num = i                                       #find maximum number in the num_list

if max_num < comparing_number:                            #compare maxmimum number and enter value
    num_list.remove(max_num)                              #remove maximum nubmber of num_list
    num_list.append(comparing_number)                     #add number
print(num_list)







