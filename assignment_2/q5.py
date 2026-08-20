# Write a function to return the sum of digits of a number n.

def sum_of_digits(n):
    sum = 0

    while(n > 0):
        digit = n % 10
        sum += digit

        n = n // 10

    return sum

n = int(input("Enter the number: " ))

print(sum_of_digits(n))