#1
def create_array(x, y, z, value):

    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]


x = int(input("Enter number of layers: "))  
y = int(input("Enter number of rows: "))    
z = int(input("Enter number of columns: ")) 
value = int(input("Enter the value to print in array: "))  


array = create_array(x, y, z, value)


for i in range(len(array)):
    print(f"Layer {i}:")
    for row in array[i]:
        print(row)
    print()
#2
def sum_avg(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5
    return total, average


marks = [85, 90, 78, 88, 92]
total, avg = sum_avg(*marks)

print("Total Marks:", total)
print("Average Marks:", avg)

#3

import string


def ispangram(sentence):
    alphaset = set(string.ascii_lowercase)  
    return set(sentence.lower()) >= alphaset  
test1 = "The quick brown fox jumps over the lazy dog"
test2 = "Crazy Fredrick bought many very exquisite opal jewels"
test3 = "Hello, this is not a pangram"

print(ispangram(test1))  
print(ispangram(test2))  
print(ispangram(test3))  

#4


def generate_tuples(end_value):
    return [(x, str(x)) for x in range(1, end_value + 1)]

end_value = 10  
result = generate_tuples(end_value)
print(result)


#5


def ispalindrome(s):
    cleaned_s = "".join(s.lower().split()) 
    return cleaned_s == cleaned_s[::-1]  
print(ispalindrome("racecar"))  
print(ispalindrome("A man a plan a canal Panama"))  
print(ispalindrome("Hello"))  
print(ispalindrome("Madam In Eden Im Adam"))
