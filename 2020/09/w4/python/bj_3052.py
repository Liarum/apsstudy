# baekjoon 3052. 나머지



####### sol1. python 의 set 이용
remainder_set = set()

for _ in range(10):
    n = int(input())
    remainder_set.add(n%42)

print(len(remainder_set))

######## sol2. check list 이용

check_list = [0] * 42
for _ in range(10):
    n = int(input())
    check_list[n%42] = 1

result = 0
for i in range(42):
    if check_list[i] == 1:
        result += 1

print(result)

