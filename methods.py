def reverse_string(s):
    return ''.join(reversed(s))

# Test cases
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("Python"))  # Output: "nohtyP"


######################


def is_even(n):
    if n % 2 == 0:  # The modulo operator (%) checks if there's a remainder when dividing by 2
        return True  # If remainder is 0, it's even
    else:
        return False  # Otherwise, it's odd

# Test cases
print(is_even(4))  # True
print(is_even(7))  # False
print(is_even(0))  # True

######################


def reverse_string(s):
    return s[::-1]  # This slices the string from end to start

# Test cases
print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("Python"))  # Output: "nohtyP"
print(reverse_string("racecar"))  # Output: "racecar"

######################
