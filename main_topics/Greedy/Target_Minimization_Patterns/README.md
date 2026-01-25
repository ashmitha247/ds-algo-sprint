# Target Minimization Patterns

## Overview
Target minimization patterns focus on greedy strategies to minimize costs, distances, or differences when selecting or transforming elements to meet a target condition.

## Core Concept
These patterns typically involve:
- Identifying an optimal target value
- Minimizing the total cost/distance to reach that target
- Using greedy selection to determine the best order of operations

## Common Scenarios
1. **Array Transformation**: Making all elements equal with minimum operations
2. **Cost Minimization**: Selecting elements to minimize total cost
3. **Distance Optimization**: Minimizing total distance to a central point
4. **Balancing**: Redistributing values to achieve balance

## Pattern Categories

### 1. Majority-Target (Base Case)
- Uses the most frequent element as the target
- Minimizes operations by leveraging existing majority
- Includes complementary counting techniques

### 2. Alternating Target Selection
- Switches between different target values
- Useful for optimization problems with multiple states
- Often involves even/odd index patterns

### 3. Median Distance Optimization
- Uses median as the optimal target point
- Minimizes sum of absolute distances
- Mathematical foundation in statistical median properties

## Key Insights
- Choice of target significantly impacts the solution
- Sorting often reveals the optimal target
- Mathematical properties (median, mode) guide target selection
