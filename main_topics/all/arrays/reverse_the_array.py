user_input = input().split()
array= list(map(int,user_input))
ans = array[::-1]
print(*ans)