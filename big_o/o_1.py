def peek(p: list):
    return p[-1]


peek([1, 2, 3, 4])
peek([1])
peek([1, 2, 3])
peek([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# - No matter how big the list is, it always takes
#   a single operation to fetch the first item.
#
# - The runtime doesn't change as
#   the size of the list increases.
