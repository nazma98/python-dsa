import re

def is_valid_phone_number(phone_number):
    pattern = r'^(\+8801\d{9}|8801\d{9}|01\d{9})$'

    if re.fullmatch(pattern, phone_number):
        return True
    return False

test_numbers = [
    "+8801671234567",  # Valid
    "8801671234567",   # Valid
    "01671234567",     # Valid
    "+880167123456",   # Invalid (only 8 digits)
    "1234567890",      # Invalid (no valid prefix)
    "+8801abcdefghi",  # Invalid (contains letters)
    "+8801976543210",  # Valid
    "01712345678",     # Valid
]

for number in test_numbers:
    result = is_valid_phone_number(number)
    print(result)