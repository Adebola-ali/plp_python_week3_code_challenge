# def large_power(base, exponent):
#     # Calculate the power of the base to the exponent
#     result = base ** exponent
    
#     # Check if the result is greater than 5000
#     if result > 5000:
#         return True
#     else:
#         return False

# # Example usage
# print(large_power(10, 3))  # Should return True (10^3 = 1000)
# print(large_power(5, 4))   # Should return True (5^4 = 625)


def large_power(base, exponent):
    # Calculate the power of the base to the exponent
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Get user input for base and exponent
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# Call the function and print the result
print(large_power(base, exponent))
