 # baekjoon 1932. 정수삼각형

# 아래층에 있는 수는 위 층의 대각선 왼 아래, 오른 아래만 선택할 수 있다
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-2, -1, -1):
    for j in range(i+1):
        nums[i][j] += max(nums[i+1][j], nums[i+1][j+1])
        
print(nums[0][0])




###################################################################################################

# n = int(input())
# nums = [list(map(int, input().split())) for _ in range(n)]

# max_sum = 0
# for i in range(n):
#     cur_max = max_sum
#     for j in range(i+1):
#         if nums[i][j] + cur_max > max_sum:
#             max_sum = nums[i][j] + cur_max

# print(max_sum)



