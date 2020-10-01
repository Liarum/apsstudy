# baekjoon 1546. 평균
N = int(input())

scores = list(map(int, input().split()))
M = max(scores)
total = 0

# 점수/M*100
for score in scores:
    total +=  score / M * 100

print(total/N)

####
# print((lambda _, arr:sum(list(map(lambda x: x / max(arr) * 100, arr))) / len(arr))(input(), list(map(int, input().split()))))

#####
# N = int(input())

# scores = list(map(int, input().split()))
# M = max(scores)

# for i in range(N):
#     scores[i] = scores[i] / M*100
# avg = sum(scores)/ N
# print(avg)