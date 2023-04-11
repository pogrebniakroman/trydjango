
number = int(input('Enter prime check number: '))  # Enter value

def isPrime_checker(number):
    if number <= 1:
        return False                               # Check rule for value
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
    return isPrime_checker(number)
print('Prime check number: ', isPrime_checker(number))
#This function is supposed to generate those many prime numbers, as taken as input argument 'num'

num = int(input('Enter range number: '))

def prime_checker(num):
    prime_checker_list = []
    i = 0
    while len(prime_checker_list) < num - 2:
         if i > 1:
            prime_checker_list.append(i)
         i = i + 1
    return prime_checker_list
print(prime_checker(num))

def checker():
    prime_list = []
    i = 1
    for i in range(num):
        if isPrime_checker(i) is True:
            prime_list.append(i)
        i = i + 1
    return prime_list

print(checker())




