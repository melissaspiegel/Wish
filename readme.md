# Python Data Structures & Algorithms

This repository contains Python implementations of various **data structures** and **algorithms**, including **searching techniques, linked lists, and space complexity analysis**.

## 📂 Directory Structure

| File                        | Description |
|-----------------------------|-------------|
| `arrays.py`                 | Array operations and manipulations |
| `binary_search.py`          | Binary search algorithm |
| `doubly_linked_list.py`     | Doubly Linked List implementation |
| `hacker.py`                 | Miscellaneous hacker-rank challenges |
| `leap_year.py`              | Leap year validation logic |
| `linear_search.py`          | Linear search implementation |
| `linear_search_enumerate.py`| Optimized linear search using enumerate() |
| `linked_list.py`            | Generic linked list implementation |
| `recursive_binary_search.py`| Recursive binary search |
| `singly_linked_list.py`     | Singly Linked List implementation |
| `space_complexity.py`       | Space complexity analysis of operations |

---

## **1. Arrays (`arrays.py`)**
### **Example: Creating and Manipulating Arrays**
```python
arr = [10, 20, 30, 40, 50]

# Accessing elements
print(arr[2])  # Output: 30

# Adding elements
arr.append(60)

# Removing elements
arr.remove(20)

# Iterating through an array
for num in arr:
    print(num)
```
📌 **Arrays provide O(1) access time but require shifting elements for insertions/deletions (O(n)).**

---

## **2. Binary Search (`binary_search.py`)**
### **Example: Searching for an Element in a Sorted List**
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))  # Output: 3
```
📌 **Binary search reduces time complexity to O(log n), making it much faster than linear search for large datasets.**

---

## **3. Doubly Linked List (`doubly_linked_list.py`)**
### **Example: Doubly Linked List Implementation**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
```
📌 **Doubly Linked Lists allow traversal in both directions but use extra space for the `prev` pointer.**

---

## **4. Leap Year Check (`leap_year.py`)**
### **Example: Checking if a Year is a Leap Year**
```python
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap(2024))  # Output: True
print(is_leap(2100))  # Output: False
```
📌 **A leap year occurs every 4 years unless divisible by 100, but always if divisible by 400.**

---

## **5. Linear Search (`linear_search.py`)**
### **Example: Finding an Element in an Unsorted List**
```python
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

arr = [4, 2, 7, 1, 9]
print(linear_search(arr, 7))  # Output: 2
```
📌 **Linear search runs in O(n) time, making it inefficient for large datasets compared to binary search.**

---

## **6. Space Complexity Analysis (`space_complexity.py`)**
### **Example: Analyzing Memory Usage**
```python
import sys

a = []
b = [1, 2, 3, 4, 5]

print(sys.getsizeof(a))  # Output: Size of empty list
print(sys.getsizeof(b))  # Output: Size of list with 5 elements
```
📌 **Understanding space complexity helps optimize memory usage in large-scale applications.**

---

## 🚀 **Final Thoughts**
This repository covers **fundamental algorithms** and **data structures**, helping in both **coding interviews** and **real-world applications**.  

📌 **For contributions or improvements, feel free to submit a pull request!**
