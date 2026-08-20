'''
Write a program that takes salary as input. Using conditional statements, calculate the final tax based on these rules:

If salary < 30,000 → 5%
If salary is 30,000 - 70,000 → 15%
If salary > 70,000 → 25%

'''

n = int(input("Enter salary in number => "))
salary = n * 1000

tax = 0

if salary < 30000:
    tax = (salary * 5) / 100
elif salary <= 70000:
    tax = (salary * 15) / 100
else:
    tax = (salary * 25) / 100

print("Tax amount:", tax)
print("Final salary after tax:", salary - tax)
