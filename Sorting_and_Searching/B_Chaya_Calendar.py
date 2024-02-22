for _ in range(int(input())):
    N=int(input())
    Arr=list(map(int,input().split()))
    Curr=Arr[0]
    
    for i in range(1,N):
        temp=Arr[i]
        while(Arr[i]<=Curr):
        
            Arr[i]=Arr[i]+temp
        if Arr[i]==Curr:
            Arr[i]=Arr[i]+temp    
        Curr=Arr[i]
        
    
    print(Curr)
            
        
        
    