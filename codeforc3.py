for i in range(int(input())):
    number_of_times,total_letters,string_lenth=map(int,input().split())
    string=str(input())
    for i in range(total_letters):
        flagj=0
        for j in range(string_lenth):
            if string[j]==chr(97+i):
                flagj=1
                break
        if flagj==1:
            checker=[0]*total_letters
            for k in range(j,string_lenth):
                checker[ord(string[k])-97]+=1
        
                
            
        
