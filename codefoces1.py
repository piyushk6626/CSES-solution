for _ in range(int(input())):
    n, k = map(int, input().split())
    ans = [0] * (n * k)
    count = 0
    z = 0
    for i in range(n):
        for j in range(k):
            ans[z] = chr(j + 97)
            z += 1

    result = ''.join(map(str, ans))
    print(result)
