n = int(input())
arr = [0, 6, 28, 96]
 
if n <= 4:
    for i in range(n):
        print(arr[i])
else:
    for i in range(4):
        print(arr[i])
 
    for i in range(5, n+1):
        corner = ((i*i) - 2) * 4
        ad_corner = ((i*i) - 3) * 8
        edge = (i*i - 4) * ((i*i) - ((i-1)*(i-1)) - 12)
        mid_sqr_corner = (i*i - 4) * 4
        mid_edge = (i*i - 6) * (((i-1)*(i-1)) - ((i-2)*(i-2)) - 4)
        mid_sqr = (i*i - 8) * ((i-4)*(i-4))
        ans = (corner + ad_corner + edge + mid_sqr_corner + mid_edge + mid_sqr) // 2
        print(ans)