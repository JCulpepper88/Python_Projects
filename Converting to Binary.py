num = 10
binary_representation = bin(num)[2:]
print(binary_representation)


def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2  # Get remainder when divided by 2 (either 0 or 1)
        binary = str(remainder) + binary  # Append remainder to the left
        n = n // 2  # Divide number by 2 and take the integer part
    return binary

# Example:
print(decimal_to_binary(15))  # Output: '1010'