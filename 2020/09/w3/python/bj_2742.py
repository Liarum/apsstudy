# baekjoon 2742. 기찍 N


from sys import stdin, stdout

n = int(stdin.readline())
for i in range(n, 0, -1):
    stdout.write(str(i) + '\n')