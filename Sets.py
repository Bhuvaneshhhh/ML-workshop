numbers = {1, 2, 3, 4, 5}
numbers.add(8)
numbers.remove(2)
evens= {2, 4, 6, 8}
union = numbers | evens
intersection = numbers & evens
difference = numbers - evens
print(intersection)
print(difference)
print(union)
