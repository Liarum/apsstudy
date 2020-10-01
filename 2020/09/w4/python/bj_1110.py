# baekjoon 1110. 더하기 사이클

N = int(input())

"""
10보다 작으면 앞에 0을 붙여 두자리 수로 만들고 각 자리의 숫자를 더한다.
주어진 수의 오른쪽 자리 수와, 앞에서 구한 합의 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
"""

new_num = N

units = (new_num//10 + new_num%10) % 10
tens = (new_num % 10) * 10
new_num = tens + units

cycle_cnt = 1


while new_num != N:
    units = (new_num//10 + new_num%10) % 10
    tens = (new_num % 10) * 10
    new_num = tens + units

    cycle_cnt += 1

print(cycle_cnt)
