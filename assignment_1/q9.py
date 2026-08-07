#Take user input for the Principle amout, rate and time for calculating simple interest.


principle = float(input("Enter the principle amout = "));
rate = float(input("Enter the interest rate = "));
time = float(input("Enter the time in years = "));


SI = (principle*rate*time) / 100;

print("Simple Interest is :", SI);