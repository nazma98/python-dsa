# if-else example to find the largest number among three numbers

num1 = input("Enter the first number:")

num2 = input("Enter the second number:")

num3 = input("Enter the third number:")


largest_num = num1

if num2>largest_num:
    largest_num = num2
    
if num3>largest_num:
    largest_num = num3

print(f"The largest number is {largest_num}")
        
