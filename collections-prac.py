from collections import Counter, namedtuple
a = "aaaabbbccc"
my_counter = Counter(a)
print(my_counter.keys())
print(my_counter.values())
print(my_counter)
print(list(my_counter.elements()))