def two_knights(n):
    ways = (n**4 - 9 * n**2 + 24 * n) // 2
    return ways

# Example usage
n = 8  # Change this to the desired chessboard size
result = two_knights(n)
print(result)
