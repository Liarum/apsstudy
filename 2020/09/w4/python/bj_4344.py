# baekjoon 4344. 평균은 넘겠지

from sys import stdin, stdout

c = int(stdin.readline())

for _ in range(c):
    tc = list(map(int, stdin.readline().split()))
    avr_score = sum(tc[1:]) // tc[0]

    h_avr = 0
    for score in tc[1:]:
        if score > avr_score:
            h_avr += 1

    stdout.write("%.3f" % round((h_avr / tc[0])*100, 3) + "%\n")