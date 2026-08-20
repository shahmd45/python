'''
Write a function that takes two integers and prints all even numbers between them (inclusive).
'''
def print_even_number(a, b):
    for i in range(a, b+1):
        if (i % 2 == 0):
            print(i)

a = int(input("Enter number for a : "))
b = int(input("Enter number for b : "))

print_even_number(a, b)
    