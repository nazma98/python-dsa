# if-else example to find the largest number among three numbers

num1 =  53

num2 = 324

num3 = 54


largest_num = num1

if num2>largest_num:
    largest_num = num2
    
if num3>largest_num:
    largest_num = num3

print(f"The largest number is {largest_num}")
        

# nested if-else to find the largest number

if num1>num2:
    if num1>num3:
        largest_num = num1
    else:
        largest_num = num3
else:
    if num2>num3:
        largest_num= num2
    else:
        largest_num = num3

        
print(f"The largest number is {largest_num}")


