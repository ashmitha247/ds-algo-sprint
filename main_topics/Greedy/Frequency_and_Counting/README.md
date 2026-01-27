# Frequency and Counting Patterns

## Overview
Frequency and Counting patterns involve tracking how often elements appear in a dataset to verify conditions, find duplicates, or validate mathematical properties. These problems are usually solved using Hash Maps (Dictionaries in Python) or Frequency Arrays.

## Core Concept
Unlike Greedy algorithms (which make choices), these patterns rely on **data aggregation**:
1.  **Traverse** the data once (O(N)).
2.  **Count** the occurrences of every element.
3.  **Verify** a specific condition based on those counts.

## Common Scenarios
* **Majority Element:** Finding an element that appears more than N/2 times.
* **Equilibrium/Balance:** Checking if a specific element's count equals the sum of all others (e.g., *Little Authors*).
* **Anagrams:** Checking if two strings have the exact same character counts.
* **Uniqueness:** Finding the first unique character or removing duplicates.

## Pattern Categories

### 1. Equilibrium Counting (The "Half" Rule)
* **Focus:** Checking if a specific element constitutes exactly half of the total dataset.
* **Mathematical Trick:** Instead of `Count(A) == Sum(Others)`, we check `Count(A) == Total_Length / 2`.
* **Example:** "Little Authors" problem.

### 2. Hash Map Lookup
* **Focus:** Storing counts to answer "How many times did X appear?" instantly.
* **Strategy:** Use a Dictionary `{Key: Count}` for O(1) lookups.

### 3. Difference Arrays
* **Focus:** manipulating counts over ranges or comparing two datasets by subtracting frequencies.
