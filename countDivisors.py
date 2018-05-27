#!/usr/bin/python

maxDivisors = 1
numWithMax = 1
n = 2

while n != 10001:
	divisorCount = 0
	for x in xrange(1,n):
		if (n % x) == 0:
			divisorCount +=1

		if (divisorCount > maxDivisors):
			maxDivisors = divisorCount
			numWithMax = n
	n  += 1

print "The maximum number of divisors is ", maxDivisors 
print "A number with max divisors is ", numWithMax