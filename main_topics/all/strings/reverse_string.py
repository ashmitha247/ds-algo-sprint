'''user_input = input().split(',')
array= list(map(str, user_input))
ans = array[::-1]
print(*ans) '''


#easier way:
user_input = input().split(',')
print(*list(reversed(user_input)))

'''
gold,silver,wood
wood silver gold '''