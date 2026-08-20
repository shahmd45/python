# Write a function to return the count the number of digits in a number n.

def count_number(n):
    count = 0

    while(n > 0):
        n = n // 10
        count += 1

    return count

n = int(input("Enter the number: "))
print(count_number(n))