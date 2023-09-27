def halve_until_one(n):
    steps = 0
    while n > 1:
        n /= 2
        steps += 1
    return steps

# Test the function
result = []
for i in range(1,100):
    result.append(halve_until_one(i))

print(result)
