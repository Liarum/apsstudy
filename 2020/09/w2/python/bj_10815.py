from sys import stdin, stdout

n = int(stdin.readline())
cards = tuple(map(int, stdin.readline().split()))

m = int(stdin.readline())
nums = tuple(map(int, stdin.readline().split()))

ret_dict = {}
for i in range(m):
    ret_dict[nums[i]] = 0

for i in range(n):
    if cards[i] in ret_dict:
        ret_dict[cards[i]] += 1
    else:
        continue

for val in ret_dict.values():
    print(val, end=' ')




######################################


# n = int(stdin.readline())
# cards = tuple(map(int, stdin.readline().split()))

# m = int(stdin.readline())
# nums = tuple(map(int, stdin.readline().split()))

# for num in nums:
#     print("1", end=" ") if num in cards else print("0", end=" ")