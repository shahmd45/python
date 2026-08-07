# Take 2 number as int type as input and one value as float type, convert 2 int type to float and calculate the avg of 3 values.

num_1 = int(input("Enter number 1: "));
num_2 = int(input("Enter number 2: "));
num_3 = float(input("Enter number 3: "));

num_1 = float(num_1);
num_2 = float(num_2);

avg = (num_1 + num_2 + num_3) / 3;


print("Average of 3 number is ", avg);