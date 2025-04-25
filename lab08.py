# 1
words = ["apple", "banana", "grape", "kiwi", "orange"]
uppercase_set = {word.upper() for word in words}
print("Uppercase Set:", uppercase_set)

# 2
random_numbers = {random.randint(15, 45) for _ in range(10)}
print("Original Set:", random_numbers)
count_below_30 = sum(1 for num in random_numbers if num < 30)
print("Count of numbers < 30:", count_below_30)
greater_than_35 = {num for num in random_numbers if num > 35}
print("Numbers > 35:", greater_than_35)

# 3
names = set()
names.update(["Alice", "Bob", "Charlie", "David", "Eve"])
print("After adding names:", names)
if "Alice" in names:
    names.remove("Alice")
    names.add("Alicia")
print("After modifying name:", names)
names.discard("Bob")
names.discard("Charlie")
print("After deleting 2 names:", names)

# 4
name_set = {"Alice", "Arnold", "Brian", "Bella", "Cathy", "Aaron", "Ben"}
a_names = {name for name in name_set if name.startswith("A")}
b_names = {name for name in name_set if name.startswith("B")}
print("Names starting with A:", a_names)
print("Names starting with B:", b_names)
