# baekjoon 2577. 숫자의 개수

from sys import stdin, stdout

A = int(stdin.readline())
B = int(stdin.readline())
C = int(stdin.readline())

num_str = str(A*B*C)
cnt_i = [0] * 10

for i in num_str:
    cnt_i[int(i)] += 1

for j in range(10):
    stdout.write(str(cnt_i[j])+"\n")