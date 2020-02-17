import sys

def is_prime(num):
    """Returns True for prime numbers, False if otherwise."""
    if num < 2:
        return False
    for factor in range(2,num):
        if num % factor == 0:
            return False
    return True

try:
    num = int(sys.argv[1])
    isPrime = is_prime(num)
    if isPrime:
        print(f'{num} is a prime!')
    else:
        print(f'{num} is not a prime!')
except:
    print('Prints if the given number is a prime.')
    print('Example: `py 16_prime.py 5` `5 is a prime!`')