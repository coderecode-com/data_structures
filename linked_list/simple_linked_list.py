class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = None
        self.length = 1
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next


if __name__ == '__main__':
    ll = LinkedList(6)
    ll.append(7)
    ll.print()
