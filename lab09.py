# 1
def fun(): return "This is fun"
def disp(): return "This is disp"
def msg(): return "This is msg"
funcs = [fun, disp, msg]
for f in funcs:
    print(f())

# 2
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
added = list(map(lambda x, y: x + y, lst1, lst2))
print("Added List:", added)

# 3
rand_nums = [random.randint(-15, 15) for _ in range(10)]
squared = list(map(lambda x: x * x, rand_nums))
print("Random Numbers:", rand_nums)
print("Squared Numbers:", squared)

# 4
lst = ["madam", "Python", "malayalam", "12321"]
palindromes = list(filter(lambda s: str(s) == str(s)[::-1], lst))
print("Palindromes:", palindromes)

# 5
faculty = ["Dr. Avinash", "Prof. Megha", "Dr. Kiran Desai", "Mr. Raj", "Dr. Hemangini Patel"]
long_names = list(filter(lambda name: len(name) > 8, faculty))
print("Names longer than 8 characters:", long_names)
