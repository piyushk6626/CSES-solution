def same_bit_representation(num1, num2):
    # Get binary representation of the numbers
    bin_num1 = bin(num1)[2:]
    bin_num2 = bin(num2)[2:]

    # Find the maximum length of the binary representations
    max_len = max(len(bin_num1), len(bin_num2))

    # Format the binary representations with leading zeros
    bin_num1 = bin_num1.zfill(max_len)
    bin_num2 = bin_num2.zfill(max_len)

    return bin_num1, bin_num2

# Example usage
num1 = 7
num2 = 10
result_num1, result_num2 = same_bit_representation(num1, num2)

print(f"Binary representation of {num1}: {result_num1}")
print(f"Binary representation of {num2}: {result_num2}")
