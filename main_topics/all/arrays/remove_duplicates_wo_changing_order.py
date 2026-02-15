#remove duplicates from a list without changing order
user_input = input().split()
array = list(map(int,user_input))

list_wo_duplicates = list(dict.fromkeys(array))
print(list_wo_duplicates)