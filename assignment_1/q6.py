#Swap two number after user entered.

num1 = int(input("Enter number 1: "));
num2 = int(input("Enter number 2: "));

temp = num1;
num1 = num2;
num2 = temp;

print('---After Swaping---');
print("Number 1:", num1);
print("Number 2:", num2);