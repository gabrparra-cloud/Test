

from functools import reduce


prev = 0
next = 1

for i in range(0, 50):
    print(f"Iteration {i}: {prev}")
    temp = prev + next
    prev = next
    next = temp

numbers = [1,2,3,4,5]

def multiply_by_two(x):
    return x * 2 

print(list(map(multiply_by_two, numbers)))
print(list(map(lambda x: x * 2, numbers)))

print(reduce(lambda x, y: x + y, numbers))

f = open("test.txt", "r+")
print(f.read())
f.close()

json_data = open("test.json", "w+")

import re

my_string = "Hello, my name is John Doe. I am 30 years old and I live in New York City."
my_another_string = "My email address is"

match = re.match("Hello", my_string,re.I)
#match = re.match("Hello", my_another_string)

print(match)
print(match.span)

import numpy 
