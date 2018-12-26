"""
Source code given in the third section of the blog article (Iterating over built-in types)

URL: http://www.pythontraininghq.com
Author: Waqas Younas <waqas@pythontraininghq.com>
"""

file_name = "somefile.txt"
some_int = 10
try:
    iterator = iter(some_int) # throws exception
except TypeError as type_error:
    print(type_error)

data = [1, 2, 3]
for item in data:
    print(item)


iterator = iter(data)

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
try:
    print(iterator.__next__()) # throws exception
except StopIteration as stop_iteration:
    print("Iterator ran out of items")

# Now demonstrating the concept of multiple scans supported by an iterator

list_one = [1, 2, 3]
list_two = [4, 5, 6]
zipped = zip(list_one, list_two)

for item_one, item_two in zipped:
    print(item_one, item_two)

print("Iterating again")

for item_one, item_two in zipped:
    print(item_one, item_two)


some_file = open(file_name)
for line in some_file:
    print(line)

# Going to try to print the file content again
for line in some_file:
    print(line)



