def round10(n):
    if(n % 10 < 5):
        return n - n % 10
    else:
        return n + (10 - n % 10)

def centsavings_td(items, D):
    def cost(n, d):
        # In this nested function, the variables `cumsums`, `memo`, `N` and `items` are available.
        if memo[n][d] == 10**9:
            # The code below should be a minimal change to `centsavings_memo`.
            # YOUR CODE HERE
            if n == 0:
                return 0
            if d == 0:
                return round10(cumsums[n])
            # Be sure to *set* memo[n][d]!
            best = round10(cumsums[-1])
            for k in range(0,n):
                best = min(best, cost(k, d-1) + round10(cumsums[n] - cumsums[k]))
            memo[n][d] = best
            return best
        return memo[n][d]

    N = len(items)
    cumsums = [0 for _ in range(N+1)]
    # Fill the cumsums list.
    # YOUR CODE HERE
    for k in range(0,N+1):
        cumsums[k] = sum(items[:k])
    assert cumsums[-1] == sum(items), "Did you fill the `cumsums` list until its final index?"
    memo = [[10**9 for _ in range(D+1)] for _ in range(N+1)]
    return cost(N, D)

firstline = input().split()
itemamount = int(firstline[0])
dividers = int(firstline[1])
secondline = input().split()
items = [int(secondline[i]) for i in range(itemamount)]
print(centsavings_td(items, dividers))