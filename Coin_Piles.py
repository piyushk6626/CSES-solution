for _ in range(int(input())):
    X,Y=map(int,input().split())
    x=max(X,Y)
    y=min(X,Y)
    if x>2*y:
        print("NO")
    elif (x+y)%3==0:
        print("YES")
    else:
        print("NO")