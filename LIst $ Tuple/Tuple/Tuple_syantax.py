tuple = (1, 2, 3, 4, 5)
print("Tuple Output:", tuple)
print("length of tuple:", len(tuple))

# Print type of tuple
print("Type:", type(tuple))

# index accses of tuple

print("Print index output:", tuple[0])

# Tuple slicing
print("Slicing:", tuple[1:3])

# Tuple methods

# 1) tup.index method (Returns index of first occurrence)
print("This element find in index number:", tuple.index(1))  # syantax tuple.index(1)

# 2) tup.count method counts total occurrences
print(tuple[0], "this element only", tuple.count(1), "time present in a tuple")
