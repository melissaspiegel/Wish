def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])  # Trim, split, reverse, and join

# Test case
s = "  Hello   World!  "
print(reverse_words(s))  # Output: "World! Hello"