# baekjoon 10818. 최소, 최대

N = int(input())
nums = list(map(int, input().split()))

min_num = 1000000
max_num = -1000000
for n in nums:
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n

print("{} {}".format(min_num, max_num))