#Write the code to find the length of the array without len keyword
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

# 1. Get the first array (limit to 2 elements)
print("Enter numbers for the first array:")
array1 = list(map(int, input().split()))[:2]

# 2. Get the second array (limit to 5 elements)
print("Enter numbers for the second array:")
array2 = list(map(int, input().split()))[:5]

# 3. Merge them
merged_array = array1 + array2
print(f"Merged Array: {merged_array}")
dict = {}
for i in merged_array:
    if i in dict:
        dict[i]+=1
    else:
        dict[i] = 1
print(dict)
count = 0
for value in dict.values():
    count += value
print(count)

''' I'm summing the value in the dict to find the total number of elements in the array. 
    There are other methods as well.'''

