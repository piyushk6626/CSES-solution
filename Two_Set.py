n=int(input())
if n%4==0 or n%4==3 :
    print("YES")
    if n%4==0:
        print(n//2)
        First_point=1
        Last_point=n
        for i in range(n//4):
            print(First_point,end=" ")
            print(Last_point,end=" ")
            First_point+=1
            Last_point-=1
        print()
        print(n//2)
        while(First_point!=Last_point+1):
            print(First_point,end=" ")
            First_point+=1
    else:
        print(n//2)
        First_point=1
        Last_point=n-1
        for i in range(n//4):
            print(First_point,end=" ")
            print(Last_point,end=" ")
            First_point+=1
            Last_point-=1
        print(n)
        print(n//2+1)
        while(First_point!=Last_point+1):
            print(First_point,end=" ")
            First_point+=1
        
    
else:
    print("NO")