def int_to_binary(num,width):
    
    binary_result = format(num, f'0{width}b')
    
    return binary_result
    
def find_msb(num):
    msb_position = 0
    while num > 1:
        num = num >> 1
        msb_position += 1

    return msb_position



for i in range(int(input())):
    a,b,r=map(int,input().split())
    if a<b:
        small=a
        big=b
    else:
        small=b
        big=a
        
    MSB_num=find_msb(big)
    
    Multipal_factor=int(pow(2,MSB_num))
    big_num_bin=int_to_binary(big,MSB_num)
    small_num_bin=int_to_binary(small,MSB_num)
    x=0
    print(big_num_bin)
    print(small_num_bin)
    for i in range(MSB_num):
        if big_num_bin[i]=='1' and small_num_bin[i]=='0':
            temp=x+Multipal_factor
            #print(temp)
            if temp<=r:
                x=x+Multipal_factor
        Multipal_factor=Multipal_factor//2
    #print(x)    
    ans=abs((big^x)-(small^x))
    print(ans)
        
    