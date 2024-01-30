def minimum_gondolas(n, x, weights):
    weights.sort()  # Sort the weights in ascending order
    left, right = 0, n - 1  # Initialize pointers for the lightest and heaviest children
    gondola_count = 0

    while left <= right:
        # If the heaviest and lightest children can fit in one gondola, assign them together
        if weights[left] + weights[right] <= x:
            left += 1
            right -= 1
        else:
            # If they can't fit together, only assign the heaviest child to a gondola
            right -= 1
        gondola_count += 1

    return gondola_count

# Read input
n, x = map(int, input().split())
weights = list(map(int, input().split()))

# Output the result
result = minimum_gondolas(n, x, weights)
print(result)
