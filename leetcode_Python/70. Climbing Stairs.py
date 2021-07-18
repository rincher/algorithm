cache = {}


def memoization(n):
    if n not in cache.keys():
        cache[n] = climbStairs(n)
    return cache[n]


def climbStairs(n):
    if n <= 3:
        return n
    return memoization(n-1) + memoization(n-2)


n = 5
print(climbStairs(n))
