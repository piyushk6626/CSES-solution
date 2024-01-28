def int_to_binary(num,width):
    
    binary_result = format(num, f'0{width}b')
    
    return binary_result
def printing(arr):
    result = ''.join(map(str, arr))
    print(result)

n=int(input())
A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16=2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072
ans=[0]*n
k=0
for i in range(int(pow(2,n))):
    printing(ans)
    if k>(A1-1): 
    

    
    
    