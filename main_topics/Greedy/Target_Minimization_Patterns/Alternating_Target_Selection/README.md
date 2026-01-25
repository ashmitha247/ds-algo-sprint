# Alternating Target Selection

## Concept
Alternating Target Selection involves switching between different target values based on position, parity, or state. This pattern is optimal when:
- Elements at different positions should converge to different targets
- The solution requires creating an alternating pattern
- Minimizing cost involves position-dependent choices

## Key Scenarios

### 1. Even-Odd Index Patterns
Elements at even indices target one value, odd indices target another.

### 2. Binary Alternation
Creating patterns like `[a, b, a, b, a, b, ...]` or `[0, 1, 0, 1, ...]`

### 3. Position-Based Optimization
Target depends on the element's position in sorted or original order

## Algorithm Pattern
```python
def alternating_target(arr):
    cost1 = 0  # Cost for pattern starting with target A
    cost2 = 0  # Cost for pattern starting with target B
    
    for i in range(len(arr)):
        if i % 2 == 0:
            cost1 += cost_to_change(arr[i], target_A)
            cost2 += cost_to_change(arr[i], target_B)
        else:
            cost1 += cost_to_change(arr[i], target_B)
            cost2 += cost_to_change(arr[i], target_A)
    
    return min(cost1, cost2)
```

## Time Complexity
**O(n)** - single pass through the array

## Space Complexity
**O(1)** - only tracking costs

## Common Problems

### Binary String Alternation
Make binary string alternating with minimum flips
```
Input: "110101"
Pattern 1: "101010" (2 changes)
Pattern 2: "010101" (4 changes)
Answer: 2
```

### Chess-like Coloring
Color a grid/array in alternating pattern
- Minimize repaints/changes
- Two possible patterns to consider

### Parity-Based Transformation
Transform array so even/odd indices follow different rules

## Example
```
Array: [1, 2, 3, 4, 5, 6]
Target: Even indices → 1, Odd indices → 2

Position:  0  1  2  3  4  5
Current:   1  2  3  4  5  6
Target:    1  2  1  2  1  2
Changes:   0  0  1  1  1  1  → 4 operations
```

## Key Insights
1. **Try Both Patterns**: Always check both alternating options
2. **Greedy Choice**: Local decision at each position
3. **No Dependencies**: Each position independently contributes to cost
4. **Optimal Substructure**: Total cost = sum of individual costs

## Variations
- **Multi-valued Alternation**: More than 2 target values
- **Cycle Length > 2**: Patterns like `[a, b, c, a, b, c, ...]`
- **Weighted Costs**: Different costs for different transformations
- **Constraint-based**: Some positions cannot be changed

## Related Problems
- LeetCode 1758: Minimum Changes to Make Alternating Binary String
- LeetCode 2166: Design Bitset
- Grid coloring problems
- Pattern matching with minimum edits
