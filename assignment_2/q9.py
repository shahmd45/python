'''
Write a function is_prime(n) that returns True if n is a prime number and otherwise False, using a loop.

Hint

We only check prime for 2 or numbers greater than 2. 2 Is the smallest prime number.
A number will always get divided by at least one number in range [2, n-1].

Non-Prime

For number 9 we'll check in range (2, 8) & it'll get divided by 3. So is non-prime & we'll return false for it.

Example

For number 7 we'll check in range (2, 6) & it won't get divided by any. So is prime & we'll return true for it.
'''


def is_prime(n):
    if n < 2:
        return False

    if n == 2: 
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number : "))
print(is_prime(n))