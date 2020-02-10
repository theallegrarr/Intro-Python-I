"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
slice_item = slice(1, 2, 1)
print(a[slice_item])

# Output the second-to-last element: 9
slice_item = slice(4, 5, 1)
print(a[slice_item])

# Output the last three elements in the array: [7, 9, 6]
slice_item = slice(3, 6, 1)
print(a[slice_item])

# Output the two middle elements in the array: [1, 7]
slice_item = slice(2, 4, 1)
print(a[slice_item])

# Output every element except the first one: [4, 1, 7, 9, 6]
slice_item = slice(1, 6, 1)
print(a[slice_item])

# Output every element except the last one: [2, 4, 1, 7, 9]
slice_item = slice(0, 5, 1)
print(a[slice_item])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
slice_item = slice(7, 12, 1)
print(s[slice_item])