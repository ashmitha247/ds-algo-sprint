"""
Little Authors - Equilibrium Counting Problem

Problem Statement:
Given a string, determine if the character 'A' appears exactly as many times 
as all other characters combined.

Input:
- First line: Number of test cases T
- For each test case: A string S

Output:
- For each test case: "YES" if 'A' count equals other characters count, "NO" otherwise

Example:
Input:
3
AAB
ABAA
ABC

Output:
YES
NO
NO

Explanation:
- "AAB": A appears 2 times, others appear 1 time (B=1). 2 ≠ 1, but wait...
  Actually: A=2, total=3, so A should be 3/2=1.5, not possible. Let me reconsider.
  
Wait, if A appears as many times as ALL others combined:
- "AAB": A=2, others=1 (B), so 2 ≠ 1 -> NO
- Actually for "AAB": total=3, A=2. Check: A == total/2? 2 == 1.5? NO
  
Let me think about this differently:
If A appears X times and others appear X times, then total = 2X, so X = total/2

For "AAB": total=3, A=2. Is 2 == 3/2? No (since 3 is odd, this can't work)
For "AABB": total=4, A=2. Is 2 == 4/2 = 2? YES

So the pattern is: count(A) == len(string) / 2
"""

def solve():
    # Read number of test cases
    t = int(input())
    
    for _ in range(t):
        s = input().strip()
        
        # Count total characters
        total_chars = len(s)
        
        # Count occurrences of 'A'
        count_a = s.count('A')
        
        # Check equilibrium: A appears exactly half the time
        # This means A appears as many times as all others combined
        if count_a * 2 == total_chars:
            print("YES")
        else:
            print("NO")

# Alternative solution using mathematical check
def solve_alternative():
    t = int(input())
    
    for _ in range(t):
        s = input().strip()
        n = len(s)
        count_a = sum(1 for char in s if char == 'A')
        
        # For A to equal all others: count_a == (n - count_a)
        # Simplifying: 2 * count_a == n
        print("YES" if 2 * count_a == n else "NO")

if __name__ == "__main__":
    solve()
