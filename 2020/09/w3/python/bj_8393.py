# baekjoon 8393. 합

n = int(input())
print((n+1) * (n//2)) if n % 2 == 0 else print((1+n) * (n//2) + (n//2+1))