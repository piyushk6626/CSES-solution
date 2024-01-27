def count_elements(input_string):
    # Create an empty dictionary to store the counts
    element_counts = {}

    # Iterate through each character in the string
    for char in input_string:
        # Increment the count for the current character in the dictionary
        element_counts[char] = element_counts.get(char, 0) + 1
    return element_counts

# finding number of elelment whcich are ocuring odd number of times
def number_of_odd(element_counter):
    odd = 0
    for count in element_counter.items():
        if count[1] % 2 == 1:
            odd += 1
    return odd
            

def main():
    string=str(input())
    element_counts=count_elements(string)
    Odd_number=number_of_odd(element_counts)
    Strat_Point=0
    End_Point=len(string)-1
    if (Odd_number==1 and (len(string)%2==1)) :
        
        ans=[0]*(len(string))
        for element, count in element_counts.items():
            if count%2==1:
                temp=len(string)//2
                ans[temp]=element
                count-=1
                
        for element, count in element_counts.items():
            
            while(count>1):
                ans[Strat_Point]=element
                ans[End_Point]=element
                Strat_Point+=1
                End_Point-=1
                count-=2
                
        result = ''.join(map(str, ans))
        print(result)
        
    
        
    elif (Odd_number==0 and (len(string)%2==0)):
        ans=[0]*(len(string))
        for element, count in element_counts.items():
            while(count>0):
                ans[Strat_Point]=element
                ans[End_Point]=element
                Strat_Point+=1
                End_Point-=1
                count-=2
        result = ''.join(map(str, ans))
        print(result)
       
    else:
        print("NO SOLUTION")
        
main()    