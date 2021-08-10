tests = int(input())
for i in range(tests):
    line = input().split()
    number = int(line[0])
    e = int(line[1])
    primes = [True for i in range(number + 1)]
    divisors = []
    p = 2
    while(p*p < number):
        if(primes[p] == True):
            if(number % p == 0):
                number = number // p
                divisors.append(p)
                divisors.append(number)
                break
            for y in range(2*p, number + 1, p):
                primes[y] = False
        p+=1
    primes[0] = False
    primes[1] = False
    primenumbers = []
    for y in range(0, number):
        if(primes[y] == True):
            primenumbers.append(y)
    phi = (divisors[0]-1)*(divisors[1]-1)
    d = 1
    while(d*e % phi != 1):
        d+= 1
    print(d)

