user_input = input("Enter numbers: ")
# Convert to a list so we can use len() and indexing [i]
array = list(map(int, user_input.split()))

n = len(array)
result = "Yes" # Assume it is sorted

for i in range(n - 1):
    # If the current number is bigger than the next one, it's NOT sorted
    if array[i] > array[i+1]:
        result = "No"
        break  # We found a problem, so we can stop looking!

print(result)

'''
Why we use range(n-1)
We stop at n-1 because if we went all the way to n,
the very last check would try to compare the last number with array[i+1],
which doesn't exist! This prevents an IndexError. '''