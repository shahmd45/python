# Design a program to continuously input a number from user and 
# print if it is positive or negative until the user enters “Quit”.


while True: 
    n = input("Enter the number or type Quit : ")

    if n == "Quit":
        break

    number = int(n)

    if(number > 0):
        print("Positive")
    elif number < 0:
        print("Negative")
    else: 
        print("Zero")


