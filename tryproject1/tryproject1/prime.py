number = int(input('Enter prime check number: '))  # Enter value

def isPrime_checker(number):
    if number <= 1:
        return False                               # Check rule for value
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
print('Prime check number: ', isPrime_checker(number))