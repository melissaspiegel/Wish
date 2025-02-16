class Node:
    def __init__(self, data):
        self.data = data  # Stores the value
        self.next = None  # Pointer to next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize empty list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("None")

# Example Usage
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()  # Output: 10 → 20 → 30 → None