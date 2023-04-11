number = int(input('Enter prime check number: ')) # Enter value
def isPrime_checker(number):
    check = True
    if number <= 1:
         check = False # Check rule for value
    for i in range(2, number):
        if number % i == 0:
             check = False
    if check == True:
     return True
    else:
        return False

print('Prime check number: ', isPrime_checker(number))

num = int(input('Enter range number: '))

def prime_checker(num):
    prime_checker_list = []
    i = 0
    while len(prime_checker_list) < num:
        if i > 1 and isPrime_checker(i) == True:
            prime_checker_list.append(i)
        i = i + 1
    return prime_checker_list
print(prime_checker(num))



