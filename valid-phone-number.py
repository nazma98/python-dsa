import re

def is_valid_phone_number(phone_number):
    pattern = r'^(\+8801\d{9}|8801\d{9}|01\d{9})$'

    if re.fullmatch(pattern, phone_number):
        return True
    return False