number_list = [ 158.0, 10.9, 4.5, 7.9, 66]
largest_position = 0
for i in range(len(number_list)):
    if number_list[i] > number_list[largest_position]:
        largest_position = i
        print('the number', number_list[largest_position],
              'index :', largest_position)
