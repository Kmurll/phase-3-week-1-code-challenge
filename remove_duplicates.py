def remove_duplicates(sequence):
    seen = set()  # Create an empty set to keep track of seen elements
    result = []   # Initialize an empty list to store the unique elements in order
    
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Test case 1
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

# Test case 2
input_sequence1 = [1, 2, 3, 4, 5]
result1 = remove_duplicates(input_sequence1)
print(result1)  # Output: [1, 2, 3, 4, 5] (no duplicates)

# Test case 3
input_sequence2 = [1, 1, 1, 1, 1]
result2 = remove_duplicates(input_sequence2)
print(result2)  # Output: [1] (all elements are duplicates)

# Test case 4
input_sequence3 = ['apple', 'banana', 'cherry', 'apple', 'date', 'banana']
result3 = remove_duplicates(input_sequence3)
print(result3)  # Output: ['apple', 'banana', 'cherry', 'date'] (removing string duplicates)

# Test case 5
input_sequence5 = [(1, 2), (2, 3), (1, 2), (4, 5), (2, 3)]
result5 = remove_duplicates(input_sequence5)
print(result5)  # Output: [(1, 2), (2, 3), (4, 5)] (removing tuple duplicates)
