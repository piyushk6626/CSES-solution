def int_to_binary(num,width):
    
    binary_result = format(num, f'0{width}b')
    
    print(binary_result)

def is_power_of_two(number):
  
    return number > 0 and (number & (number - 1)) == 0

n=int(input())
Max=int(pow(2,n))
Ans=[0,1]

K=2
J=1
num=1

while(K <Max):
    if is_power_of_two(K):
        num=num+K
        Ans.append(num)
        K=K+1
    else:
        while(J>0):
            DIFF=Ans[J]-Ans[J-1]
            num-=DIFF
            Ans.append(num)
            J=J-1
            K=K+1
        J=len(Ans)-1    

for number in Ans:
    int_to_binary(number,n)

    
        
    
    
    

    
    
    