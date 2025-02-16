class Node:
    def __init__(self, data):
        self.data = data
    #  ✅ This special method (__repr__) defines how an object is represented when printed or inspected in a debugger.
    def __repr__(self):
        return f"<Node data: {self.data}>"

node = Node(10)
print(node)


class LinkedList:
    """
    Singly Linked List
    """
    head = None

    def __init__(self):
        self.head = None
        # new list always empty
    
    def is_empty(self):
        return self.head == None
    
