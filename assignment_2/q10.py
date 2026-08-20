'''
Given a secret number (already decided by you), write a program that asks the user to guess it and prints:

If the guess is above the number: "Too high"
If the guess is below: "Too low"
If the guess matches:
'''

secret_number = 7

n = int(input("Enter the number : "))

if n > secret_number:
    print("Too High")
elif n < secret_number:
    print("Too Low")
else:
    print("Correct!")