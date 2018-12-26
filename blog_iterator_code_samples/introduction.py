"""Source code given in the first section of the article"""
file_name = 'somefile.txt'
items = [1, 2, 3]
for item in items:
    print(item)
one, two, three = items
print(one, two, three)
print(3 in items)
print([item for item in items]) # list comprehensions are concise way to create lists
# map(function, iterable) applies the function to every item in iterable
iterator =  map(str.lower, open(file_name))
# file object syntax is made possible because of iteration support
for line in open(file_name):
    print(line)
