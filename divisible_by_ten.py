def divisible_by_ten(num):
    # calculating remainder using modulus
    remainder = number % 10
    # Check if number is divisible by ten
    if remainder == 0:
        return True
    else:
        return False

# Taking user input
number = int(input('Enter a number: '))
# divisible_by_ten(print(f'{number} is divisible by 10'))
# print(divisible_by_ten(number))
print(f'{number} is divisible by 10 \n{divisible_by_ten(number)}')