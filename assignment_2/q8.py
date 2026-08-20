#Create a function that performs addition, subtraction, multiplication, or division based on the parameter.
# calculator(a, b, operation)

def calculator(a, b, op):
    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b

a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
op = input("Enter the operator : ")

print(calculator(a, b, op))