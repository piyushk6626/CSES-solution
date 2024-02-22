for _ in range(int(input())):
    Lenth,Loctaion=map(int,input().split())
    Arr=[1]
    Two_power=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]
    curr=1
    j=0
    temp=1
    Loctaion=0
    while (j <=30):
        temp=curr*Two_power[j]
        if temp>Lenth:
            j=j+1
            curr=1
        else:
            Arr.append(temp)
            curr+=2
    print(Arr[Loctaion])