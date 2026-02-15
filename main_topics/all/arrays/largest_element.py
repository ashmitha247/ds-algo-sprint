#find the largest element in an array

user_input = input("Enter numbers: ").split()
array = map(int, user_input)
max_so_far = float("-inf")
for i in array:
    i = int(i)
    if i > max_so_far:
        max_so_far = i
print(max_so_far)
