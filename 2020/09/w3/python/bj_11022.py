# baekjoon 11022. A+B -8


from sys import stdin, stdout

n = int(stdin.readline())
nums = tuple(tuple(map(int, stdin.readline().split())) for _ in range(n))

for i in range(n):
    stdout.write("Case #%d: %d + %d = %d\n" % (i+1, nums[i][0], nums[i][1], nums[i][0] + nums[i][1]))