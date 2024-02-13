a=[]
b=[]
C=[]
N=int(input())
for i in range(N):
    A,B=map(int,input().split())
    a.append(A)
    b.append(B)


B_max=max(b)

CH=[0]*B_max
for j in range(N):
    for k in range(a[j],b[j]):
        CH[k]+=1

ans=max(CH)
print(ans)
