for _ in range(int(input())):
    N=int(input())
    A=str(input())
    count=0
    flag=0
    for i in range(N-1):
        if A[i]=='*' and A[i+1]=='*' :
            flag=1
            break
        else:
            if A[i]=='@':
                count+=1
    
    if flag==0 and A[N-1]=='@':
        count+=1
    
    print(count)