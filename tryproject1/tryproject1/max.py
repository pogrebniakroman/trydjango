num_list = [12,43,4,6,34,634,34,13]
max_num = 0
max_index = 0
x = 0
new_num_list = []
for i in range(len(num_list)):
        if num_list[i] > max_num:
           max_num = num_list[i]
           max_index = i
num_list.remove(max_num)
new_num_list.append(max_num)
#find maximum number in the num_list


new_max_list = num_list
new_max_num = 0
for j in range(len(new_max_list)):
    if new_max_list[j] > new_max_num:
       new_max_num = num_list[j]

print(num_list)
print(new_num_list)
print(new_max_list)
print(new_max_num)
print('The maximum number is', max_num) #correct
print('The index of the maximum number is', max_index)
new_sort_list = []


