from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()  # pronounced “deck”, which stands for double-ended queue.

    def is_empty(self):
        return not self.items  # Pythonic

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push('Test')
    print(s)
    s.push(1)
    s.push(False)
    print(s)
    print(s.size())
    s.pop()
    print(s)
