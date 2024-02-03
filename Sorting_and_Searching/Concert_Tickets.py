# def list_to_sorted_dict(lst):
#     """
#     Convert a list to a dictionary of value and index, and then sort it based on values.

#     Parameters:
#     - lst (list): The input list.

#     Returns:
#     - dict: A sorted dictionary where keys are values from the list, and values are their indices.
#     """
#     # Create an unsorted dictionary
#     unsorted_dict = {value: index for index, value in enumerate(lst)}
    
#     # Sort the dictionary based on values
#     sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))
    
#     return sorted_dict

# def main():
#     number_of_tickets, number_of_customers = map(int, input().split())
#     Price_of_tickets = list(map(int, input().split()))
#     maximum_price_given_by_customer = list(map(int, input().split()))
#     Price_of_tickets.sort()
#     sorted_dict = list_to_sorted_dict(maximum_price_given_by_customer)
    
#     ans = [0] * number_of_customers
#     price = list(sorted_dict.keys())
#     custmor_index = list(sorted_dict.values())
    
#     i = 0
#     j = 0
#     while i < number_of_tickets and j < number_of_customers:
#         if price[j] >= Price_of_tickets[i]:
#             ans[custmor_index[j]] = Price_of_tickets[i]
#             i += 1
#             j += 1
#         else:
#             j += 1
#             ans[custmor_index[j - 1]] = -1
            
#     print(*ans)

# main()
from bisect import bisect_right

def main():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))
    s = sorted(h)

    for val in p:
        index = bisect_right(s, val)

        if index == 0:
            print("-1")
        else:
            index -= 1
            print(s[index])
            del s[index]

if __name__ == "__main__":
    main()

