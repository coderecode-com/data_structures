"""
- Array need traversing of the entire array
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# for when you know how many iterations
for c in string:
    s.push(c)

# When you dont know how many iterations
while not s.is_empty():
    reversed_string += s.pop()
print(reversed_string)
