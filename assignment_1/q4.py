# Type Casing a string "45" to int, float, string agin and print along with the type.

number = input("Enter the number :");

num_type = int(number);
float_type = float(number);
str_type = str(number);


print(type(num_type), ":", num_type)
print(type(float_type), ":", float_type)
print(type(str_type), ":", str_type)