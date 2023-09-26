import stack

string = "!reerac a t'nsi soahc esuaceB :serutcurts ataD"
reversed_string = ""
s = stack.Stack()

# `for` when you know how many iterations
for c in string:
    s.push(c)

# `when` you don't know how many iterations
while not s.is_empty():
    reversed_string += s.pop()
print(reversed_string)
