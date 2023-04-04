num_list = [12,43,4,6,34,634,34,13]
new_num_list = []
j = len(num_list)

while j > 0:
    max_num = 0
    max_index = 0
    for i in range(len(num_list)):
      if num_list[i] > max_num:
        max_num = num_list[i]
        max_index = i
    print('The maximum number is', max_num) #correct
    print('The index of the maximum number is', max_index)

    num_list.remove(max_num)
    new_num_list.append(max_num)

    print(num_list)
    print(new_num_list)

    j = j - 1