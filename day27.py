# Day 27: Tuple methods and operations

nums = (1, 2, 2, 3, 2)
print("Count of 2:", nums.count(2))

values = (10, 90, 30, 20)
print("Index of 20:", values.index(20, 1, 4))

first = (1, 2)
second = (3, 4)
combined = first + second
print("Combined:", combined)
print("First tuple:", first)
print("Second tuple:", second)

# Convert a tuple to a list to modify an item, then convert it back.
editable = (1, 2, 3)
temporary = list(editable)
temporary[1] = 100
editable = tuple(temporary)
print("Modified tuple:", editable)
print("Length:", len(editable))
