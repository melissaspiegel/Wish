# Python Methods Cheat Sheet

## 🔥 String Methods
| Method | Description | Example |
|--------|------------|---------|
| `s.lower()` | Converts to lowercase | `"HELLO".lower()` → `"hello"` |
| `s.upper()` | Converts to uppercase | `"hello".upper()` → `"HELLO"` |
| `s.strip()` | Removes spaces from both ends | `" hello ".strip()` → `"hello"` |
| `s.replace(a, b)` | Replaces `a` with `b` | `"hello".replace("h", "y")` → `"yello"` |
| `s.split()` | Splits a string into a list | `"a,b,c".split(",")` → `["a", "b", "c"]` |
| `s.join(iterable)` | Joins list into a string | `",".join(["a", "b", "c"])` → `"a,b,c"` |
| `s.startswith(x)` | Checks if string starts with `x` | `"hello".startswith("h")` → `True` |
| `s.endswith(x)` | Checks if string ends with `x` | `"hello".endswith("o")` → `True` |
| `s[::-1]` | Reverses a string | `"hello"[::-1]` → `"olleh"` |

## 🔥 List Methods
| Method | Description | Example |
|--------|------------|---------|
| `len(lst)` | Returns length of list | `len([1,2,3])` → `3` |
| `lst.append(x)` | Adds `x` to the end | `[1,2].append(3)` → `[1,2,3]` |
| `lst.extend(lst2)` | Merges two lists | `[1,2].extend([3,4])` → `[1,2,3,4]` |
| `lst.insert(i, x)` | Inserts `x` at index `i` | `[1,2].insert(1, 5)` → `[1,5,2]` |
| `lst.pop()` | Removes last element | `[1,2,3].pop()` → `3` |
| `lst.remove(x)` | Removes first occurrence of `x` | `[1,2,3].remove(2)` → `[1,3]` |
| `lst.sort()` | Sorts the list | `[3,1,2].sort()` → `[1,2,3]` |
| `lst.reverse()` | Reverses the list | `[1,2,3].reverse()` → `[3,2,1]` |

## 🔥 Dictionary Methods
| Method | Description | Example |
|--------|------------|---------|
| `d.keys()` | Returns all keys | `{"a":1, "b":2}.keys()` → `dict_keys(["a", "b"])` |
| `d.values()` | Returns all values | `{"a":1, "b":2}.values()` → `dict_values([1,2])` |
| `d.items()` | Returns key-value pairs | `{"a":1, "b":2}.items()` → `[("a",1), ("b",2)]` |
| `d.get(x, default)` | Returns value of `x`, else `default` | `{"a":1}.get("b", 0)` → `0` |
| `d.pop(x)` | Removes key `x` | `d = {"a":1, "b":2}; d.pop("a")` → `{"b":2}` |
| `d.update(d2)` | Merges dictionaries | `d.update({"c":3})` |

## 🔥 Set Methods
| Method | Description | Example |
|--------|------------|---------|
| `set.add(x)` | Adds `x` to the set | `{1,2}.add(3)` → `{1,2,3}` |
| `set.remove(x)` | Removes `x` | `{1,2,3}.remove(2)` → `{1,3}` |
| `set.union(set2)` | Combines sets | `{1,2}.union({3,4})` → `{1,2,3,4}` |
| `set.intersection(set2)` | Common elements | `{1,2,3}.intersection({2,3,4})` → `{2,3}` |
| `set.difference(set2)` | Unique to `set1` | `{1,2,3}.difference({2,3,4})` → `{1}` |

## 🔥 Math Methods
| Method | Description | Example |
|--------|------------|---------|
| `abs(x)` | Absolute value | `abs(-5)` → `5` |
| `max(iterable)` | Max value | `max([1,2,3])` → `3` |
| `min(iterable)` | Min value | `min([1,2,3])` → `1` |
| `sum(iterable)` | Sum of values | `sum([1,2,3])` → `6` |
| `round(x, n)` | Rounds to `n` decimals | `round(3.14159, 2)` → `3.14` |
| `pow(x, y)` | Exponentiation | `pow(2, 3)` → `8` |

## 🔥 Interview Cheat Sheet
### **1. Reverse a String**
```python
def reverse(s):
    return s[::-1]
```

### **2. Check If a Number is Prime**
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### **3. Find Duplicates in a List**
```python
def find_duplicates(lst):
    return set([x for x in lst if lst.count(x) > 1])
```

### **4. Find the Most Frequent Element**
```python
from collections import Counter

def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]
```

---

## **🔥 Final Tip**
🚀 If you forget a method, use:
```python
help(str)  # Shows all string methods
help(list) # Shows all list methods
```

