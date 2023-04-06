max_list = [12, 43, 4, 6, 34, 634, 34, 13]
max_num = 0
for i in range(1, len(max_list)):
    value_sort = max_list[i]

    while max_list[i - 1] > value_sort and i > 0:
        max_list[i], max_list[i - 1] = max_list[i - 1], max_list[i]
        i = i - 1
print(max_list)



