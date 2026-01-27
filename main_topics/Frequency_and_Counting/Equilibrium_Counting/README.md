# Equilibrium Counting

## Pattern Description
Equilibrium Counting problems check if a specific element's frequency equals a mathematical relationship with other elements (often "exactly half" of the total).

## The "Half Rule"
Instead of comparing `Count(A) == Sum(All Other Counts)`, we simplify to:
```
Count(A) == Total_Length / 2
```

This works because if A appears exactly as many times as all others combined, A must be exactly half of the total.

## Key Characteristics
* **Single Pass:** Traverse the data once to count frequencies
* **Mathematical Verification:** Check if counts satisfy a specific equation
* **O(N) Time, O(K) Space** where K = number of unique elements

## Example Problem: Little Authors
**Problem:** Check if character 'A' appears exactly as many times as all other characters combined.

**Approach:**
1. Count total characters in string (N)
2. Count occurrences of 'A' (count_A)
3. Check if `count_A == N / 2`

**Why it works:** If A appears X times and others appear X times total, then X + X = N, so X = N/2.

## Implementation Pattern
```python
def check_equilibrium(data, target):
    total = len(data)
    count_target = sum(1 for x in data if x == target)
    return count_target == total / 2
```
