class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # New pointer for backward traversal

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp  # Link backward

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ↔ ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ↔ ")
            temp = temp.prev
        print("None")

# Example Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display_forward()  # Output: 10 ↔ 20 ↔ 30 ↔ None
dll.display_backward() # Output: 30 ↔ 20 ↔ 10 ↔ None