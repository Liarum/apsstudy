# baekjoon 10950. A+B - 3

n = int(input())
nums = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    print(nums[i][0] + nums[i][1])