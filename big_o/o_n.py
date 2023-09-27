# O(n) - Linear Time
def find_element(lst, target):
    for item in lst:
        if item == target:
            return True
    return False


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find_element(lst, 1)  # best case
find_element(lst, 5)  # average case
find_element(lst, 10)  # worst case - Ο (Omicron, not the letter O) . This is Big O
