## O(n^2) - Quadratic Time

def has_duplicates(p: list):
    counter = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            counter += 1
            if p[i] == p[j]:
                return True
    print(f"Execution count: {counter}")
    return False


# Test the function
lst = [1, 2]
has_duplicates(lst)

lst = [1, 2, 3]
has_duplicates(lst)

lst = [1, 2, 3, 4]
has_duplicates(lst)

lst = [1, 2, 3, 4, 5]
has_duplicates(lst)

lst = [1, 2, 3, 4, 5, 6]
has_duplicates(lst)


lst = [1, 2, 3, 4, 5, 6, 7]
has_duplicates(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8]
has_duplicates(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
has_duplicates(lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
has_duplicates(lst)
