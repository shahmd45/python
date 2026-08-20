'''
Write a function that prints the digits of a number n, 
for example: There are 3 digits in it: 3, 1, and 2, and we need to print them.
'''

# def print_digit(n):
#     while n > 0:
#         digit = n % 10
#         print(digit)
#         n = n // 10

# n = int(input("Enter the number : "))
# print_digit(n) # print number in reverse order


# 2 way to solve the problem

def print_digit(n):
    for i in str(n):
        print(i)

n = input("Enter the number: ")

print_digit(n)
