from collections import Counter
import sys
input = sys.stdin.readline
n= int(input())
X=list(map(int,input().split()))
X.sort()
ans=0
for i in range(n-1):
    if X[i]!=X[i+1]:
        ans=ans+1
print(ans+1)