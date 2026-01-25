# Median Distance Optimization

## Concept
The median minimizes the sum of absolute distances. This mathematical property makes it the optimal target point for minimization problems involving distances or movements.

## Mathematical Foundation

### Why Median?
For a set of points, the median minimizes:
$$\sum_{i=1}^{n} |x_i - target|$$

**Proof Intuition**: Moving the target away from the median increases distance to more than half the points while decreasing it for fewer than half.

## Key Properties
1. **Optimal for L1 Distance**: Minimizes sum of absolute differences
2. **Balanced Point**: Equal elements on both sides (for odd n)
3. **Any Point Between**: For even n, any point between the two middle elements works
4. **Robust to Outliers**: Unlike mean, not affected by extreme values

## Algorithm Pattern
```python
def median_distance_optimization(arr):
    # Sort the array
    arr.sort()
    
    # Find median
    n = len(arr)
    median = arr[n // 2]
    
    # Calculate total cost
    total_cost = sum(abs(x - median) for x in arr)
    
    return total_cost
```

## Time Complexity
**O(n log n)** - dominated by sorting

## Space Complexity
**O(1)** - if sorting in-place is allowed
**O(n)** - if creating a sorted copy

## Common Problems

### 1. Minimum Moves to Make Array Equal
Move all elements to the same value with minimum total moves.

### 2. Warehouse Location
Place a warehouse to minimize total distance to all customers.

### 3. Meeting Point Problem
Find a point where sum of distances from all points is minimized.

### 4. 2D Median (Manhattan Distance)
Find coordinates (x, y) that minimize total Manhattan distance.

## Examples

### Example 1: 1D Array
```
Array: [1, 3, 7, 9, 10]
Median: 7
Distances: |1-7| + |3-7| + |7-7| + |9-7| + |10-7|
         = 6 + 4 + 0 + 2 + 3 = 15
```

### Example 2: Even Length
```
Array: [1, 2, 3, 10]
Sorted: [1, 2, 3, 10]
Middle elements: 2 and 3
Any target in [2, 3] gives same result

Using target = 2:
Distances: 1 + 0 + 1 + 8 = 10

Using target = 3:
Distances: 2 + 1 + 0 + 7 = 10
```

## 2D Extension (Manhattan Distance)
For 2D points, find median of x-coordinates and y-coordinates independently:
```python
def median_2d(points):
    x_coords = sorted([p[0] for p in points])
    y_coords = sorted([p[1] for p in points])
    
    median_x = x_coords[len(x_coords) // 2]
    median_y = y_coords[len(y_coords) // 2]
    
    return (median_x, median_y)
```

## Variations

### Weighted Median
When elements have weights, find the point where cumulative weight is balanced:
```python
def weighted_median(values, weights):
    # Sort by values
    pairs = sorted(zip(values, weights))
    
    total_weight = sum(weights)
    cumulative = 0
    
    for value, weight in pairs:
        cumulative += weight
        if cumulative >= total_weight / 2:
            return value
```

### Constrained Target
Target must be from the original array or specific range:
```python
def constrained_median(arr):
    arr.sort()
    median = arr[len(arr) // 2]
    # Median is always from the array
    return median
```

## Comparison with Mean

| Property | Median | Mean |
|----------|--------|------|
| Minimizes | Sum of absolute distances | Sum of squared distances |
| Outlier Sensitivity | Robust | Sensitive |
| Computation | O(n log n) sort | O(n) sum |
| Use Case | L1/Manhattan distance | L2/Euclidean distance |

## Related Problems
- **LeetCode 462**: Minimum Moves to Equal Array Elements II
- **LeetCode 296**: Best Meeting Point
- **LeetCode 2448**: Minimum Cost to Make Array Equal
- Facility location problems
- Optimal gathering point problems

## Key Insights
1. **Always sort first** to find median efficiently
2. **For even length**, any point between middle two works
3. **Independent dimensions**: For multi-dimensional problems, solve each dimension separately (Manhattan distance)
4. **Greedy proof**: Moving target away from median always increases total distance
