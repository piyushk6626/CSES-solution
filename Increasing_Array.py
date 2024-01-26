size_of_arr=int(input())
arr=list(map(int,input().split()))
total=0
for i in range(1,size_of_arr):
    temp=arr[i-1]-arr[i]
    if temp>0:
        total+=temp
        arr[i]=arr[i-1]
        
print(total)