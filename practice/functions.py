# calculate sum of 2 numbers

'''
def sum(a, b):
    return a + b

ans = sum(3,4)
print(ans)
'''


# default parameters

'''
def sum (a = 0, b = 0):
    return a + b

ans = sum(True)
print(ans)

'''

'''
    2 types of function in python
        1. buit-in function
        2. user-defined function
'''


# write a function to calculate the factorial of n number

# def calculate_factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i

#     return fact

# n = int(input("Enter the number : "))

# print(calculate_factorial(n));


# Calculate factorial of n numbers

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n-1)

n = int(input("Enter the value of n: "))
print("Factorial is: ", factorial(n))