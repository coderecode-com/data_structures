import stack

input_str = "!reerac a t'nsi soahc esuaceB :serutcurts ataD"
output_str = ""
s = stack.Stack()


# `for` when you know how many iterations
for c in input_str:
    s.push(c)

# `when` you don't know how many iterations
while not s.is_empty():
    output_str += s.pop()

print(output_str)
