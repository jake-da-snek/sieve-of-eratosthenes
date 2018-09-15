def sieve():
    n = input("Enter the maximum range: ")
    primes = []     # init array
    p = 2       # constant since 2 is the smallest prime number
    for i in range(n+1):        # create an array with an index of n+1
        primes.append(True)
    while p * p <= n:       # if p^2 is outside our set, then we know we have already reached the largest prime in the set
        if primes[p] == True:
            for i in range(p * p, n+1, p):      
                 primes[i] = False
        p += 1
    for i in range(2, n+1):
        if primes[i]:
            print(i)

sieve()
