# baekjoon 2588 곱셈

a, b = int(input()), int(input())
c = a * b
for i in range(3):
    print(a * (b%10))
    b //= 10
print(c)