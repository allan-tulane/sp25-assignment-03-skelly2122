import math
from collections import Counter

# Sample test pairs for string comparison
example_pairs = [
    ('book', 'back'),
    ('kookaburra', 'kookybird'),
    ('elephant', 'relevant'),
    ('AAAGAATTCA', 'AAATCA')
]

# Expected alignment results
expected_alignments = [
    ('b--ook', 'bac--k'),
    ('kook-ab-urr-a', 'kooky-bi-r-d-'),
    ('relev--ant', '-ele-phant'),
    ('AAAGAATTCA', 'AAA---T-CA')
]

# Basic recursive implementation of edit distance calculation
def calculate_edit_distance(str1, str2):
    # Base cases for empty strings
    if len(str1) == 0: 
        return len(str2)
    if len(str2) == 0: 
        return len(str1)
    
    # If first characters match, no operation needed
    if str1[0] == str2[0]:
        return calculate_edit_distance(str1[1:], str2[1:])
    
    # Try all operations (insert, delete) and take minimum
    return 1 + min(
        calculate_edit_distance(str1[1:], str2),    # Delete from str1
        calculate_edit_distance(str1, str2[1:])     # Insert into str1
    )

# Optimized version using memoization to avoid redundant calculations
def optimized_edit_distance(str1, str2, cache=None):
    # Initialize cache dictionary if not provided
    if cache is None:
        cache = {}
    
    # Create unique key for the current string pair
    pair_key = (str1, str2)
    
    # Return cached result if available
    if pair_key in cache:
        return cache[pair_key]
    
    # Handle base cases
    if len(str1) == 0:
        result = len(str2)
    elif len(str2) == 0:
        result = len(str1)
    # If first characters match, no operation needed
    elif str1[0] == str2[0]:
        result = optimized_edit_distance(str1[1:], str2[1:], cache)
    else:
        # Calculate costs for insertion and deletion
        insertion_cost = optimized_edit_distance(str1, str2[1:], cache)
        deletion_cost = optimized_edit_distance(str1[1:], str2, cache)
        
        # Take minimum cost and add 1 for the operation
        result = 1 + min(insertion_cost, deletion_cost)
    
    # Store result in cache before returning
    cache[pair_key] = result
    return result

# Function to reconstruct alignment based on dynamic programming table
def generate_alignment(str1, str2):
    # Build the complete memo table first
    memo_table = {}
    optimized_edit_distance(str1, str2, memo_table)
    
    # Start from the end of both strings
    pos1, pos2 = len(str1), len(str2)
    aligned_str1, aligned_str2 = [], []
    
    # Trace back through the memo table
    while pos1 > 0 or pos2 > 0:
        # Current prefixes
        prefix1, prefix2 = str1[:pos1], str2[:pos2]
        current_cost = memo_table.get((prefix1, prefix2), float('inf'))
        
        # Check for character match
        is_match = pos1 > 0 and pos2 > 0 and str1[pos1 - 1] == str2[pos2 - 1]
        
        # Check possible operations
        insertion = pos2 > 0 and memo_table.get((prefix1, str2[:pos2 - 1]), float('inf')) + 1 == current_cost
        deletion = pos1 > 0 and memo_table.get((str1[:pos1 - 1], prefix2), float('inf')) + 1 == current_cost
        
        # Apply the appropriate operation
        if is_match:
            # Match case - add characters from both strings
            aligned_str1.insert(0, str1[pos1 - 1])
            aligned_str2.insert(0, str2[pos2 - 1])
            pos1 -= 1
            pos2 -= 1
        elif insertion:
            # Insertion case - add gap in first string
            aligned_str1.insert(0, '-')
            aligned_str2.insert(0, str2[pos2 - 1])
            pos2 -= 1
        elif deletion:
            # Deletion case - add gap in second string
            aligned_str1.insert(0, str1[pos1 - 1])
            aligned_str2.insert(0, '-')
            pos1 -= 1
        else:
            # Fallback case for alignment consistency
            aligned_str1.insert(0, str1[pos1 - 1] if pos1 > 0 else '-')
            aligned_str2.insert(0, str2[pos2 - 1] if pos2 > 0 else '-')
            pos1 = max(pos1 - 1, 0)
            pos2 = max(pos2 - 1, 0)
    
    # Convert lists to strings
    return ''.join(aligned_str1), ''.join(aligned_str2)
