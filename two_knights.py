def two_knights(n):
    ways = (n**4 - 9 * n**2 + 24 * n) // 2
    return ways
n=int(input())
for i in range(1,n+1):
    result = two_knights(i)
    print(result)
