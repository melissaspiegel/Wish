# Python Cheat Sheet

## 1. Loops
# For Loop
for i in range(n):
    print(i)

for item in my_list:
    print(item)

# While Loop
i = 0
while i < n:
    print(i)
    i += 1

## 2. List Comprehensions
squared = [x**2 for x in range(10)]
even_numbers = [x for x in my_list if x % 2 == 0]

## 3. Dictionary Iteration
my_dict = {'a': 1, 'b': 2}
for key, value in my_dict.items():
    print(key, value)

## 4. Sorting
arr = [3, 1, 4, 1, 5, 9]
arr.sort()  # Sort in place
sorted_arr = sorted(arr, reverse=True)

## 5. Finding Max/Min
max_val = max(my_list)
min_val = min(my_list)

## 6. String Operations
s = "hello world"
words = s.split()
s_upper = s.upper()
s_reversed = s[::-1]

## 7. List Operations
my_list.append(10)
my_list.pop()
my_list.remove(10)

## 8. Sets (Unique Elements)
my_set = set([1, 2, 3, 3, 2])
my_set.add(4)

## 9. Tuples (Immutable)
point = (3, 4)
x, y = point

## 10. Lambda (Anonymous Functions)
square = lambda x: x ** 2
sorted_list = sorted(my_list, key=lambda x: -x)

## 11. Using Heap for Priority Queue
import heapq
heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)
heapq.heappush(heap, 2)
min_val = heapq.heappop(heap)

## 12. Binary Search
import bisect
arr = [1, 3, 5, 7, 9]
pos = bisect.bisect_left(arr, 4)

## 13. Default Dictionary
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1

## 14. Counter (Counting Elements)
from collections import Counter
counts = Counter("hello")
print(counts['l'])

## 15. Recursion (Factorial Example)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

## 16. Two-Pointer Technique
arr = [1, 2, 3, 4, 5]
left, right = 0, len(arr) - 1
while left < right:
    print(arr[left], arr[right])
    left += 1
    right -= 1

## 17. Sliding Window (Sum of k elements)
def max_subarray_sum(arr, k):
    max_sum = cur_sum = sum(arr[:k])
    for i in range(k, len(arr)):
        cur_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, cur_sum)
    return max_sum

## 18. Depth-First Search (DFS)
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)

## 19. Breadth-First Search (BFS)
from collections import deque
def bfs(start):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.append(neighbor)

## 20. Graph Adjacency List Representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
