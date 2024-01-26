Dna_sequence=str(input())
Max_Lenth=0
temp=0
for i in range(len(Dna_sequence)-1):
    if Dna_sequence[i]==Dna_sequence[i+1]:
        temp=temp+1
        if temp>Max_Lenth:
            Max_Lenth=temp
    else:
        temp=0
print(Max_Lenth+1)