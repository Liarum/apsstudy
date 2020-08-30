# baekjoon 10869 사칙연산

numbs = input().split()
calc_dict = {0:lambda a,b: a+b, 1:lambda a,b: a-b, 2:lambda a,b: a*b, 3: lambda a,b: int(a/b), 4:lambda a,b: a%b}
for _ in range(5):
    print(calc_dict[_](int(numbs[0]), int(numbs[1])))
