def main():
    Number_of_applicants,number_of_apartments,maximum_allowed_difference=map(int,input().split())
    applicants=list(map(int,input().split()))
    apartments=list(map(int,input().split()))
    
    applicants.sort()
    apartments.sort()
    
    i=0
    j=0
    count=0
    
    while(j<number_of_apartments and i <Number_of_applicants):
        if   (applicants[i]-maximum_allowed_difference)<= apartments[j]<=(applicants[i]+maximum_allowed_difference) :
            count+=1
            i+=1
            j+=1
        elif (applicants[i]-maximum_allowed_difference)> apartments[j]:
            j=j+1
        elif (applicants[i]+maximum_allowed_difference)< apartments[j]:
            i=i+1
    
    print(count)

main()