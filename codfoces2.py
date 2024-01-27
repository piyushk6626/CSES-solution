for _ in range(int(input())):
    SUM,Numbers=map(int,input().split())
    Higest=SUM//Numbers
    ans=1
    for i in range(Higest,0,-1):
        if SUM%i==0:
            ans=i
            break
    print(ans)