# Majority-Target (Base Case)

## Concept
The Majority-Target pattern uses the most frequent element (or mode) as the target value to minimize the number of operations needed to transform all elements.

## Key Principle
When transforming all elements to be equal, choosing the most frequent element minimizes operations because:
- Fewer elements need to be changed
- The majority already satisfies the target condition

## Algorithm Pattern
```
1. Find the most frequent element (majority/mode)
2. Count elements that differ from this target
3. The count represents minimum operations needed
```

## Time Complexity
- **O(n)** with hash map counting
- **O(n log n)** with sorting approach

## Space Complexity
- **O(n)** for hash map
- **O(1)** additional space with sorting (if allowed to modify)

## Common Problems
- Make all elements equal with minimum operations
- Minimum deletions to make frequency equal
- Array transformation with replacement cost

## Example
```
Array: [1, 2, 2, 2, 3]
Majority: 2 (appears 3 times)
Operations needed: 2 (change 1 and 3 to 2)
```

## Related Techniques
- **Complementary Counting**: Alternative counting method
- **Frequency Analysis**: Finding mode efficiently
- **Hash Map**: For O(n) frequency tracking

## Variations
- Weighted operations (different costs for different changes)
- Multiple valid targets (choose optimal among ties)
- Constraints on transformation rules
