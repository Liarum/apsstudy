# baekjoon 1330 두 수 비교하기

a, b = input().split()
a, b = int(a), int(b)

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
