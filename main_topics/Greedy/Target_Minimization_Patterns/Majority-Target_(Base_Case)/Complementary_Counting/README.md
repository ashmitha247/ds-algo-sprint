# Complementary Counting

## Concept
Instead of counting elements equal to the target, count elements NOT equal to the target. This is particularly useful when:
- The majority is obvious
- Direct counting is more complex
- We need the minimum operations (which equals non-target elements)

## Key Formula
```
Minimum Operations = Total Elements - Maximum Frequency
```

## Why It Works
If we want to make all elements equal:
- Best target = most frequent element
- Operations needed = all other elements
- Complementary count = n - max_frequency

## Algorithm
```python
def min_operations(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    max_frequency = max(freq.values())
    return len(arr) - max_frequency
```

## Time Complexity
**O(n)** - single pass to count frequencies

## Space Complexity
**O(k)** where k is the number of unique elements

## Advantages
1. **Simpler Logic**: One subtraction instead of summing differences
2. **Direct Answer**: Immediately gives minimum operations
3. **No Target Tracking**: Don't need to identify the actual majority element
4. **Works with Ties**: If multiple elements have max frequency, any works

## Example
```
Array: [1, 1, 2, 2, 2, 3, 3]
Length: 7
Frequencies: {1: 2, 2: 3, 3: 2}
Max Frequency: 3

Complementary Count: 7 - 3 = 4 operations
(Change four elements to match the majority element 2)
```

## Common Applications
- **LeetCode 1551**: Minimum Operations to Make Array Equal
- **LeetCode 2870**: Minimum Number of Operations to Make Array Empty
- **Array Equalization Problems**
- **Deletion/Transformation Problems**

## Related Patterns
- Boyer-Moore Majority Vote Algorithm
- Frequency-based optimization
- Mode finding in statistics
