for _ in range(int(input())):
    N,X=map(int,input().split())
    Arr=list(map(int,input().split()))
    S=str(input())
    Product=1
    for num in Arr:
        Product=Product*num
    
    Ans=[]
    Ans.append(Product%X)
    Left=0
    Right=N-1
    for i in range(N):
        if Left==Right:            
            break
        
        if S[i]=='L':
            Product=Product//Arr[Left]
            Left+=1
            Ans.append(Product%X)
        else:
            Product=Product//Arr[Right]
            Right-=1
            Ans.append(Product%X)
            #print(f" Left={Left} Right={Right} appended={Product%X}")
            
    
    print(*Ans)
        
            
        