#Take a decimal number as input: 45.78 and output its integer part : 45 fractional part : .78

num = float(input("Enter the numbers with 2 decimal value : "));

integer_num = int(num);
fractional_num = num - integer_num;

print("\nAfter calculation");
print("\ninteger number =", integer_num);
print("\nfractional number =", f"{fractional_num:.2f}"[1:], "\n");