set1 = {1, 2, 3, 2, 1};
print(set1)

myset = set("Hello")
print(myset)

newSet = set()
print(type(newSet))

newSet.add(1)
newSet.add(2)
newSet.add(3)
print(newSet)

newSet.remove(3)
print(newSet)

newSet.discard(4)
print(newSet)

newSet.clear()
print(newSet)