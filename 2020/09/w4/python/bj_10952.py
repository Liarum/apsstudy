# baekjoon 10951. A+B -5

# 두 정수 A, B 를 입력받은 다음 A + B를 출력
"""
1 1
2 3
3 4
9 8
5 2
0 0
"""

from sys import stdin, stdout

while 1:
    a, b = map(int, stdin.readline().split())
    if a==0 and b==0:
        break
    stdout.write(str(a+b)+"\n")