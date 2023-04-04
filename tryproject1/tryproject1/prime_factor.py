def isPrime(x):
    # invalid input
    if x <= 1:
        return False

    # process all potential divisors
    for i in range(2, x):
        if x % i == 0:
            return False

            # no divisor found, therfore it's a prime number
    return True


# the number to we want largest prime factor of
number = 123

# iterate from half of the number to 2 as there can be no factor
# greater than half of the number.
for i in range(number // 2, 2, -1):
    # check if number is a factor
    if number % i == 0:
        # check if factor is also a prime
        if isPrime(i):
            # add the number to the list
            print("Largest prime factor = ", i)
            break
