def find_largest_smallest(num1, num2, num3):
    largest = max(num1, num2, num3)
    smallest = min(num1, num2, num3)
    return largest, smallest

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest, smallest = find_largest_smallest(num1, num2, num3)

print("Largest value:", largest)
print("Smallest value:", smallest)