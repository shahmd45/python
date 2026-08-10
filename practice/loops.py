# print 1 to 5 number
'''
i = 1
while i <= 5:
    print(i);
    i += 1
'''


# using for loop
'''
for i in range(1, 6):
    print(i);
'''

# count the no of i in the string;

'''
string = str(input("Enter the string : "))
count = 0

for ch in string:
    if ch == 'i':
        count += 1

print("Number of i = ", count)
'''

# count the number of vowels

'''
string = str(input("Enter the string : "))

count = 0

for ch in string:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1

print("Number of vowel is = ", count);
'''

# write the multiple of 6

n = int(input("Enter the number : "))
i = 1

print("\n")
while i <= 10:
    print(n, "*", i, "=", n * i )
    i += 1

print("\n")