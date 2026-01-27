# Target Maximization Patterns

## Overview

Target maximization patterns focus on greedy strategies to maximize scores, distances, or profits by making the locally optimal "best" choice at every step.

## Core Concept

These patterns typically involve:
* **Greedy Choice Property:** Making the choice that offers the immediate highest gain or distance.
* **Tie-Breaking:** Using secondary criteria (like lexicographical order) when multiple choices offer the same gain.
* **Constructive Logic:** Building a solution piece-by-piece rather than transforming an existing array.

## Common Scenarios

* **String/Sequence Construction:** Building a new sequence to maximize Hamming distance or dissimilarity.
* **Profit/Score Accumulation:** Picking elements to get the highest total value.
* **Activity Selection:** Maximizing the number of non-overlapping tasks or intervals.

## Pattern Categories

### 1. Complementary Construction (Base Case)
* **Focus:** Maximizing difference or distance from reference inputs.
* **Strategy:** Check the input values and choose the "opposite" or "complement" to gain points.
* **Example:** "Balls for Challenge" (If input is 'B', choose 'W').
* **Key Logic:** `IF (Input == X) THEN Output = NOT X`.

### 2. Lexicographical Maximization
* **Focus:** Maximizing a primary value while minimizing/maximizing the "dictionary order" as a secondary goal.
* **Strategy:** If two options yield the same maximum score, pick the character/number that appears first alphabetically.
* **Key Logic:** `IF (Score(A) == Score(B)) THEN Pick min(A, B)`.

### 3. Priority Selection (Accumulative)
* **Focus:** Always picking the largest available resource or value.
* **Strategy:** Sorting inputs by value and picking from the top.
* **Example:** Fractional Knapsack or assigning cookies to children with greed factors.

## Key Insights

* **Independence:** In constructive maximization, the choice at index `i` often does not affect index `i+1`, allowing for a single pass (O(N)).
* **Tie-Breakers Matter:** In maximization problems, multiple "best" scores are common; the tie-breaking rule (e.g., "lexicographically smallest") often dictates the unique solution.
* **Divergence vs. Convergence:** Unlike minimization (which tries to meet in the middle), maximization often tries to push values to the extremes.
