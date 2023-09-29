class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0  # Initialize length to 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1  # Increment the length by 1

    def __str__(self):
        values = []
        current_node = self.head
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        return ' -> '.join(values)

    def __contains__(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self.length += 1  # Increment the length by 1

    def delete(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            if not self.head:  # If the list became empty after deletion
                self.tail = None
            self.length -= 1  # Decrement the length by 1
            return

        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                if not current_node.next:  # If we deleted the last node
                    self.tail = current_node
                self.length -= 1  # Decrement the length by 1
                return
            current_node = current_node.next

    def __len__(self):  # Magic method to support len()
        return self.length


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.prepend(3)
    print(ll)
    print(5 in ll)  # True
    print(8 in ll)  # False
    ll.delete(5)
    print(ll)
