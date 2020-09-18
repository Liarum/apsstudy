# baekjoon 15552. 빠른 A+B
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)






#######################################
from sys import stdin, stdout

readline = stdin.readline
write = stdout.write

n = int(readline())
for _ in range(n):
    a, b = readline().split()
    write(str(int(a) + int(b)) + '\n')