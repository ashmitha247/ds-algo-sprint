user_input = input()
array = map(int,user_input.split())
first_largest = float("-inf")
second_largest = float("-inf")
for i in array:
    if i > first_largest:
        second_largest = first_largest
        first_largest = i
    elif i > second_largest:
        second_largest = i
print(second_largest)
        

'''

We take first largest and second largest as -infinity.
we go through each element in array.
if i > first largest, we make first largest as i AND second largest takes the value of first largest.
NOTE: first opeartion is to make second largest = first largest so that sceond largest takes the value of first largest
and THEN first largest will receive the value of i. order matters.

there is a case where say in the array: [10 2 3]
10 is greater than -inf so first largest is 10 and second largest is -inf
2 is not greater than 10 but second largest = -inf is greater. 
so to account for the case of i > second largest, we use the elif case. '''