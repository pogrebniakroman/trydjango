
input_cub_number = int(input('Enter number which need transform to cub: '))
dictionary_cub = {}
i = 0
while len(dictionary_cub) <= input_cub_number:
    dictionary_cub.update({i: i*i})
    i = i + 1
print(dictionary_cub)