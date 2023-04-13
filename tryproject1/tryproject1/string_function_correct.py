my_set =  {'qwerty', 2, 'banana'}
your_set = {'apple', 'melone', 5}
my_set.add(1)
new_set = my_set.union(your_set)
print(new_set)
new_set.update(your_set)
print(new_set)
print(3 in new_set)
new_set.remove('qwerty')
new_set.clear()
print(new_set)

fruit1 = {'apple','mango','cherry'}
fruit2 = {'apple','papaya','pineapple'}

fruit1.union(fruit2) #joining


#intersection

#symmetric_difference
print(fruit1.symmetric_difference(fruit2))
print(fruit1.difference(fruit2))
print(fruit2.difference(fruit1))
print(fruit1.intersection(fruit2))

