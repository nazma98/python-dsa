# Enumerations or Enums is a set of symbolic names bound to unique values.


from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    MONSOON = 3
    WINTER = 4

print(Season.SPRING)  # Season.SPRING

print(Season.SPRING.value) # 1

print(Season.WINTER.value) # 4

print(Season.SPRING.name) # SPRING


print(type(Season.SPRING)) # <enum 'Season'>
