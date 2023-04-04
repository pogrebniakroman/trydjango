#linear_search_number = int(input('Enter search number: '))
list_input = input('Enter list numbers separated by space: ')
print("\n")
list = list_input.split()
print(list)
for i in range(len(list)):
    list[i] = int(list[i])
print(list)
search_number = int(input('Enter search number: '))
def linear_search(list_input):
    for i in range(len(list)):
        if list[i] == search_number:
            print('Search number: ', search_number)
            print('Id number: ', i)
            break


linear_search(list_input)



