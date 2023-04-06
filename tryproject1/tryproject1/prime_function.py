# Create a prime_checker(num):
# return True, if prime
# return False, if not
num = int(input('Enter check number: '))

def prime_checker(num):
    prime_checker_list = []
    i = 0
    while len(prime_checker_list) <= num:
        prime_checker_list.append(i)
        i = i + 1
    print(prime_checker_list)
    for j in range(1, num):
        if num % prime_checker_list[j] == 0:
            print(j)
    return prime_checker_list
print(prime_checker(num))






