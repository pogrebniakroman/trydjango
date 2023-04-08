number = int(input('Enter prime check number: '))  # Enter value

def isPrime_checker(number):
    if number <= 1:
        return False                               # Check rule for value
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
   # return isPrime_checker(number)
print('Prime check number: ', isPrime_checker(number))
#This function is supposed to generate those many prime numbers, as taken as input argument 'num'

num = int(input('Enter range number: '))


num_list = []
i = 0
while len(num_list) <= num:
        num_list.append(i)
        i = i + 1
print(num_list)
for i in num_list:
    print(isPrime_checker(i))

























