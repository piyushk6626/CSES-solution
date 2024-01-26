N=int(input())
A=list(map(int,input().split()))
ans=N*(N+1)/2- sum(A)
print(int(ans))