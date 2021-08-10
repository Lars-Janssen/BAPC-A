amount = int(input())
for i in range(amount):
    number = int(input())
    primes = [True for i in range(number + 1)]
    p = 2
    while(p*p < number):
        if(primes[p] == True):
            for y in range(2*p, number + 1, p):
                primes[y] = False
        p+=1
    primes[0] = False
    primes[1] = False
    primenumbers = []
    for y in range(0, number):
        if(primes[y] == True):
            primenumbers.append(y)
    representanten = []
    for y in primenumbers:
        if(y <= number//2 and (number - y) in primenumbers):
            representanten.append(y)
    print("{} {} {} {}".format(number, "has", len(representanten), "representation(s)"))
    for y in range(len(representanten)):
        print("{}{}{}".format(representanten[y], "+", number - representanten[y]))
    print()
