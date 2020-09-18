# baekjoon 10871. X보다 작은 수

from sys import stdin, stdout

n, x = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
check = [0] * n

for i in range(n):
    if nums[i] < x:
        check[i] = 1

for i in range(n):
    if check[i]:
        print(str(nums[i]), end=" ")


#########################################
a,b = map(int,input().split())
score = [x for x in input().split() if int(x)<b]
print(' '.join(score))