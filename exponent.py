print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for num in range(pow_num):
        result *= base_num
    return result
    
print(raise_to_power(2, 4))