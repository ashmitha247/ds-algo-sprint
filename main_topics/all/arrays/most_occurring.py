#Write the code to find the length of the array without len
'''
input format:

2
23 39
5
87 34 56 34 22

It means that if n = 2, we need to take only 2 elements in the array(which the user will enter)
We have two arrays like this.
For the first array, user will input n, which is the number of elements in the array, AND they will also
input the elements of the array. same for the sceond array.
then, we merge those two arrays.
and from this array, we find out which is the most repeating element. 
even if user enters more numbers than specified n, the input will take only n number of elements in the array.'''

# 1. Get the first array (limit to n1 elements)
n1 = int(input("Enter number of elements of 1st array: "))
print("Enter elements for the first array:")
array1 = list(map(int, input().split()))[:n1]

# 2. Get the second array (limit to n2 elements)
n2 = int(input("Enter number of elements of 2nd array: "))
print("Enter elements for the second array:")
array2 = list(map(int, input().split()))[:n2]

# 3. Merge them
merged_array = array1 + array2
print(f"Merged Array: {merged_array}")
dict = {}
for i in merged_array:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] +=1
max_so_far = float("-inf")
key = None
for key,value in dict.items():
    if value > max_so_far:
        max_so_far = value
        key_key = key

print(f"The element {key_key} has repeated the most number of times i.e {max_so_far} times")