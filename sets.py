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

# newSet.clear()
# print(newSet)

for i in newSet:
    print(i)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8 ,9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

symDiff = setA.symmetric_difference(setB)
print(symDiff)

setA.update(setB)
print(setA)

setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}

print(setD.issubset(setC))