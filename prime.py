#!/usr/bin/python
counter = 0

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

prime_range = int(raw_input("Prime range: "))

for x in xrange(1, prime_range +1 ):
    if is_prime(x) == True:
        counter += 1

print "There are", counter, "prime numbers from 1 to", prime_range
