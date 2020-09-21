# baekjoon 10799. 쇠막대기

from sys import stdin, stdout

bar = stdin.readline()

total_splits = 0
left_brackets = 0

for i in range(len(bar)):
    if bar[i] == "(":
        left_brackets += 1
        total_splits += 1
    else:
        if bar[i-1] == "(":
            left_brackets -= 1
            total_splits -= 1   
            total_splits += left_brackets
        else:
            left_brackets -= 1

print(total_splits)